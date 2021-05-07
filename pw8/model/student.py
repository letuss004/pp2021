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