from course import Course
from student import Student


class Database:

    def __init__(self):
        self.courses = {'CSC101': Course('CSC101', 3, 3, ['1004', '1003']),
                        'CSC102': Course('CSC102', 4, 2, ['1001']),
                        'CSC103': Course('CSC103', 5, 1, ['1002']),
                        'CSC104': Course('CSC104', 3, 3)}

        self.students = {'1001': Student('1001', '111', True),
                         '1002': Student('1002', '222'),
                         '1003': Student('1003', '333', True),
                         '1004': Student('1004', '444')}

    def student_id_list(self):
        temp = []
        for id in self.students:
            temp.append(self.students[id].student_id)
        return temp

    def course_name_list(self):
        temp = []
        for name in self.courses:
            temp.append(self.courses[name].course_name)
        return temp

    def course_contains_student(self, id, course):
        return id in self.courses[course].course_roster

    def get_courses_of_student(self, id):
        temp = []
        for c in self.courses:
            if id in self.courses[c].course_roster:
                temp.append(self.courses[c])
        return temp

    def display_courses_of_student(self, id):
        temp = []
        for course in self.get_courses_of_student(id):
            temp.append(course.course_name)
        print(temp)

