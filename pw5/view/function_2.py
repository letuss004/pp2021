from tkinter.ttk import *
# from tkinter import *
import PythonStore.GUI.ControllerStore as Cs
import pw5.controller.controller as controller
import pw5.model.data_base as db


class Function2(Frame):
    def __init__(self, container, attr_root):
        super(Function2, self).__init__(container)
        #
        self.label_status = Label(self, text="Setting Course Information Function")
        self.label_status.grid(row=0, column=1, padx=5, pady=5, sticky="NS")
        self.et_c_id_call()
        self.et_c_name_call()
        # empty label for balance
        lb_empty = Label(self, text="             ")
        lb_empty.grid(row=0, column=2, padx=5, pady=5)
        # button
        self.button_enter_call()
        self.button_back_call(attr_root)
        #
        self.grid_columnconfigure(1, weight=1)

    def command_button_enter(self):
        # check variable for checking name, dob, id
        check1, check2 = False, False
        # name checking
        check1 = Cs.input_a_s_controller(self.et_cour_name.get(), self.label_s_name_ano, "Name")
        # id checking
        if Cs.input_identifier(self.et_cour_id.get(), self.label_sid_ano) and not \
                controller.check_c_id(self.et_cour_id.get()):
            check2 = True
        elif controller.check_c_id(self.et_cour_id.get()):
            self.label_sid_ano.config(text="This ID is already exist")
        # if all true => save on database
        if check1 and check2:
            db.course_list.append(db.Course(self.et_cour_name.get(), self.et_cour_id.get()))
            self.label_s_name_ano.config(text="Information is added successful")

    def command_button_back(self, root_attr):
        Function2.destroy(self)
        root_attr.show_frame(root_attr.MenuFrame)

    def button_back_call(self, root_attr):
        self.button_back = Button(self, text="<-",
                                  command=lambda: self.command_button_back(root_attr))
        self.button_back.grid(row=0, column=0, padx=5, pady=5)

    def button_enter_call(self):
        self.button_enter = Button(self, text="Enter", command=lambda: self.command_button_enter())
        self.button_enter.grid(row=5, column=1, padx=5, pady=5)

    def et_c_id_call(self):
        self.et_cour_id = Entry(self)
        self.et_cour_id.insert(-1, "ID")
        self.et_cour_id.grid(row=1, column=1, padx=5, pady=5)
        self.et_cour_id.grid_columnconfigure(1, weight=1)
        #
        self.label_sid_ano = Label(self)
        self.label_sid_ano.grid(row=2, column=1)

    def et_c_name_call(self):
        self.et_cour_name = Entry(self)
        self.et_cour_name.insert(-1, "Name")
        self.et_cour_name.grid(row=3, column=1, padx=5, pady=5)
        self.et_cour_name.grid_columnconfigure(1, weight=1)
        #
        self.label_s_name_ano = Label(self)
        self.label_s_name_ano.grid(row=4, column=1)
