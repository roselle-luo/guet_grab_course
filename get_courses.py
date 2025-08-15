import json
from dataclasses import asdict

import common
from model.get_course_param import CourseQueryParams
from network import NetClient
from utils import json_perfect_out


def get_courses(course_name, teacher_name, page_num: int = None, page_size: int = None):
    client = NetClient()
    path = f'/course-selection-api/api/v1/student/course-select/query-lesson/{common.STUDENT_ID}/1321'
    param = CourseQueryParams()
    param.courseNameOrCode = course_name
    param.teacherNameOrCode = teacher_name
    param.coursePropertyId = 2
    if page_num and page_size:
        param.pageNo = page_num
        param.pageSize = page_size
    print(param.to_dict())
    response = client.post(path_or_url=path, json=param.to_dict())
    data = response.json()['data']
    lessons = data['lessons']
    page_info = data['pageInfo']
    print(len(lessons))
    for i in lessons:
        print(i['teachers'])
    print(page_info)

def test():
    client = NetClient()
    response1 = client.get('/simplest-lessons/static/lessons/1321/version.json')
    number = response1.json()['itemList'][0]
    response2 = client.get(f'/simplest-lessons//static/lessons/1321/{number}.json')

    # data 字段是字符串，需要先转成 JSON 对象
    courses = json.loads(response2.json()['data'])

    print(len(courses))

    def fix_chinese(s):
        if s:
            return s.encode('latin1').decode('utf-8')
        return s

    for c in courses:
        c['courseName'] = fix_chinese(c.get('courseName'))
        c['lessonName'] = fix_chinese(c.get('lessonName'))
        c['teacherName'] = fix_chinese(c.get('teacherName'))
        c['openDepartment'] = fix_chinese(c.get('openDepartment'))
    # 写入本地文件
    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)

    print("课程数据已写入 courses.json")