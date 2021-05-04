from tkinter.ttk import *
from ttkthemes import *
# from tkinter import *
from pw6.view.function_1 import Function1
from pw6.view.function_2 import Function2
from pw6.view.function_3 import Function3
from pw6.view.function_4 import Function4
from pw6.view.function_5 import Function5




class MenuFrame(Frame):
    def __init__(self, container, attr_root):
        super(MenuFrame, self).__init__(container)
        #
        lb_start = Label(self, text="Select the functionality by click buttons")
        lb_start.grid(row=0, column=0, pady=10)
        # Button for setting student inf
        bt_function1 = Button(self, text="Set Students Information", width=30,
                              command=lambda: [attr_root.show_frame(Function1), self.destroy()])
        bt_function1.grid(row=1, column=0, pady=10)
        #
        bt_function2 = Button(self, text="Set Courses Information", width=30,
                              command=lambda: [attr_root.show_frame(Function2), self.destroy()])
        bt_function2.grid(row=2, column=0, pady=10)
        #
        bt_function3 = Button(self, text="Set Mark For Student", width=30,
                              command=lambda: [attr_root.show_frame(Function3), self.destroy()])
        bt_function3.grid(row=3, column=0, pady=10)
        #
        bt_function4 = Button(self, text="Get Students Information", width=30,
                              command=lambda: [attr_root.show_frame(Function4), self.destroy()])
        bt_function4.grid(row=4, column=0, pady=10)
        #
        bt_function5 = Button(self, text="Get Courses Information", width=30,
                              command=lambda: [attr_root.show_frame(Function5), self.destroy()])
        bt_function5.grid(row=5, column=0, pady=10)
        #
        # bt_function6 = Button(self, text="Get Courses Information", width=30,
        #                       command=lambda: [attr_root.show_frame(Function6), self.destroy()])
        # bt_function6.grid(row=6, column=0, pady=10)
        # #
        # bt_function7 = Button(self, text="Get Courses Information", width=30,
        #                       command=lambda: [attr_root.show_frame(Function7), self.destroy()])
        # bt_function7.grid(row=7, column=0, pady=10)

        self.grid_columnconfigure(0, weight=1)
