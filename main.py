from common import BASE_URL, USERNAME
from network import NetClient

def main():
    print('========== 请先输入你的学号和密码 ==========')
    USERNAME = input('学号：').strip()
    PASSWORD = input('密码：').strip()
    client = NetClient(base_url= BASE_URL)
    response = client.get(path_or_url='/course-selection-api/api/v1/student/course-select/99899/turn/1321/select')

if __name__ == '__main__':
    main()

