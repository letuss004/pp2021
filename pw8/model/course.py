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
