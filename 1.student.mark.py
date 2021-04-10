"""
:author: Le Anh Tu
:ID: Ba9-067 
:Lab work: 1
"""
# --------lists-----------
studentName = []
studentID = []
studentDoB = []
courseID = []
courseName = []
studentInformation = {}


# ------------------------------ menu -------------------------------------
def menu_option():
    print("1. Set information for student: ")
    print("2. Set information for course: ")
    print("3. Set mark for student by course: ")
    print("4. Get information for student: ")
    print("5. Get information for course: ")
    print("6. Get information for student course management: ")
    print("0. Quit.")


# ------------------------------ function's option -------------------------------------
def input_domain(value, min_value, max_value):
    while value < min_value or value > max_value:
        value = int(input("Your input is invalid! Enter again: "))
    return value


def set_inf_student():
    global i
    student_number = int(input("Enter number of student: "))
    student_number = input_domain(student_number, 1, 999999)
    # --------list-----------
    for i in range(0, student_number):
        print("The order of student in class: %d ------------------------------" % (i + 1))
        a = str(input("Enter student ID: "))
        b = str(input("Enter student name: "))
        c = str(input("Enter student DoB: "))
        studentID.append(a)
        studentName.append(b)
        studentDoB.append(c)


def set_inf_course():
    global i

    courses_number = int(input("Enter number of courses: "))
    courses_number = input_domain(courses_number, 0, 999999)
    # --------list-----------
    for i in range(0, courses_number):
        print("The order of course in courses: %d ------------------------------" % (i + 1))
        a = str(input("Enter course name: "))
        b = str(input("Enter course ID: "))
        courseName.append(a)
        courseID.append(b)


def get_st_inf():
    global i
    for i in range(0, len(studentName)):
        print("This is the information of " + studentName[i] + ": ")
        print("student name is: " + studentName[i])
        print("student id is: " + studentID[i])
        print("student DoB is: " + studentDoB[i])


def get_cour_inf():
    global i
    for i in range(0, len(courseName)):
        print("This is the information of " + courseName[i] + ": ")
        print("This is name of course: " + courseName[i])
        print("This is id of course: " + courseID[i])


def cond_quit(input_value, min_value, max_value):
    if min_value < input_value < max_value:
        a = True
    else:
        a = False
        print("You choose quit! Thank for using my program.")
    return a


# ------------------------------ menu option -------------------------------------
print("Program started !!!")
menu_option()
choice = int(input("Enter your choice: "))

while choice != 0:
    break_point = False
    if choice == 1:
        set_inf_student()

        print("---------------------End of this choice---------------------")
        menu_option()
        choice = int(input("Do u want to get more choice: "))
        if not cond_quit(choice, 0, 6):
            break

    elif choice == 2:
        min_op = 0
        max_op = 6
        set_inf_course()

        print("---------------------End of this choice---------------------")
        menu_option()
        choice = int(input("Do u want to get more choice: "))
        if not cond_quit(choice, 0, 6):
            break

    elif choice == 3:
        name = str(input("Enter name of student u want to manage: "))
        st_cour_mang = {}
        check_stop = False
        for i in range(0, len(studentName)):
            if studentName[i] == name:
                check_stop = True
                stcourse = int(input("How many course " + studentName[i] + " is learning: "))
                while stcourse > len(courseName) or stcourse < 0:
                    print("course amount is run out of course number you entered! Enter again: ")
                    stcourse = int(input("How many course " + studentName[i] + " is learning: "))
                for j in range(0, stcourse):
                    checka = False
                    name_course_curr = str(input("Enter course name to manage: "))
                    for k in range(0, len(courseName)):
                        if name_course_curr == courseName[k]:
                            checka = True
                            mark = int(input("Enter mark of " + name_course_curr + ": "))
                            st_cour_mang[name_course_curr] = mark
                            studentInformation[name] = st_cour_mang
                            break
                    if not check_stop or not checka:
                        print("----------------- course name input not found!----------------- ")
                        if not check_stop:
                            exit(100)
        if not check_stop:
            print("----------------- student name input not found!----------------- ")
            exit(100)
        print("---------------------End of this choice---------------------")
        menu_option()
        choice = int(input("Do u want to get more choice: "))
        if 0 > choice > 6:
            print("You choose quit! Thank for using my program.")
            break
    elif choice == 4:
        get_st_inf()

        choice = int(input("Do u want to get more choice: "))
    elif choice == 5:
        get_cour_inf()

        choice = int(input("Do u want to get more choice: "))
    elif choice == 6:
        print(studentInformation)
        choice = int(input("Do u want to get more choice: "))
    else:
        print("You choose quit! Thank for using my program.")
        break
