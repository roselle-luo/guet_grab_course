from dataclasses import dataclass, asdict
from typing import Optional
import common

@dataclass
class CourseQueryParams:
    adminclassId: str = ""
    campusId: Optional[int] = 3
    canSelect: Optional[int] = None  # 是否可选
    courseNameOrCode: str = ""  # 课程名或编号
    coursePropertyId = ""
    courseSubstitutePoolId: Optional[int] = None
    courseTypeId: str = ""  # 课程类型
    creditGte: Optional[float] = None
    creditLte: Optional[float] = None
    departmentId: str = ""  # 上课学院，编号同开课学院
    grade: str = ""  # 年级
    hasCount: Optional[int] = None
    ids: list[int] = None
    lessonNameOrCode: str = ""  # 教学班名
    majorId: str = ""  # 上课专业
    openDepartmentId: str = ""  # 开课学院
    pageNo: int = 1  # 页数
    pageSize: int = 20  # 页面大小
    semesterId: int = 281  # 学期
    sortField: str = "course"  # 暂时先固定
    sortType: str = "ASC"  # 暂时先固定
    studentId: int = common.STUDENT_ID  # 学生ID
    substitutedCourseId: Optional[int] = None
    teacherNameOrCode: str = ""  # 上课老师
    turnId: int = 1321  # 暂时先固定
    week: str = ""  # 在星期几上课
    _canSelect: str = ""  # 是否可选，只能填写为 “可选” 或 “不可选”

    def to_dict(self):
        return asdict(self)