import pickle

import pw8.model.data_base as db
from pw8.model.course import Course
from pw8.model.mark import Mark
from pw8.model.student import Student


def write_data_to_file():
    student = open("student.txt", "w+")
    course = open("course.txt", "w+")
    mark = open("mark.txt", "w+")
    # writing
    for S in db.st_list:
        # text for writing
        student_string = S.get_st_name() + "|" + S.get_st_id() + "|" + \
                         S.get_st_dob() + "|\n"
        # write to file
        student.write(student_string)

    for C in db.course_list:
        # text for writing
        course_string = C.get_name() + "|" + C.get_id() + "|\n"
        # write to file
        course.write(course_string)

    for M in db.marks_list:
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
            db.st_list.append(Student(inf_list[0], inf_list[1], inf_list[2]))
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
            db.course_list.append(Course(inf_list[0], inf_list[1]))
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
            db.marks_list.append(Mark(inf_list[0], inf_list[1], int(inf_list[2])))
        # file closing
        mark.close()
    except FileNotFoundError:
        pass

def write_data_by_pickle():
    student = open("student.txt", "wb")
    course = open("course.txt", "wb")
    mark = open("mark.txt", "wb")
    #
    pickle.dump(db.st_list, file=student)
    pickle.dump(db.course_list, file=course)
    pickle.dump(db.marks_list, file=mark)
    #
    student.close()
    course.close()
    mark.close()


def read_data_by_pickle():
    try:
        student = open("student.txt", "rb")
        course = open("course.txt", "rb")
        mark = open("mark.txt", "rb")
        #
        db.st_list = pickle.load(student)
        db.course_list = pickle.load(course)
        db.marks_list = pickle.load(mark)
        #
        student.close()
        course.close()
        mark.close()
        #
        # print(db.st_list)
        # print(db.course_list)
        # print(db.marks_list)
    except FileNotFoundError:
        # print("alo")
        pass
