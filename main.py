from dotenv import load_dotenv

from utils import json_perfect_out

load_dotenv(dotenv_path='env.env')
import common

from network import NetClient
from select_course import select_course, drop_course
from get_courses import search_course, get_selected_courses
from monitor import grab_course
from model.course_out import CourseOut


def main():
    print('========== 初始化环境 ==========')
    client = NetClient(base_url= common.BASE_URL)
    print_menu()
    # training_plan_courses = client.get(path_or_url='/course-selection-api/api/v1/student/course-select/selected-lessons/1321/99899')
    # json_perfect_out(training_plan_courses.json())
    #select_course()
    #search_course(course_name='（网络）')
    grab_course(course_name='（网络）')

def print_menu():
    print('\n选择要进行的功能：')
    print('1. 查看已选课程')
    print('2. 查看培养方案课程')
    print('3. 根据id持续监控抓取某个课程')
    print('4. 根据课程名字或老师名字搜索课程')
    print('5. 根据课程名字持续监控抓取某个课程')

if __name__ == '__main__':
    main()

