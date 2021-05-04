from tkinter.ttk import *
import PythonStore.GUI.ControllerStore as Cs
import pw5.controller.controller as controller
from pw5.model.data_base import *
from pw5.model.mark import Mark


class Function3(Frame):
    def __init__(self, container, attr_root):
        super(Function3, self).__init__(container)
        #
        label_status = Label(self, text="Enter Student ID Want To Manage")
        label_status.grid(row=0, column=1)
        #
        self.et_sid_call()
        #
        self.button_enter_call()
        self.button_back_call(attr_root)
        #
        lb_empty = Label(self, text="             ")
        lb_empty.grid(row=0, column=2, padx=5, pady=5)
        self.grid_columnconfigure(1, weight=1)

    def et_sid_call(self):
        self.et_st_id = Entry(self)
        self.et_st_id.insert(0, "ID")
        self.et_st_id.grid(row=1, column=1, padx=5, pady=5)
        self.et_st_id.grid_columnconfigure(1, weight=1)
        # label annotation
        self.label_sid_ano = Label(self)
        self.label_sid_ano.grid(row=2, column=1, pady=5)
        # placeholder label

    def button_back_call(self, root_attr):
        self.button_back = Button(self, text="<-",
                                  command=lambda: self.command_button_back(root_attr))
        self.button_back.grid(row=0, column=0, padx=5, pady=5)

    def command_button_back(self, root_attr):
        Function3.destroy(self)
        root_attr.show_frame(root_attr.MenuFrame)

    def button_enter_call(self):
        self.button_enter = Button(self, text="Enter Student ID", command=lambda: self.command_button_enter())
        self.button_enter.grid(row=4, column=1, padx=5, pady=5)

    def command_button_enter(self):
        #
        if controller.check_s_id(self.et_st_id.get()):
            self.combobox_and_mark()
            self.button_enter.destroy()
            self.button_enter_call_2()
        else:
            self.label_sid_ano.config(text="Student ID does not exist", foreground="red")

    def button_enter_call_2(self):
        self.button_enter_2 = Button(self, text="Enter Mark", command=lambda: self.command_button_enter_2())
        self.button_enter_2.grid(row=7, column=1, padx=5, pady=5)

    def command_button_enter_2(self):
        if controller.check_s_id(self.et_st_id.get()):
            self.store_mark_on_database()
        else:
            self.cbb_destroy()
            self.button_enter_2.destroy()
            self.label_sid_ano.config(text="Student ID does not exist", foreground="red")
            self.button_enter_call()

    def store_mark_on_database(self):
        sid = self.et_st_id.get()
        cid = controller.filter_cid_cbb(self.cbb.get())
        mark = self.et_mark_input.get()
        condition, index = controller.check_sid_cid_on_mark(sid, cid)
        if condition:
            if Cs.input_float_controller(mark, 0, 20, self.label_sid_ano):
                marks_list[index].set_mark(mark)
                self.label_sid_ano.config(text="Mark is overridden successful", foreground="red")
        else:
            if Cs.input_float_controller(mark, 0, 20, self.label_sid_ano):
                marks_list.append(Mark(cid, sid, mark))
                self.label_sid_ano.config(text="Mark is added successful", foreground="red")

    def cbb_destroy(self):
        self.cbb.destroy()
        self.label_cbb_ano.destroy()
        self.et_mark_input.destroy()

    def combobox_and_mark(self):
        # combo box
        id_name_cour_list = controller.get_id_name_cour_list()
        self.cbb = Combobox(self, value=id_name_cour_list, width=30, state="readonly")
        self.cbb.grid(row=4, column=1)
        # label cbb ano
        self.label_cbb_ano = Label(self, text="")
        self.label_cbb_ano.grid(row=5, column=1)
        # entry for mark
        self.et_mark_input = Entry(self, width=10)
        self.et_mark_input.insert(0, "Mark")
        self.et_mark_input.grid(row=4, column=2, padx=5)
        # set entry label ano
        self.label_sid_ano.config(text="Input Mark For Course On The Right")
        #
