from dotenv import load_dotenv
load_dotenv(dotenv_path='env.env')
import common

from network import NetClient
from select_course import select_course, drop_course
from get_courses import search_course
from monitor import grab_course


def main():
    print('========== 初始化环境 ==========')
    client = NetClient(base_url= common.BASE_URL)
    # training_plan_courses = client.get(path_or_url='/course-selection-api/api/v1/student/course-select/selected-lessons/1321/99899')
    # json_perfect_out(training_plan_courses.json())
    #select_course()
    #get_courses(course_name='EE', teacher_name='肖', page_num=1, page_size=300)
    grab_course(course_name='形势与政策5')

if __name__ == '__main__':
    main()

