from dataclasses import dataclass


@dataclass
class CourseOut:
    id: str = ''
    course_name: str = ''
    teacher: list[str] = None
    credits: str = ''
    type: str = ''

    def out(self):
        print(f'id: {self.id}')
        print(f'name: {self.course_name}')
        print(f'teacher: {self.teacher}')
        print(f'type: {self.type}')
        print(f'credits: {self.credits}')
        print('\n')
