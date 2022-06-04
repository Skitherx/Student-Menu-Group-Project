# Author: Joshua Pierce
# menu system that allows the user to add, drop, display their courses, and show the bill
#

from database import Database
from billing import calculate_hours_and_bill
database = Database()


def menu(student):
    if student is None:
        return
    userinput = str(input(""""Enter '1' to Add a course|
           '2' to Drop a course|
           '3' to View your courses|
           '4' to show your bill |
           '5' logout|
           '6' exit|
            """))

    if userinput == "1":
        course_input = input("Please enter a course you would like to add: ")
        if course_input in database.course_name_list():
            database.courses[course_input].add_student(student.student_id)
        else:
            print("That course does not exist")
        menu(student)

    elif userinput == "2":
        course_input = input("Please enter a course you would like to drop: ")
        if course_input in database.course_name_list():
            database.courses[course_input].remove_student(student.student_id)
        else:
            print("That course does not exist")
        menu(student)

    elif userinput == '3':
        database.display_courses_of_student(student.student_id)
        menu(student)

    elif userinput == "4":
        calculate_hours_and_bill(student, database)
        menu(student)

    elif userinput == "5":
        print("Exiting to login")
        menu(login())

    elif userinput == "6":
        print("Good bye")
        return
    else:
        print("That option is invalid")
        menu(student)


def login():
    while 1:
        stud = input("Please enter your id: ")
        if stud in database.student_id_list():
            studobj = database.students[stud]
            password = input("Please enter the password: ")
            if studobj.check_password(password):
                print(f"Log in successful {stud}")
                return studobj
            else:
                print("incorrect password")
        else:
            print("Id not found")
    else:
        print(f"ID {stud} is not found in the database")


