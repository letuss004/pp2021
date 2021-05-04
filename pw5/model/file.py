from pw5.controller.controller import *
from pw5.model.student import Student
from pw5.model.course import Course
from pw5.model.mark import Mark


def write_data_to_file():
    student = open("student.txt", "w+")
    course = open("course.txt", "w+")
    mark = open("mark.txt", "w+")
    # writing
    for S in st_list:
        # text for writing
        student_string = S.get_st_name() + "|" + S.get_st_id() + "|" + \
                         S.get_st_dob() + "|\n"
        # write to file
        student.write(student_string)

    for C in course_list:
        # text for writing
        course_string = C.get_name() + "|" + C.get_id() + "|\n"
        # write to file
        course.write(course_string)

    for M in marks_list:
        #
        mark_string = M.get_c_id() + "|" + M.get_s_id() + "|" + str(M.get_mark()) + "|\n"
        # write
        mark.write(mark_string)
    # closing
    student.close()
    course.close()
    mark.close()


def read_data_from_file():
    try:
        student = open("student.txt", "r")
        # reading and adding to data_base
        for line in student:
            inf_list = line.split("|")
            #
            st_list.append(Student(inf_list[0], inf_list[1], inf_list[2]))
        # file closing
        student.close()
    except FileNotFoundError:
        pass

    try:
        course = open("course.txt", "r")
        # reading and adding to data_base
        for line in course:
            inf_list = line.split("|")
            #
            course_list.append(Course(inf_list[0], inf_list[1]))
        # file closing
        course.close()
    except FileNotFoundError:
        pass

    try:
        mark = open("mark.txt", "r")
        # reading and adding to data_base
        for line in mark:
            inf_list = line.split("|")
            #
            marks_list.append(Mark(inf_list[0], inf_list[1], int(inf_list[2])))
        # file closing
        mark.close()
    except FileNotFoundError:
        pass
