import re

from bs4 import BeautifulSoup
from requests import Session

import common
from crypto import crypto_login_password


def login(session: Session, username, password):
    print(f'当前登录账户：{username}')
    salt = session.get("https://bkjwtest.guet.edu.cn/student/ldap/login-salt").text
    encrypt_password = crypto_login_password(password, salt)
    form = {
        'username': username,
        'password': encrypt_password
    }
    response1 = session.post("https://bkjwtest.guet.edu.cn/student/ldap/login", json=form)
    #print(response1.text)
    response2 = session.get("https://bkjwtest.guet.edu.cn/student/for-std/course-select",allow_redirects=True)
    token = parse_token(response2.text)
    cookie = 'cs-course-select-student-token=' + token
    authorization = token
    header = {
        'Authorization': authorization,
        'Cookie': cookie
    }
    session.headers.update(header)
    student_id_response = session.get('https://bkjwtest.guet.edu.cn/course-selection-api/api/v1/student/course-select/students')
    common.STUDENT_ID = student_id_response.json()['data'][0]


def parse_token(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_html = str(soup.body)
    match = re.search(r"token=([A-Za-z0-9_\-\.]+)", body_html)
    if match:
        token = match.group(1)
        return token
    else:
        return 'token not found'
