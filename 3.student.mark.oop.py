"""
Overview:
    - Student Mark Management (practice work 4)
    - File name: 3.student.mark.oop.py
    - Fix all bug (I tried)
    - Good user interface design 
    - Comment and documentation are available 

Author:
    - Le Anh Tu

User Note:           ---------- YOU MUST READ THIS THINGS ----------
    - To anyone who is reading this file
    - Please clone my python module package
    - Named PythonStore at https://github.com/letuss004/pp2021
    - If not this program will die

System Note:
    - " - " + message = system's input
    - "---" + message = system's output
    - "" + message = system's required re-input
    - [n] = choices

    - SMM = Student Mark Management
    - CMM = Course Mark Management
"""

import PythonStore.ControllerStore as Cs
import PythonStore.StringStore as Ss
import math
import numpy as np


# ------------------------------ classes -------------------------------------

class Student:

    def __init__(self, name, s_id, dob):
        self.__stdName = name
        self.__stdID = s_id
        self.__stdDoB = dob
        self.__gpa = 0

    def set_st_name(self, name):
        self.__stdName = name

    def set_st_id(self, std_id):
        self.__stdID = std_id

    def set_st_dob(self, dob):
        self.__stdDoB = dob

    def set_st_gpa(self, gpa):
        self.__gpa = gpa

    def get_st_gpa(self):
        return self.__gpa

    def get_st_name(self):
        return self.__stdName

    def get_st_id(self):
        return self.__stdID

    def get_st_dob(self):
        return self.__stdDoB


class Course:

    def __init__(self, name, c_id):
        self.__name = name
        self.__id = c_id

    def set_c_name(self, name):
        self.__name = name

    def set_c_id(self, c_id):
        self.__id = c_id

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id


class Mark:

    def __init__(self, c_id, s_id, mark):
        self.__mark = mark
        self.__s_id = s_id
        self.__c_id = c_id

    def get_mark(self):
        return self.__mark

    def get_s_id(self):
        return self.__s_id

    def get_c_id(self):
        return self.__c_id


class SMM:
    # i create this to manage student and mark
    # but it not necessary

    def __init__(self, s_id, smm):
        self.__s_id = s_id
        self.__smm = smm

    def get_smm(self):
        return self.__smm

    def get_s_id(self):
        return self.__s_id


