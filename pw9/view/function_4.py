from tkinter.ttk import *

# import pw9.control.controller as controller
# import pw9.model.old_db.data_base as db
import pw9.model.database as db_sql


class Function4(Frame):
    def __init__(self, container, attr_root):
        super(Function4, self).__init__(container)
        # button for enter and back
        self.button_back_call(attr_root)
        # label status 0-0
        self.label_status = Label(self, text="Students Information List")
        self.label_status.grid(row=0, column=0, padx=5, pady=5, columnspan=4, sticky="NS")
        # button for sorting list
        self.button_sort_call()
        # calling
        self.show_inf()
        # column config
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def button_sort_call(self):
        self.button_id = Button(self, text="Student ID  ↑", command=lambda: self.command_bt_id_up())
        self.button_id.grid(row=1, column=0, padx=5, pady=5)
        #
        self.button_name = Button(self, text="Student Name  ↑", command=lambda: self.command_bt_name_up())
        self.button_name.grid(row=1, column=1, padx=5, pady=5)
        #
        self.button_dob = Button(self, text="Student DoB  ↑", command=lambda: self.command_bt_dob_up())
        self.button_dob.grid(row=1, column=2, padx=5, pady=5)
        #
        self.button_gpa = Button(self, text="Student GPA  ↑", command=lambda: self.command_bt_gpa_up())
        self.button_gpa.grid(row=1, column=3, padx=5, pady=5)

    def command_bt_gpa_up(self):
        db_sql.sort_st_list_by_gpa_up()
        self.destroy_inf()
        self.show_inf()
        self.button_gpa.config(text="Student GPA  ↓",
                               command=lambda: [db_sql.sort_st_list_by_gpa_down(), self.command_bt_gpa_down()])
        pass

    def command_bt_gpa_down(self):
        db_sql.sort_st_list_by_gpa_down()
        self.destroy_inf()
        self.show_inf()
        self.button_gpa.config(text="Student GPA  ↑",
                               command=lambda: [db_sql.sort_st_list_by_gpa_up(), self.command_bt_gpa_up()])
        pass

    def command_bt_dob_up(self):
        db_sql.sort_st_list_by_dob_up()
        self.destroy_inf()
        self.show_inf()
        self.button_dob.config(text="Student DoB  ↓",
                               command=lambda: [db_sql.sort_st_list_by_dob_down(), self.command_bt_dob_down()])
        pass

    def command_bt_dob_down(self):
        db_sql.sort_st_list_by_dob_down()
        self.destroy_inf()
        self.show_inf()
        self.button_dob.config(text="Student DoB  ↑",
                               command=lambda: [db_sql.sort_st_list_by_dob_up(), self.command_bt_dob_up()])
        pass

    def command_bt_name_up(self):
        db_sql.sort_st_list_by_name_up()
        self.destroy_inf()
        self.show_inf()
        self.button_name.config(text="Student Name  ↓",
                                command=lambda: [db_sql.sort_st_list_by_name_down(), self.command_bt_name_down()])
        pass

    def command_bt_name_down(self):
        db_sql.sort_st_list_by_name_down()
        self.destroy_inf()
        self.show_inf()
        self.button_name.config(text="Student Name  ↑",
                                command=lambda: [db_sql.sort_st_list_by_name_up(), self.command_bt_name_up()])
        pass

    def command_bt_id_up(self):
        db_sql.sort_st_list_by_id_up()
        self.destroy_inf()
        self.show_inf()
        self.button_id.config(text="Student ID  ↓",
                              command=lambda: [db_sql.sort_st_list_by_id_down(), self.command_bt_id_down()])

    def command_bt_id_down(self):
        db_sql.sort_st_list_by_id_down()
        self.destroy_inf()
        self.show_inf()
        self.button_id.config(text="Student ID  ↑",
                              command=lambda: [db_sql.sort_st_list_by_id_up(), self.command_bt_id_up()])

    def command_bt_name(self):
        self.button_name.config(text="Student Name  ↓")
        self.show_inf()

    def command_bt_dob(self):
        self.button_dob.config(text="Student DoB  ↓")
        self.show_inf()

    def button_back_call(self, root_attr):
        self.button_back = Button(self, text="<-",
                                  command=lambda: self.command_button_back(root_attr))
        self.button_back.grid(row=0, column=0, padx=5, pady=5, sticky="W")

    def command_button_back(self, root_attr):
        Function4.destroy(self)
        root_attr.show_frame(root_attr.MenuFrame)

    # def show_inf(self):
    #     row = 2
    #     element = 0
    #     #
    #     self.label_id_list = []
    #     self.label_name_list = []
    #     self.label_dob_list = []
    #     self.label_gpa_list = []
    #     for student in db.st_list:
    #         s_id = student.get_st_id()
    #         s_name = student.get_st_name()
    #         s_dob = student.get_st_dob()
    #         s_gpa = student.get_st_gpa()
    #         #
    #         self.label_id_list.append(Label(self, text=s_id))
    #         self.label_id_list[element].grid(row=row, column=0, pady=2)
    #         #
    #         self.label_name_list.append(Label(self, text=s_name))
    #         self.label_name_list[element].grid(row=row, column=1, pady=2)
    #         #
    #         self.label_dob_list.append(Label(self, text=s_dob))
    #         self.label_dob_list[element].grid(row=row, column=2, pady=2)
    #         #
    #         self.label_gpa_list.append(Label(self, text=s_gpa))
    #         self.label_gpa_list[element].grid(row=row, column=3, pady=2)
    #         #
    #         element += 1
    #         row += 1

    def show_inf(self):
        row = 2
        element = 0
        #
        self.label_id_list = []
        self.label_name_list = []
        self.label_dob_list = []
        self.label_gpa_list = []
        for i in db_sql.get_all_sts_inf():
            s_id = i[0]
            s_name = i[1]
            s_dob = i[2]
            s_gpa = i[3]
            #
            self.label_id_list.append(Label(self, text=s_id))
            self.label_id_list[element].grid(row=row, column=0, pady=2)
            #
            self.label_name_list.append(Label(self, text=s_name))
            self.label_name_list[element].grid(row=row, column=1, pady=2)
            #
            self.label_dob_list.append(Label(self, text=s_dob))
            self.label_dob_list[element].grid(row=row, column=2, pady=2)
            #
            self.label_gpa_list.append(Label(self, text=s_gpa))
            self.label_gpa_list[element].grid(row=row, column=3, pady=2)
            #
            element += 1
            row += 1

    def destroy_inf(self):
        for i in self.label_id_list:
            i.destroy()
        #
        for i in self.label_name_list:
            i.destroy()
        #
        for i in self.label_dob_list:
            i.destroy()
        #
        for i in self.label_gpa_list:
            i.destroy()
