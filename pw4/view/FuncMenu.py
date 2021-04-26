from Root import *
import tkinter as tk

class MenuFrame(tk.Frame):
    def __init__(self, container, attr_main):
        super(MenuFrame, self).__init__(container)

        lb1 = tk.Label(self, text="Select the functionality by click buttons")
        lb1.grid(padx=5, pady=5)

        bt1 = tk.Button(self, text="Set information for all student in class",
                        command=lambda: attr_main.show_frame(Func1Frame))
        bt1.grid(padx=5, pady=5)

        bt2 = tk.Button(self, text="Set information for course",
                        command=lambda: attr_main.show_frame(Func2Frame))
        bt2.grid(padx=5, pady=5)

        bt3 = tk.Button(self, text="hello")
        bt3.grid(padx=5, pady=5)
