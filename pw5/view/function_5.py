from tkinter.ttk import *
from pw5.model.data_base import *


class Function5(Frame):
    def __init__(self, container, attr_root):
        super(Function5, self).__init__(container)
        #
        self.button_back_call(attr_root)
        # label status 0-1
        self.label_status = Label(self, text="Courses Information List")
        self.label_status.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="NS")
        # label for showing information
        self.label_Id = Label(self, text="Courses ID").grid(row=1, column=0, padx=5, pady=5)
        self.label_Name = Label(self, text="Courses Name").grid(row=1, column=1, padx=5, pady=5)
        # calling
        self.show_inf()
        # column config
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


    def button_back_call(self, root_attr):
        self.button_back = Button(self, text="<-",
                                  command=lambda: self.command_button_back(root_attr))
        self.button_back.grid(row=0, column=0, padx=5, pady=5, sticky="W")

    def command_button_back(self, root_attr):
        Function5.destroy(self)
        root_attr.show_frame(root_attr.MenuFrame)

    def show_inf(self):
        row = 2
        for student in course_list:
            #
            c_id = student.get_id()
            c_name = student.get_name()
            #
            label_id = Label(self, text=c_id)
            label_id.grid(row=row, column=0, pady=2)
            #
            label_name = Label(self, text=c_name)
            label_name.grid(row=row, column=1, pady=2)
            #
            row += 1
        pass
