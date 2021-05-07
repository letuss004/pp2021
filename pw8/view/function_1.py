from tkinter.ttk import *

# from tkinter import *
import PythonStore.GUI.ControllerStore as Cs
import pw8.control.controller as controller
import pw8.model.data_base as db


class Function1(Frame):
    def __init__(self, container, attr_root):
        super(Function1, self).__init__(container)
        #
        self.label_status = Label(self, text="Setting Student Information Function")
        self.label_status.grid(row=0, column=1, padx=5, pady=5, sticky="NS")
        # entry
        self.et_s_id_call()
        self.et_s_name_call()
        self.et_s_dob_call()
        #
        lb_empty = Label(self, text="             ")
        lb_empty.grid(row=0, column=2, padx=5, pady=5)
        # button
        self.button_enter_call()
        self.button_back_call(attr_root)
        #
        lb_empty = Label(self, text="             ")
        lb_empty.grid(row=0, column=2, padx=5, pady=5)
        self.grid_columnconfigure(1, weight=1)

    def command_button_enter(self):
        # check variable for checking name, dob, id
        check1, check2, check3 = False, False, False
        # name checking
        check1 = Cs.input_a_s_controller(self.et_st_name.get(), self.label_s_name_ano, "Name")
        # id checking
        if Cs.input_identifier(self.et_st_id.get(), self.label_sid_ano) and not \
                controller.check_s_id(self.et_st_id.get()):
            check2 = True
        elif controller.check_s_id(self.et_st_id.get()):
            self.label_sid_ano.config(text="This ID is already exist")
        # dob checking
        check3 = Cs.input_dob(self.et_st_dob.get(), self.label_s_dob_ano)
        # if all true => save on database
        if check1 and check2 and check3:
            db.st_list.append(db.Student(self.et_st_name.get(), self.et_st_id.get(), self.et_st_dob.get()))
            self.label_s_dob_ano.config(text="Information is added successful")

    def command_button_back(self, root_attr):
        Function1.destroy(self)
        root_attr.show_frame(root_attr.MenuFrame)

    def button_back_call(self, root_attr):
        self.button_back = Button(self, text="<-",
                                  command=lambda: self.command_button_back(root_attr))
        self.button_back.grid(row=0, column=0, padx=5, pady=5)

    def button_enter_call(self):
        self.button_enter = Button(self, text="Enter", command=lambda: self.command_button_enter())
        self.button_enter.grid(row=7, column=1, padx=5, pady=5)

    def et_s_id_call(self):
        self.et_st_id = Entry(self)
        self.et_st_id.insert(-1, "ID")
        self.et_st_id.grid(row=1, column=1, padx=5, pady=5)
        self.et_st_id.grid_columnconfigure(1, weight=1)
        #
        self.label_sid_ano = Label(self)
        self.label_sid_ano.grid(row=2, column=1)

    def et_s_name_call(self):
        self.et_st_name = Entry(self)
        self.et_st_name.insert(-1, "Name")
        self.et_st_name.grid(row=3, column=1, padx=5, pady=5)
        self.et_st_name.grid_columnconfigure(1, weight=1)
        #
        self.label_s_name_ano = Label(self)
        self.label_s_name_ano.grid(row=4, column=1)

    def et_s_dob_call(self):
        self.et_st_dob = Entry(self)
        self.et_st_dob.insert(-1, "DoB ")
        self.et_st_dob.grid(row=5, column=1, padx=5, pady=5)
        self.et_st_dob.grid_columnconfigure(1, weight=1)
        #
        self.label_s_dob_ano = Label(self, text="")
        self.label_s_dob_ano.grid(row=6, column=1)
