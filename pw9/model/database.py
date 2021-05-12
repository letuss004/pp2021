import mysql.connector as cnt

database = cnt.connect(host="localhost", user="root", passwd="12345678", database="smm")
cursor = database.cursor()


# st_formula = 'insert into student (id, name, dob) values (%s, %s, %s)'
# st_tuple = ["Ba1", "Tu", "13/08/2000"]
# condi = "SELECT * FROM student"
# condi = "SELECT * FROM "
#
# cursor.execute(condi)
# rs = cursor.fetchall()
#
# print(rs)

def check_s_id(input_sid):
    """

    :param input_sid:
    :return: True if exits
    """
    condition = f"select * from student where id = '{str(input_sid)}'"
    cursor.execute(condition)
    rs = cursor.fetchone()
    if rs is None:
        return False
    return True


def check_c_id(input_cid):
    """

    :param input_cid:
    :return: True is exits
    """
    condition = f"select * from course where id = '{str(input_cid)}'"
    cursor.execute(condition)
    rs = cursor.fetchone()
    if rs is None:
        return False
    return True


def check_sid_cid_exist_on_mark(input_sid, input_cid):
    condition = f"select * from mark where s_id = '{str(input_sid)}' and c_id = '{str(input_cid)}'"
    cursor.execute(condition)
    rs = cursor.fetchone()
    if rs is None:
        return False
    return True


def get_all_sts_inf():
    condition = f"SELECT * FROM student"
    cursor.execute(condition)
    rs = cursor.fetchall()
    return rs


def get_all_courses_inf():
    condition = f"SELECT * FROM course"
    cursor.execute(condition)
    rs = cursor.fetchall()
    return rs


def get_all_marks_inf():
    condition = f"SELECT * FROM mark"
    cursor.execute(condition)
    rs = cursor.fetchall()
    return rs


def get_id_name_cour_list():
    """

    :return: return value of combobox
    """
    id_name_of_cour_list = []
    condition = f"SELECT * FROM course"
    cursor.execute(condition)
    rs = cursor.fetchall()
    # rs = [(.,.,.), (.,.,.)]
    for course in rs:
        cid = course[0]
        c_name = course[1]
        id_name_of_cour_list.append(cid + ": " + c_name)
    return id_name_of_cour_list


def get_st_gpa(sid):
    # make sure that sid is already exist
    # if sid is not exits method return false
    condition = f"SELECT mark FROM mark WHERE s_id = '{str(sid)}'"
    cursor.execute(condition)
    data = cursor.fetchall()
    # print(rs) = [(Decimal('15'),), (....)]
    # print(rs[0][0]) = 15
    try:
        mark_total = 0
        count = 0
        for mark in data:
            mark_total += mark[0]
            count += 1
        return mark_total / count
    except ZeroDivisionError:
        return False


# def get_st_gpa_sql  (sid):
#     condition = f"SELECT AVG(gpa) FROM student WHERE id = '{str(sid)}'"
#     cursor.execute(condition)
#     rs = cursor.fetchone()
#     print(rs)
#     return rs


def add_student_to_db(s_id, name, dob):
    condition = f"INSERT INTO student (id, name, dob, gpa)" \
                f"VALUES ('{str(s_id)}', '{str(name)}', '{str(dob)}', '0')"
    cursor.execute(condition)
    database.commit()
    pass


def add_course_to_db(c_id, name):
    condition = f"INSERT INTO course (id, name)" \
                f"VALUES ('{str(c_id)}', '{str(name)}')"
    cursor.execute(condition)
    database.commit()
    pass


def add_mark_to_db(sid, cid, mark):
    condition = f"INSERT INTO mark (s_id, c_id, mark)" \
                f"VALUES ('{str(sid)}', '{str(cid)}', '{float(mark)}')"
    cursor.execute(condition)
    database.commit()
    pass


def add_mark_to_db_if_overlap(sid, cid, mark):
    condition = f"UPDATE mark SET mark = '{mark}' WHERE s_id = '{sid}' AND c_id = '{cid}'"
    cursor.execute(condition)
    database.commit()
    pass


def set_st_gpa(sid):
    condition = f"UPDATE student SET gpa = {get_st_gpa(sid)} WHERE id = '{sid}'"
    cursor.execute(condition)
    database.commit()


def sort_st_list_by_name_up():
    condition = f"SELECT * FROM student ORDER BY name ASC"
    cursor.execute(condition)


def sort_st_list_by_name_down():
    condition = f"SELECT * FROM student ORDER BY name DESC"
    cursor.execute(condition)
    pass


def sort_st_list_by_id_up():
    condition = f"SELECT * FROM student ORDER BY id ASC"
    cursor.execute(condition)
    pass


def sort_st_list_by_id_down():
    condition = f"SELECT * FROM student ORDER BY id DESC"
    cursor.execute(condition)
    pass


def sort_st_list_by_dob_up():
    condition = f"SELECT * FROM student ORDER BY dob ASC"
    cursor.execute(condition)
    pass


def sort_st_list_by_dob_down():
    condition = f"SELECT * FROM student ORDER BY dob DESC"
    cursor.execute(condition)
    pass


def sort_st_list_by_gpa_up():
    condition = f"SELECT * FROM student ORDER BY gpa ASC"
    cursor.execute(condition)
    pass


def sort_st_list_by_gpa_down():
    condition = f"SELECT * FROM student ORDER BY gpa DESC"
    cursor.execute(condition)
    pass


def sort_cour_list_by_id_up():
    condition = f"SELECT * FROM course ORDER BY id ACS"
    cursor.execute(condition)
    pass


def sort_cour_list_by_id_down():
    condition = f"SELECT * FROM course ORDER BY id DESC"
    cursor.execute(condition)
    pass


def sort_cour_list_by_name_up():
    condition = f"SELECT * FROM course ORDER BY name ACS"
    cursor.execute(condition)
    pass


def sort_cour_list_by_name_down():
    condition = f"SELECT * FROM course ORDER BY name DESC"
    cursor.execute(condition)
    pass
