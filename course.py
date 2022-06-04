#
# Author: Dylan Intriago
# Manipulates a list of students by ID, and contains useful information relating to the course
#

class Course:

    def __init__(self, name, hours, size, roster=None):
        self.course_name = name
        self.course_max_size = size
        self.course_hours = hours
        if roster is None:
            self.course_roster = []
        else:
            self.course_roster = roster

    def remove_student(self, student_id):
        if student_id in self.course_roster:
            self.course_roster.remove(student_id)
            print(f"Student removed from course {self.course_name}")
        else:
            print(f"{student_id} is not in this course")

    def add_student(self, student_id):
        if self.is_roster_at_max():
            print(f"Max roster reached\nCannot add anymore students to {self.course_name}")
            return
        if student_id not in self.course_roster:
            self.course_roster.append(student_id)
            print(f"Student added to course {self.course_name}")
        else:
            print(f"{student_id} is already in this course")

    def is_roster_at_max(self):
        return len(self.course_roster) == self.course_max_size

    def display_course(self):
        print(self.course_roster)



