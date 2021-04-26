import pw4.domains.DataBase as Db


def filter_cbb_func3(input_id_name):
    """"""
    # ba1: math
    input_id_name = str(input_id_name)
    list_id_name = input_id_name.split(": ")
    id_after_fil = list_id_name[0]
    print(id_after_fil)
    return id_after_fil


def check_s_id(input_sid):
    """

    :param input_sid:
    :return: True if exits
    """
    for i in Db.st_list:
        if input_sid == i.get_st_id():
            return True
    return False


def check_c_id(input_cid):
    """

    :param input_cid:
    :return: True is exits
    """
    for i in Db.course_list:
        if input_cid == i.get_id():
            return True
    return False


def input_c_id(inputs, label_annotation, color="red"):
    """

    :param inputs:
    :param label_annotation:
    :param color:
    :return:
    """
    if check_c_id(inputs):
        label_annotation.config(text="This id is already exist", fg=color)
        return False
    else:
        return True


def input_s_id(inputs, label_annotation, color="red"):
    if check_s_id(inputs):
        label_annotation.config(text="This id is already exist", fg=color)
        return False
    else:
        return True


def save_mark_db(cid, sid, mark):
    print(str(cid) + "= cid||" + str(sid) + " sid||" + str(mark) + "= mark||" + "------------")
    check = True
    for i in Db.marks_list:

        if i.get_c_id() == cid and i.get_s_id() == sid:
            print("co o trong db")
            i.set_mark(mark)
            check = False
            break
    if check:
        print("k co o trong db")
        Db.marks_list.append(Db.Mark(cid, sid, mark))
