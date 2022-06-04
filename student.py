# ----------------------------------------------------------------
# Author:Dylan Intriago
# Date:06/04/2022
#
# Original implementation: This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# Refactored by Joshua Pierce to be a student class
# -----------------------------------------------------------------

class Student:

    def __init__(self, id, password, in_state=False):
        self.student_id = id
        self.student_password = password
        self.state_status = in_state

    def check_password(self, attempt):
        return attempt == self.student_password
