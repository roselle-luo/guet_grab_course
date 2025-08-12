import common
from network import NetClient


def select_course(lesson_id):
    client = NetClient()
    data = {
        "coursePackAssoc": None,
        "courseSelectTurnAssoc": 1321,
        "requestMiddleDtos": [
            {
                "lessonAssoc": lesson_id,
                "virtualCost": 0
            }
        ],
        "studentAssoc": common.STUDENT_ID
    }
    response = client.post(path_or_url='/course-selection-api/api/v1/student/course-select/add-request', json= data)
    result_id = response.json()['data']
    result = client.get(path_or_url=f'/course-selection-api/api/v1/student/course-select/add-drop-response/99899/{result_id}').json()
    print(f'请求结果: {result['data']['success']}\n原因: {result['data']['errorMessage']}\n')

def drop_course(lesson_id):
    client = NetClient()
    data = {
        "coursePackAssoc": None,
        "courseSelectTurnAssoc": 1321,
        "lessonAssocs": [
            lesson_id
        ],
        "studentAssoc": common.STUDENT_ID
    }
    response = client.post(path_or_url='/course-selection-api/api/v1/student/course-select/drop-request', json= data)
    result_id = response.json()['data']
    result = client.get(path_or_url=f'/course-selection-api/api/v1/student/course-select/add-drop-response/99899/{result_id}').json()
    print(f'请求结果: {result['data']['success']}\n原因: {result['data']['errorMessage']}\n')