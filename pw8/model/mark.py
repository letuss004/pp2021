class Mark:

    def __init__(self, c_id, s_id, mark):
        self.__mark = mark
        self.__s_id = s_id
        self.__c_id = c_id

    def set_cid(self, cid):
        self.__c_id = cid

    def set_sid(self, sid):
        self.__s_id = sid

    def set_mark(self, mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark

    def get_s_id(self):
        return self.__s_id

    def get_c_id(self):
        return self.__c_id