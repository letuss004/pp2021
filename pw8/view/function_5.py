from tkinter.ttk import *

import pw8.control.controller as controller
import pw8.model.data_base as db


class Function5(Frame):
    def __init__(self, container, attr_root):
        super(Function5, self).__init__(container)
        #
        self.button_back_call(attr_root)
        # label status 0-1
        self.label_status = Label(self, text="Courses Information List")
        self.label_status.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="NS")
        # label for showing information
        self.button_sort_call()
        # calling
        self.show_inf()
        # column config
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def button_sort_call(self):
        self.button_id = Button(self, text="Courses ID  ↑", command=lambda: self.command_bt_id_up())
        self.button_id.grid(row=1, column=0, padx=5, pady=5)
        self.button_name = Button(self, text="Courses Name  ↑", command=lambda: [self.command_bt_name_up()])
        self.button_name.grid(row=1, column=1, padx=5, pady=5)

    def command_bt_id_up(self):
        controller.sort_cour_list_by_id_up()
        self.destroy_inf()
        self.show_inf()
        self.button_id.config(text="Courses ID  ↓",
                              command=lambda: [controller.sort_cour_list_by_id_down(), self.command_bt_id_down()])
        pass

    def command_bt_id_down(self):
        controller.sort_cour_list_by_id_down()
        self.destroy_inf()
        self.show_inf()
        self.button_id.config(text="Courses ID  ↑",
                              command=lambda: [controller.sort_cour_list_by_id_up(), self.command_bt_id_up()])
        pass

    def command_bt_name_up(self):
        controller.sort_cour_list_by_name_up()
        self.destroy_inf()
        self.show_inf()
        self.button_name.config(text="Courses Name  ↓",
                              command=lambda: [controller.sort_cour_list_by_name_down(), self.command_bt_name_down()])
        pass

    def command_bt_name_down(self):
        controller.sort_cour_list_by_name_down()
        self.destroy_inf()
        self.show_inf()
        self.button_name.config(text="Courses Name  ↑",
                              command=lambda: [controller.sort_cour_list_by_name_up(), self.command_bt_name_up()])
        pass

    def button_back_call(self, root_attr):
        self.button_back = Button(self, text="<-",
                                  command=lambda: self.command_button_back(root_attr))
        self.button_back.grid(row=0, column=0, padx=5, pady=5, sticky="W")

    def command_button_back(self, root_attr):
        Function5.destroy(self)
        root_attr.show_frame(root_attr.MenuFrame)

    def show_inf(self):
        row = 2
        element = 0
        #
        self.label_id_list = []
        self.label_name_list = []
        #
        for student in db.course_list:
            #
            c_id = student.get_id()
            c_name = student.get_name()
            #
            self.label_id_list.append(Label(self, text=c_id))
            self.label_id_list[element].grid(row=row, column=0, pady=2)
            #
            self.label_name_list.append(Label(self, text=c_name))
            self.label_name_list[element].grid(row=row, column=1, pady=2)
            #
            row += 1
            element += 1
        pass

    def destroy_inf(self):
        for i in self.label_id_list:
            i.destroy()
        #
        for i in self.label_name_list:
            i.destroy()
        pass