class Main:
    # ------------------------------ database -------------------------------------

    st_list = [Student(None, None, None)]
    course_list = [Course(None, None)]
    marks_list = [Mark(None, None, None)]
    smm_list = [SMM(None, Mark(None, None, None))]

    st_list.clear()
    course_list.clear()
    smm_list.clear()

    # ------------------------------ engine -------------------------------------

    def check_s_id(self, s_id):
        # if sid is on st_list => return True
        check = False
        for i in self.st_list:
            if i.get_st_id() == s_id:
                check = True
        return check

    def check_c_id(self, c_id):
        # if c_id is on st_list => return True
        check = False
        for i in self.course_list:
            if i.get_id() == c_id:
                check = True
        return check

    def quit_menu_full(self):
        self.end_of_choice()
        self.menu_full()
        choice = Cs.integer_controller(" - Make other choice, 0 to quit: ", 0, 8)
        return choice

    def input_s_id(self, sid):
        while self.check_s_id(sid):
            sid = self.input_s_id(Cs.input_identifier(
                "This student id is already exist, enter another :"))
        return sid

    def input_c_id(self, cid):
        while self.check_c_id(cid):
            cid = self.input_c_id(Cs.input_identifier(
                "This course id is already exist, enter another: "))
        return cid

    def function_2(self):
        c_id = self.input_c_id(Cs.input_identifier(
            " - Enter course id you want to add: "))
        c_name = Cs.input_a_s_controller(
            " - Enter course name you want to add: ", "Course name")
        self.course_list.append(Course(c_name, c_id))

    def function_1(self):
        s_id = self.input_s_id(Cs.input_identifier(
            " - Enter student id you want to add: "))
        s_name = Cs.input_a_s_controller(
            " - Enter student name you want to add: ", "Student name")
        s_dob = Cs.input_dob(
            " - Enter student date of birth you want to add: ")
        self.st_list.append(Student(s_name, s_id, s_dob))

    def end_of_choice(self):
        print("\n---------------------End of this choice---------------------\n")

    def menu_1(self):
        print("[1] Set information for all student in class. ")
        print("[2] Set information for all course in class. ")
        print("[0] Exit.\n")

    def menu_course(self):
        print("[1] Set information for course. ")
        print("[0] Exit.\n")

    def menu_st(self):
        print("[1] Set information for student. ")
        print("[0] Exit.\n")

    def menu_2(self):
        print("[1] Set information for student. ")
        print("[2] Set information for course. ")
        print("[3] Set mark for student by course. ")
        print("[4] Get information for student. ")
        print("[5] Get information for course. ")
        print("[0] Exit.\n")

    def menu_full(self):
        print("[1] Set information for student. ")
        print("[2] Set information for course. ")
        print("[3] Set mark for student by course. ")
        print("[4] Get information for student. ")
        print("[5] Get information for course. ")
        print("[6] Get information for student mark management. ")
        print("[7] Get information for course mark management. ")
        print("[8] Sort student list by GPA descending.")
        print("[0] Quit.\n")

    def function_full(self, message_choice):
        # choice_for_menu is already secured by Cs.input_controller(message_choice, 0, 8).
        choice_for_menu = Cs.integer_controller(message_choice, 0, 8)
        while True:

            # Student add function
            if choice_for_menu == 1:
                self.function_1()
                choice_for_menu = self.quit_menu_full()

            # Course add function
            elif choice_for_menu == 2:
                self.function_2()
                choice_for_menu = self.quit_menu_full()

            # Set mark for student by course.
            elif choice_for_menu == 3:
                self.function_3()
                choice_for_menu = self.quit_menu_full()

            # Get information for student.
            elif choice_for_menu == 4:
                self.function_4()
                choice_for_menu = self.quit_menu_full()

            # Get information for course.
            elif choice_for_menu == 5:
                self.function_5()
                choice_for_menu = self.quit_menu_full()

            # Get information for student mark management.
            elif choice_for_menu == 6:
                self.function_6()
                choice_for_menu = self.quit_menu_full()

            # Get information for course mark management.
            elif choice_for_menu == 7:
                self.function_7()
                choice_for_menu = self.quit_menu_full()

            # Sort student list by GPA descending.
            elif choice_for_menu == 8:
                self.function_8()
                choice_for_menu = self.quit_menu_full()

            # Quit.
            elif choice_for_menu == 0:
                print("You choose quit! Thank for using my program.")
                break
            else:
                choice_for_menu = Cs.integer_controller(
                    "Your input was wrong, make other choice, 0 to quit: ", 0, 8)

    def function_8(self):
        # sort student information by GPA based on bubble sort algorithm

        if len(self.st_list) != 1:
            for i in range(len(self.st_list)):
                for j in range(len(self.st_list) - 1):
                    if self.st_list[j].get_st_gpa() > self.st_list[j + 1].get_st_gpa():
                        self.st_list[j], self.st_list[j + 1] = self.st_list[j + 1], self.st_list[j]
            self.st_list.reverse()

    # def function_9(self):
    #     self.st_list.sort(key=getattr(self.st_list[0], "__gpa"), reverse=False)

    def function_7(self):
        # force input corresponding course id
        c_id = Cs.input_identifier(
            " - Enter course id you want to get information of CMM: ")
        while not self.check_c_id(c_id):
            c_id = Cs.input_identifier(
                " - This course's id is not in system, enter again: ")

        # get all mark of this course | if statement will execute when there is nothing to show
        check = False
        for i in self.marks_list:
            if i.get_c_id() == c_id:
                check = True
                print("---The course's id: " + i.get_c_id() + ", mark : "
                      + str(i.get_mark()) + ", student's id : " + i.get_s_id())
        if check:
            print("---This course did not contains any information.")

    def function_6(self):
        # force input corresponding student id
        s_id = Cs.input_identifier(
            " - Enter student id you want to get information of SMM: ")
        while not self.check_s_id(s_id):
            s_id = Cs.input_identifier(
                "This student's id is not in system, enter again: ")

        # list all mark this student have studied
        check = False
        print("The student's id is " + s_id + " have completed the following course: ")
        for i in self.marks_list:
            if i.get_s_id() == s_id:
                check = True
                print("---The course's id: " + i.get_c_id() + " with mark : " + str(i.get_mark()) + ".")

        if not check:
            print("---This student did not contains any information.")

        # Print GPA
        for i in self.st_list:
            if i.get_st_id() == s_id and check:
                print("---So, the GPA is: %d" % i.get_st_gpa())

    def function_5(self):
        for i in range(0, len(self.course_list)):
            print("---Course name: " + self.course_list[i].get_name(), end=", ")
            print("ID: " + self.course_list[i].get_id())

    def function_4(self):
        for i in range(0, len(self.st_list)):
            print("---Student name: " + self.st_list[i].get_st_name(), end=", ")
            print("ID: " + self.st_list[i].get_st_id(), end=", ")
            print("DoB: " + self.st_list[i].get_st_dob())

    def function_3(self):
        # input student id
        s_id = Cs.input_identifier(" - Enter student id you want to manage: ")
        while not self.check_s_id(s_id):
            s_id = Cs.input_identifier(" - This student's id is not in system, enter again: ")

        # if this function is overload in database, it will reset all mark information of this student
        for i in self.marks_list:
            if i.get_s_id() == s_id:
                i.__init__(None, None, None)

        # input number of course want to manage
        am_of_course = Cs.input_integer_not_exception(" - How many course this student was study: ")
        while am_of_course > len(self.course_list) or am_of_course < 0:
            am_of_course = Cs.input_integer_not_exception("There is only " + str(len(self.course_list)) +
                                                          " courses you can not add more than them. Enter again:")
        # am_of_course is true => CMM
        c_id_current = []  # c_id_current is list to store the already c_id inputted
        for i in range(0, am_of_course):

            # force input for course id must in database
            c_id = Cs.input_identifier(" - Enter course id you want to add: ")
            while not self.check_c_id(c_id):
                c_id = Cs.input_identifier(" - This course's id is not in system, enter again: ")

            # check to find out this did this course is inputted
            # if yes force input course id
            # then append this c_id into list of c_id_current
            # c_id_current is list to store the already c_id inputted
            while c_id in c_id_current:
                c_id = self.function_3_mini_check(c_id, c_id_current)
            c_id_current.append(c_id)

            # mark for this course, ordered by PythonStore.StringStore.ordinal
            m = Cs.input_controller(" - Enter mark of course " + Ss.ordinal(i + 1) + ": ", 0.0, 20.0)
            mark = math.floor(m)
            self.marks_list.append(Mark(c_id, s_id, mark))
        self.function_gpa(s_id)

    def function_3_mini_check(self, c_id, c_id_current):
        for j in c_id_current:
            if c_id == j:
                c_id = Cs.input_identifier(
                    " - This course already inputted, choose another: ")
                while not self.check_c_id(c_id):
                    c_id = Cs.input_identifier(
                        " - This course's id is not in system, enter again: ")
        return c_id

    def function_gpa(self, s_id):

        mark_count = 0
        count_time = 0
        for i in self.marks_list:
            if i.get_s_id() == s_id:
                mark_count += i.get_mark()
                count_time += 1
        gpa = mark_count / count_time

        for i in self.st_list:
            if i.get_st_id() == s_id:
                i.set_st_gpa(gpa)
                break

    def function_gpa_np(self, s_id):
        # function_gpa but using numpy

        arr_mark = np.array([])
        count = 0
        # add all mark to arr_mark
        for i in self.marks_list:
            if i.get_s_id() == s_id:
                count += 1
                np.append(arr_mark, [i.get_mark()])

        # calculate summation of course's mark
        mark_count = 0
        for i in arr_mark:
            print(i)
            mark_count += i
        gpa = mark_count / count

        # set student gpa
        for i in self.st_list:
            if i.get_st_id() == s_id:
                i.set_st_gpa(gpa)
                break
        pass

    def function_for_menu2(self, choice_menu_2, message_choice):
        # menu option for menu 2
        # force user input 3 if not => unable to full menu options

        while True:
            """ Seeing comment for this block at function_full method"""

            if choice_menu_2 == 1:
                self.function_1()
                self.end_of_choice()
                self.menu_2()
                choice_menu_2 = Cs.integer_controller(" - Make other choice, 0 to quit: ", 0, 5)

            elif choice_menu_2 == 2:
                self.function_2()
                self.end_of_choice()
                self.menu_2()
                choice_menu_2 = Cs.integer_controller(" - Make other choice, 0 to quit: ", 0, 5)

            elif choice_menu_2 == 3:
                self.function_3()
                self.end_of_choice()

                # Course and Student are done => menu_full appear => full functionality
                self.menu_full()
                self.function_full(message_choice)
                break

            elif choice_menu_2 == 4:
                self.function_4()
                self.end_of_choice()
                self.menu_2()
                choice_menu_2 = Cs.integer_controller(" - Make other choice, 0 to quit: ", 0, 5)

            elif choice_menu_2 == 5:
                self.function_5()
                self.end_of_choice()
                self.menu_2()
                choice_menu_2 = Cs.integer_controller(" - Make other choice, 0 to quit: ", 0, 5)

            elif choice_menu_2 == 0:
                print("You choose quit! Thank for using my program.")
                break

            else:
                choice_menu_2 = Cs.integer_controller(
                    "Your input was wrong, make other choice, 0 to quit: ", 0, 8)

    def start_engine(self):
        print("\n ------------------------ PROGRAM IS STARTED ------------------------ \n\n")

        # Select functionality in the first menu
        self.menu_1()
        message_choice = " - Select the functionality by input the corresponding number: "
        choice_menu1 = Cs.integer_controller(message_choice, 0, 2)

        if choice_menu1 == 1:
            # Student add is selected, setting .....
            am_of_st = Cs.input_integer_not_exception(" - Enter amount of in the class you want to add: ")
            for i in range(0, am_of_st):
                self.function_1()
            self.end_of_choice()

            # Student completed => menu2 appear => Course information setting
            self.menu_course()
            choice_menu_1_2 = Cs.integer_controller(message_choice, 0, 1)

            if choice_menu_1_2 == 1:
                am_of_cor = Cs.input_integer_not_exception(
                    " - Enter amount of course you want to add: ")
                for i in range(0, am_of_cor):
                    self.function_2()
                self.end_of_choice()

                # Course and Student are done => menu_full 2 appear
                self.menu_2()
                choice_menu_2 = Cs.integer_controller(message_choice, 0, 5)
                self.function_for_menu2(choice_menu_2, message_choice)

            else:
                print("Thank for using my program! Good Bye !!!")
                exit(0)

        elif choice_menu1 == 2:
            am_of_c = Cs.input_integer_not_exception(
                " - Enter amount of courses you want to add: ")
            for i in range(0, am_of_c):
                self.function_2()
            self.end_of_choice()

            # course inputting completed => menu2 appear => Student information setting
            self.menu_st()
            choice_menu_1_2 = Cs.integer_controller(message_choice, 0, 1)

            if choice_menu_1_2 == 1:
                am_of_st = Cs.input_integer_not_exception(
                    " - Enter amount of student in the class you want to add: ")
                for i in range(0, am_of_st):
                    self.function_1()
                self.end_of_choice()

                # Course and Student are done => menu_full 2 appear
                self.menu_2()
                choice_menu_2 = Cs.integer_controller(message_choice, 0, 5)
                self.function_for_menu2(choice_menu_2, message_choice)

                # Course and Student are done => menu_full appear => full functionality
                self.menu_full()
                choice_menu_full = Cs.integer_controller(message_choice, 0, 5)
                self.function_full(choice_menu_full)
            else:
                print("Thank for using my program! Good Bye !!!")
                exit(0)

        elif choice_menu1 == 0:
            print("You choose quit! Thank for using my program.")
            exit(0)


if __name__ == '__main__':
    main = Main()
    main.start_engine()

