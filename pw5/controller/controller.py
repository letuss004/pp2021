from zipfile import ZipFile
from pw5.model.data_base import *
import os


def check_s_id(input_sid):
    """

    :param input_sid:
    :return: True if exits
    """
    for i in st_list:
        if input_sid == i.get_st_id():
            return True
    return False


def check_c_id(input_cid):
    """

    :param input_cid:
    :return: True is exits
    """
    for i in course_list:
        if input_cid == i.get_id():
            return True
    return False


def check_sid_cid_on_mark(input_sid, input_cid):
    index = -1
    for i in marks_list:
        index += 1
        if input_cid == i.get_c_id() and input_sid == i.get_s_id():
            return True, index
    return False, index


def check_sid_in_mark(input_sid):
    """

    :param input_sid:
    :return: True is exits
    """
    for i in marks_list:
        if input_sid == i.get_s_id():
            return True
    return False


def check_cid_in_mark(input_cid):
    """

    :param input_cid:
    :return: True is exits
    """
    for i in marks_list:
        if input_cid == i.get_c_id():
            return True
    return False


def find_sid_index_in_mark(input_cid):
    """

    :param input_cid:
    :return:
    """
    index = -1
    for i in marks_list:
        index += 1
        if input_cid == i.get_id():
            return index
    return -1


def get_id_name_cour_list():
    """

    :return: return value of combobox
    """
    id_name_cour_list = []
    for c in course_list:
        c_name = str(c.get_name())
        cid = str(c.get_id())
        id_name_cour_list.append(cid + ": " + c_name)
    return id_name_cour_list


def filter_cid_cbb(id_name_cour):
    """

    :param id_name_cour:
    :return:
    """
    id_name_cour = str(id_name_cour)
    list_id_name = id_name_cour.split(": ")
    id_after_filter = list_id_name[0]
    return id_after_filter


def get_st_gpa(sid):
    try:
        mark_total = 0
        count = 0
        for mark in marks_list:
            if sid == mark.get_s_id():
                mark_total += float(mark.get_mark())
                count += 1
        return mark_total / count
    except ZeroDivisionError:
        return False


def compress_data():
    with ZipFile("student.dat", "w") as file:
        file.write("student.txt")
        file.write("mark.txt")
        file.write("course.txt")
    # remove file not necessary
    os.remove("student.txt")
    os.remove("mark.txt")
    os.remove("course.txt")


def extract_data():
    try:
        with ZipFile("student.dat", "r") as file:
            for member in file.namelist():
                file.extract(member)
    except FileNotFoundError:
        pass
