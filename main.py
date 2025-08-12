from dotenv import load_dotenv

from utils import json_perfect_out

load_dotenv(dotenv_path='env.env')
import common
from network import NetClient
from select_course import select_course, drop_course


def main():
    print('========== 初始化环境 ==========')
    client = NetClient(base_url= common.BASE_URL)
    print(common.STUDENT_ID)
    training_plan_courses = client.get(path_or_url='/course-selection-api/api/v1/student/course-select/selected-lessons/1321/99899')
    #select_course()


if __name__ == '__main__':
    main()

