from tkinter.ttk import *
from pw5.model.data_base import *
import pw5.controller.controller as controller


class Function4(Frame):
    def __init__(self, container, attr_root):
        super(Function4, self).__init__(container)
        # button for enter and back
        self.button_back_call(attr_root)
        # label status 0-0
        self.label_status = Label(self, text="Students Information List")
        self.label_status.grid(row=0, column=0, padx=5, pady=5, columnspan=4, sticky="NS")
        # label for showing information
        self.label_Id = Label(self, text="Student ID").grid(row=1, column=0, padx=5, pady=5)
        self.label_Name = Label(self, text="Student Name").grid(row=1, column=1, padx=5, pady=5)
        self.label_DoB = Label(self, text="Student DoB").grid(row=1, column=2, padx=5, pady=5)
        self.label_GPA = Label(self, text="Student GPA").grid(row=1, column=3, padx=5, pady=5)
        # calling
        self.show_inf()
        # column config
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def button_back_call(self, root_attr):
        self.button_back = Button(self, text="<-",
                                  command=lambda: self.command_button_back(root_attr))
        self.button_back.grid(row=0, column=0, padx=5, pady=5, sticky="W")

    def command_button_back(self, root_attr):
        Function4.destroy(self)
        root_attr.show_frame(root_attr.MenuFrame)

    def show_inf(self):
        row = 2
        for student in st_list:
            #
            s_id = student.get_st_id()
            s_name = student.get_st_name()
            s_dob = student.get_st_dob()
            s_gpa = controller.get_st_gpa(s_id)
            #
            label_id = Label(self, text=s_id)
            label_id.grid(row=row, column=0, pady=2)
            #
            label_name = Label(self, text=s_name)
            label_name.grid(row=row, column=1, pady=2)
            #
            label_dob = Label(self, text=s_dob)
            label_dob.grid(row=row, column=2, pady=2)
            #
            if type(s_gpa) != type(False):
                label_gpa = Label(self, text=s_gpa)
                label_gpa.grid(row=row, column=3, pady=2)
            #
            row += 1
        pass
