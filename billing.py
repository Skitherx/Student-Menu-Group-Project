# Andrew Nguyen
# Date:06/04/2022
# Billing portion of the project
# Refactored by Joshua Pierce to be inline with the proposed OOP restructuring

from database import Database

IN_STATE_TUITION = 225
OUT_OF_STATE_TUITION = 850


def calculate_hours_and_bill(student, database):
    student_courses = database.get_courses_of_student(student.student_id)
    total_hours = 0
    for i in student_courses:
        total_hours += i.course_hours

    if student.state_status:
        bill = total_hours * IN_STATE_TUITION
    else:
        bill = total_hours * OUT_OF_STATE_TUITION

    display_hours_and_bill(total_hours, bill)


def display_hours_and_bill(c_hours, cost):
    print(f"Course Hour Amount:{c_hours} hours")
    print(f"Enroll Cost: ${cost}")

