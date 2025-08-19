from enum import Enum


class CourseType(Enum):
    Must = 1,  # 必修课
    General = 2,  # 通识课
    MajorLimit = 3,  # 专业限选
    NoMajorLimit = 4,  # 专业任选
    Practice = 21  # 实践
