import logging

network_logger = logging.getLogger("NetClient")
network_logger.setLevel(logging.DEBUG)  # 输出所有调试信息
ch = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s", datefmt="%H:%M:%S")
ch.setFormatter(formatter)
network_logger.addHandler(ch)