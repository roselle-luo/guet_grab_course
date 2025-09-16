import time

import requests

from logger import network_logger
from common import USERNAME, PASSWORD, MODE
from login import login


def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class NetClient:
    def __init__(self, base_url=None):
        self.session = requests.session()
        self.base_url = base_url.rstrip("/") if base_url else None
        headers = self.session.headers
        has_cookie = "Cookie" in headers and bool(headers["Cookie"].strip())
        has_auth = "Authorization" in headers and bool(headers["Authorization"].strip())
        if not has_cookie and not has_auth:
            login(self.session, USERNAME, PASSWORD)


    def get(self, path_or_url, **kwargs):
        url = self._full_url(path_or_url)
        start = time.time()
        resp = self.session.get(url, **kwargs)
        elapsed = time.time() - start
        self._log_request("GET", url, elapsed, resp, **kwargs)
        resp.raise_for_status()
        return resp

    def post(self, path_or_url, data=None, json=None, **kwargs):
        url = self._full_url(path_or_url)
        start = time.time()
        resp = self.session.post(url, data=data, json=json, **kwargs)
        elapsed = time.time() - start
        self._log_request("POST", url, elapsed, resp, data=data, json=json, **kwargs)
        resp.raise_for_status()
        return resp

    def _log_request(self, method, url, elapsed, resp, **kwargs):
        network_logger.info('========== Begin ==========')
        network_logger.info(f"[{method}] {url}")
        if kwargs.get("params"):
            network_logger.debug(f"Params: {kwargs['params']}")
        if kwargs.get("data"):
            network_logger.debug(f"Data: {kwargs['data']}")
        if kwargs.get("json"):
            network_logger.debug(f"JSON: {kwargs['json']}")
        network_logger.info(f"Status: {resp.status_code} | Time: {elapsed:.2f}s | Size: {len(resp.content)} bytes")
        network_logger.debug(f"Response: {resp.text[:200]}{'...' if len(resp.text) > 200 else ''}")
        network_logger.info('========== End ==========\n')

    def _full_url(self, path_or_url):
        if path_or_url.startswith("http"):
            return path_or_url
        if not self.base_url:
            raise ValueError("Base URL not set, and path is not a full URL")
        return f"{self.base_url}/{path_or_url.lstrip('/')}"