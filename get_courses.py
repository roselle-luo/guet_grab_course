import common
import json
from model.get_course_param import CourseQueryParams
from network import NetClient


def get_courses(course_name, teacher_name, ids, page_num: int = None, page_size: int = None):
    client = NetClient()
    path = f'/course-selection-api/api/v1/student/course-select/query-lesson/{common.STUDENT_ID}/1321'
    param = CourseQueryParams()
    param.courseNameOrCode = course_name
    param.teacherNameOrCode = teacher_name
    param.ids = ids
    if page_num and page_size:
        param.pageNo = page_num
        param.pageSize = page_size
    response = client.post(path_or_url=path, json=param.to_dict())
    data = response.json()['data']
    lessons = data['lessons']
    page_info = data['pageInfo']
    return lessons

def search_preview(courses, name = '', teacher = ''):
    return [item for item in courses if name in item['courseName'].lower() and teacher in item['teacherName'].lower()]

def search_course(course_name = '', teacher_name=''):
    client = NetClient()
    all_course_number = client.get('/simplest-lessons/static/lessons/1321/version.json')
    number = all_course_number.json()['itemList'][0]
    all_course = client.get(f'/simplest-lessons//static/lessons/1321/{number}.json')
    # data 字段是字符串，需要先转成 JSON 对象
    courses = json.loads(all_course.json()['data'])
    print(f'总课程数量：{len(courses)}')

    # 结果编码不一样，得先调整编码
    def fix_chinese(s):
        if s:
            return s.encode('latin1').decode('utf-8')
        return s
    # 执行编码调整
    for c in courses:
        c['courseName'] = fix_chinese(c.get('courseName'))
        c['lessonName'] = fix_chinese(c.get('lessonName'))
        c['teacherName'] = fix_chinese(c.get('teacherName'))
        c['openDepartment'] = fix_chinese(c.get('openDepartment'))

    # 先从本地找到对应课程ids
    courses = search_preview(courses=courses, name=course_name, teacher=teacher_name)
    ids = [course['id'] for course in courses]
    print(f'先行找到的ids：{ids}')
    lessons = get_courses(course_name=course_name, teacher_name=teacher_name, ids=ids)
    print(lessons)


def save_courses(courses):
    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)
    print("课程数据已写入 courses.json")