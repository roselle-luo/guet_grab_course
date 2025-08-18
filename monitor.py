import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from get_courses import search_course
from select_course import select_course


def monitor_course(course_name, teacher_name=''):
    courses = search_course(course_name=course_name, teacher_name=teacher_name)
    if courses:
        return courses
    else:
        return None



def grab_course(course_name, teacher_name='', interval=2, max_workers=5):
    while True:
        courses = monitor_course(course_name=course_name, teacher_name=teacher_name)
        if courses:
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = [executor.submit(select_course, course['id']) for course in courses]
                # 可选：等待所有任务完成
                for future in as_completed(futures):
                    try:
                        result = future.result()
                        print("选课结果:", result)
                    except Exception as e:
                        print("错误:", e)
            break
        time.sleep(interval)
