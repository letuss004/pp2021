import tkinter as tk
import PythonStore.GUI.ControllerStore as Cs
import pw4.domains.DataBase as Db
import tkinter.ttk as ttk
import pw4.input as ip


class Root(tk.Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.geometry("450x400")
        self.title("Student Mark Management")

        container = tk.Frame(self)
        container.grid()

        self.frame_dic = {}
        # , Func4Frame,Func5Frame, Func6Frame, Func7Frame, Func8Frame
        #
        for i in (MenuFrame, Func1Frame, Func2Frame, Func3Frame, Func4Frame, Func5Frame, Func6Frame):
            frame = i(container, self)
            self.frame_dic[i] = frame

        self.show_frame(MenuFrame)

    def show_frame(self, frame_input):
        frame_showed = self.frame_dic[frame_input]
        frame_showed.grid(row=0, column=0, sticky="NSEW")
        frame_showed.tkraise()


class MenuFrame(tk.Frame):
    def __init__(self, container, attr_main):
        super(MenuFrame, self).__init__(container)

        lb1 = tk.Label(self, text="Select the functionality by click buttons")
        lb1.grid(padx=5, pady=5)

        butt_st_inf = tk.Button(self, text="Set information for all student in class",
                                command=lambda: attr_main.show_frame(Func1Frame))
        butt_st_inf.grid(padx=5, pady=5, sticky="W")

        butt_c_inf = tk.Button(self, text="Set information for course",
                               command=lambda: attr_main.show_frame(Func2Frame))
        butt_c_inf.grid(padx=5, pady=5, sticky="w")

        bt_func3 = tk.Button(self, text="Set mark for student", command=lambda: attr_main.show_frame(Func3Frame))
        bt_func3.grid(padx=5, pady=5, sticky="w")

        bt_func4 = tk.Button(self, text="Get student information", command=lambda: attr_main.show_frame(Func4Frame))
        bt_func4.grid(padx=5, pady=5, sticky="w")

        bt_func5 = tk.Button(self, text="Get student information", command=lambda: attr_main.show_frame(Func5Frame))
        bt_func5.grid(padx=5, pady=5, sticky="w")

        bt_func6 = tk.Button(self, text="Get SMM information", command=lambda: attr_main.show_frame(Func6Frame))
        bt_func6.grid(padx=5, pady=5, sticky="w")


# -------------------Func1Frame-----------------------
class Func1Frame(tk.Frame):
    entries_inf = []

    def __init__(self, container, attr_main):
        super(Func1Frame, self).__init__(container)
        #
        lb1 = tk.Label(self, text="Input the correct information")
        lb1.grid(column=2, row=0, padx=25, pady=5)

        self.entry_name()
        self.entry_id()
        self.entry_dob()

        bt1 = tk.Button(self, text="<-", command=lambda: attr_main.show_frame(MenuFrame))
        bt1.grid(column=0, row=0, sticky="NW")

        bt2 = tk.Button(self, text="Enter", command=lambda: [self.check_input()])
        bt2.grid(column=2, row=7)

        bt2 = tk.Button(self, text="Clear", command=lambda: self.clear_entries())
        bt2.grid(column=2, row=8)

    def check_input(self):
        length = len(self.entries_inf)
        # check variable for checking name, dob, id
        check1, check2, check3 = False, False, False
        # name -> id -> dob
        for i in range(0, length):
            #
            if i == 0:  # name
                check1 = Cs.input_a_s_controller(self.et_name.get(), self.lb_ano_name, "Name")
            if i == 1:  # id
                if Cs.input_identifier(self.et_id.get(), self.lb_ano_id) \
                        and ip.input_s_id(self.et_id.get(), self.lb_ano_id):
                    check2 = True
                # check2 = Cs.input_identifier(self.et_id.get(), self.lb_ano_id) and
                #          ip.input_s_id(self.et_id.get(), self.lb_ano_id)
            if i == 2:  # dob
                check3 = Cs.input_dob(self.et_dob.get(), self.lb_ano_dob)
                # if all true => save in database
        if check1 and check2 and check3:
            Db.st_list.append(Db.Student(self.et_name.get(), self.et_id.get(), self.et_dob.get()))

    def clear_entries(self):
        self.et_dob.delete(0, "end")
        self.et_id.delete(0, "end")
        self.et_name.delete(0, "end")
        self.clear_lb_ano()

    def clear_lb_ano(self):
        self.lb_ano_dob.config(text="", fg="red")
        self.lb_ano_id.config(text="", fg="red")
        self.lb_ano_name.config(text="", fg="red")

    def entry_dob(self):
        etl1 = tk.Label(self, text="DoB*", fg="red")
        etl1.grid(column=0, row=5, padx=10)

        self.et_dob = tk.Entry(self, width=50)
        self.et_dob.grid(column=2, row=5, padx=10, pady=0)

        self.lb_ano_dob = tk.Label(self, text="")
        self.lb_ano_dob.grid(column=2, row=6)

        self.entries_inf.append(self.et_dob.get())

    def entry_id(self):
        etl1 = tk.Label(self, text="ID*", fg="red")
        etl1.grid(column=0, row=3, padx=10)

        self.et_id = tk.Entry(self, width=50)
        self.et_id.grid(column=2, row=3, padx=10, pady=0)

        self.lb_ano_id = tk.Label(self, text="")
        self.lb_ano_id.grid(column=2, row=4)

        self.entries_inf.append(self.et_id.get())

    def entry_name(self):
        etl1 = tk.Label(self, text="Name*", fg="red")
        etl1.grid(column=0, row=1, padx=10)

        self.et_name = tk.Entry(self, width=50)
        self.et_name.grid(column=2, row=1, padx=10, pady=0)

        self.lb_ano_name = tk.Label(self, text="")
        self.lb_ano_name.grid(column=2, row=2)

        self.entries_inf.append(self.et_name.get())

    # def check_entry


# -------------------Func2Frame-----------------------
class Func2Frame(tk.Frame):
    entries_inf = []

    def __init__(self, container, attr_main):
        super(Func2Frame, self).__init__(container)
        #
        lb1 = tk.Label(self, text="Input the correct information")
        lb1.grid(column=1, row=0, padx=25, pady=5)
        #
        self.entry_name()
        self.entry_id()
        #
        bt1 = tk.Button(self, text="<-", command=lambda: attr_main.show_frame(MenuFrame))
        bt1.grid(column=0, row=0, sticky="NW")
        #
        butt_enter = tk.Button(self, text="Enter", command=lambda: [self.check_input()])
        butt_enter.grid(column=1, row=7)
        #
        butt_clear = tk.Button(self, text="Clear", command=lambda: self.clear_entries())
        butt_clear.grid(column=1, row=8)

    def check_input(self):
        length = len(self.entries_inf)
        # check variable for checking name, dob, id
        check1, check2 = False, False
        # name -> id -> dob
        for i in range(0, length):
            #
            if i == 0:  # name
                check1 = Cs.input_a_s_controller(self.et_name.get(), self.lb_ano_name, "Name")
            if i == 1:  # id
                if Cs.input_identifier(self.et_id.get(), self.lb_ano_id) \
                        and ip.input_c_id(self.et_id.get(), self.lb_ano_id):
                    check2 = True
                # check2 = Cs.input_identifier(self.et_id.get(), self.lb_ano_id)
        # if all true => save in database
        if check1 and check2:
            Db.st_list.append(Db.Course(self.et_name.get(), self.et_id.get()))

    def clear_entries(self):
        self.et_id.delete(0, "end")
        self.et_name.delete(0, "end")
        self.clear_lb_ano()

    def clear_lb_ano(self):
        self.lb_ano_id.config(text="", fg="red")
        self.lb_ano_name.config(text="", fg="red")

    def entry_id(self):
        etl1 = tk.Label(self, text="ID*", fg="red")
        etl1.grid(column=0, row=3, padx=10)

        self.et_id = tk.Entry(self, width=50)
        self.et_id.grid(column=1, row=3, padx=10, pady=0)

        self.lb_ano_id = tk.Label(self, text="")
        self.lb_ano_id.grid(column=2, row=4)

        self.entries_inf.append(self.et_id.get())

    def entry_name(self):
        etl1 = tk.Label(self, text="Name*", fg="red")
        etl1.grid(column=0, row=1, padx=10)

        self.et_name = tk.Entry(self, width=50)
        self.et_name.grid(column=1, row=1, padx=10, pady=0)

        self.lb_ano_name = tk.Label(self, text="")
        self.lb_ano_name.grid(column=2, row=2)

        self.entries_inf.append(self.et_name.get())


# -------------------Func3Frame-----------------------------------------------------
class Func3Frame(tk.Frame):
    def __init__(self, container, attr_main):
        super(Func3Frame, self).__init__(container)
        # label for display that y can use this function or not
        lb_ano_full_cond = tk.Label(self, text="Waiting for condition checking")
        lb_ano_full_cond.grid(column=1, row=0)
        #
        self.entry_sid()
        #
        butt_back = tk.Button(self, text="<-",
                              command=lambda: attr_main.show_frame(MenuFrame))
        butt_back.grid(column=0, row=0, sticky="NW")
        #
        self.butt_enter = tk.Button(self, text="Enter", command=lambda: [self.enter_command()])

        self.butt_enter.grid(column=1, row=3, pady=10)
        #
        self.butt_clear = tk.Button(self, text="Clear")
        self.butt_clear.grid(column=2, row=3, pady=10)

    def enter_command(self):
        # try:
        self.get_sid_method()
        self.disp_sname_method()
        self.input_sid_func()
        #

    # except AttributeError:
    #     print("Enter button appear Exception because cbb_cour did not declare yet!!!!!!!!!!")
    #     pass

    def input_sid_func(self):
        # every important ------------------------------------
        #
        if ip.check_s_id(self.s_id):
            #
            # self.butt_enter.grid(column=1, row=5, pady=10)
            self.butt_clear.grid(column=2, row=5, pady=10)
            self.butt_enter.destroy()
            #
            self.combobox_cour()
        else:
            # try:
            #     self.combobox_cour_destroy()
            # except AttributeError:
            #     print("ComboBox courses destroy appear Exception because lb_et_1 did not declare yet!!!!!!!!!!!!!!")
            pass

    def entry_sid(self):
        lb_et_1 = tk.Label(self, text="Student ID*", fg="red")
        lb_et_1.grid(column=0, row=1, padx=5)
        #
        self.et_sid = tk.Entry(self, width=20)
        self.et_sid.grid(column=1, row=1, padx=0)
        #
        self.lb_ano_name = tk.Label(self, text="", fg="red")
        self.lb_ano_name.grid(column=1, row=2, sticky="n")
        #
        self.lb_et_dis_s_name = tk.Label(self, text="Student name: ")
        self.lb_et_dis_s_name.grid(column=2, row=1, padx=0, sticky="W")
        #

    def get_sid_method(self):
        self.s_id = self.et_sid.get()

    def disp_sname_method(self):
        s_name = "Student name: "
        for i in Db.st_list:
            if i.get_st_id() == self.s_id:
                s_name = s_name + " " + i.get_st_name()
                break
        self.lb_et_dis_s_name.config(text=s_name)

    def but_new_enter_command(self):
        self.get_sid_method()
        self.disp_sname_method()
        if ip.check_s_id(self.s_id):
            self.smm()
            self.print()
        else:
            self.combobox_cour_destroy()

    def combobox_cour(self):
        self.lb_et_1 = tk.Label(self, text="Course ID|Name:", fg="red")
        self.lb_et_1.grid(column=0, row=3)
        # new enter button
        self.but_enter_new = tk.Button(self, text="Enter Mark",
                                       command=lambda: [self.but_new_enter_command(), self.smm])
        self.but_enter_new.grid(column=1, row=5, pady=10)
        #
        cour_inf_list = []
        #
        for i in Db.course_list:
            c_name = str(i.get_name())
            cid = str(i.get_id())
            cour_inf_list.append(cid + ": " + c_name)
        # crete a Combobox of cour name
        self.cbb_cour = ttk.Combobox(self, value=cour_inf_list, width=20, state="readonly")
        self.cbb_cour.grid(column=1, row=3)
        #
        self.lb_mark = tk.Label(self, text="Mark")
        self.lb_mark.grid(column=2, row=2)
        # entry for input mark
        self.et_mark = tk.Entry(self, width=10)
        self.et_mark.grid(column=2, row=3)
        # function for manage SMM
        # get cid from

    def combobox_cour_destroy(self):
        self.lb_et_1.destroy()
        self.cbb_cour.destroy()
        self.lb_mark.destroy()
        self.et_mark.destroy()

    def smm(self):
        cid = ip.filter_cbb_func3(self.cbb_cour.get())
        print("day la smm method and cid is " + cid)
        ip.save_mark_db(cid, self.s_id, self.et_mark.get())

    def print(self):
        for i in Db.marks_list:
            print(str(i.get_s_id()) + str(i.get_c_id()) + str(i.get_mark()) + "|||||||||||||||||||")
            pass


# -------------------Func3Frame-----------------------
class Func4Frame(tk.Frame):
    def __init__(self, container, attr_root):
        super(Func4Frame, self).__init__(container)
        # || 0-0
        button_back = tk.Button(self, text='<-', command=lambda: [attr_root.show_frame(MenuFrame)])
        button_back.grid(row=0, column=0, sticky="NW")
        # title label || 0-1
        lable_title = tk.Label(self, text="This is list of Student: ")
        lable_title.grid(row=0, column=1, sticky="W")
        # update button for updating st list
        self.button_update = tk.Button(self, text="Update", command=lambda: [self.update_st_list()])
        self.button_update.grid(row=1, column=1)

    def update_st_list(self):
        length = len(Db.st_list)
        for i in range(0, length):
            text = "Id: " + Db.st_list[i].get_st_id() + "|| Name: " + Db.st_list[i].get_st_name() \
                   + "|| Dob: " + Db.st_list[i].get_st_dob()
            lable_st_inf = tk.Label(self, text=text)
            lable_st_inf.grid(row=1 + i, column=1, sticky="w")
        self.button_update.grid(row=length + 1,column=1)


# -------------------Func3Frame-----------------------
class Func5Frame(tk.Frame):
    def __init__(self, container, attr_root):
        super(Func5Frame, self).__init__(container)
        #
        button_back = tk.Button(self, text='<-', command=lambda: [attr_root.show_frame(MenuFrame)])
        button_back.grid(row=0, column=0, sticky="NW")
        # title label || 0-1
        lable_title = tk.Label(self, text="This is list of Course: ")
        lable_title.grid(row=0, column=1, sticky="W")
        # update button for updating st list
        self.button_update = tk.Button(self, text="Update", command=lambda: [self.update_cour_list()])
        self.button_update.grid(row=1, column=1)

    def update_cour_list(self):
        length = len(Db.course_list)
        for i in range(0, length):
            text = "Id: " + Db.course_list[i].get_id() + "|| Name: " + Db.course_list[i].get_name()
            lable_cr_inf = tk.Label(self, text=text)
            lable_cr_inf.grid(row=1 + i, column=1, sticky="w")
        self.button_update.grid(row=length + 1, column=1)


# -------------------Func3Frame-----------------------
class Func6Frame(tk.Frame):
    def __init__(self, container, att_root):
        super(Func6Frame, self).__init__(container)
        #
        button_back = tk.Button(self, text='<-', command=lambda: [att_root.show_frame(MenuFrame)])
        button_back.grid(row=0, column=0, sticky="NW")
        # title label || 0-1
        lable_title = tk.Label(self, text="This is list of Student with Mark: ")
        lable_title.grid(row=0, column=1, sticky="W")
        # update button for updating st list
        self.button_update = tk.Button(self, text="Update", command=lambda: [self.update_smm_list()])
        self.button_update.grid(row=1, column=1)

    def update_smm_list(self):
        length = len(Db.marks_list)
        for i in range(0, length):
            text = "Id student: " + Db.marks_list[i].get_s_id() + "|| Id course: " + Db.marks_list[i].get_c_id()\
            + "|| Mark: " + Db.marks_list[i].get_mark()
            lable_smm_inf = tk.Label(self, text=text)
            lable_smm_inf.grid(row=1 + i, column=1, sticky="w")
        self.button_update.grid(row=length + 1, column=1)


# -------------------Func3Frame-----------------------
class Func7Frame(tk.Frame):
    pass


# -------------------Func3Frame-----------------------
class Func8Frame(tk.Frame):
    pass


# -------------------Func3Frame-----------------------
class FuncQuit(tk.Frame):
    pass


if __name__ == '__main__':
    root = Root()
    root.mainloop()
