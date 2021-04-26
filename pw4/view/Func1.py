from Root import *
import tkinter as tk


class Func1Frame(tk.Frame):
    def __init__(self, container, attr_main):
        super(Func1Frame, self).__init__(container)
        #
        lb1 = tk.Label(self, text="Input the correct information")
        lb1.grid(column=2, row=0, padx=25, pady=5)
        #
        self.entries_inf = []
        #
        etl1 = tk.Label(self, text="Name*", fg="red")
        etl1.grid(column=0, row=1, padx=10)
        self.et1 = tk.Entry(self, width=50)
        self.et1.grid(column=2, row=1, padx=10, pady=15)
        etl2 = tk.Label(self, text="", fg="red")
        etl2.grid(column=2, row=2, padx=10, pady=15)
        self.entries_inf.append(self.et1.get())
        #
        etl1 = tk.Label(self, text="ID*", fg="red")
        etl1.grid(column=0, row=2, padx=10)
        self.et2 = tk.Entry(self, width=50)
        self.et2.grid(column=2, row=2, padx=10, pady=15)
        self.entries_inf.append(self.et2.get())

        etl1 = tk.Label(self, text="DoB*", fg="red")
        etl1.grid(column=0, row=3, padx=10)
        self.et3 = tk.Entry(self, width=50)
        self.et3.grid(column=2, row=3, padx=10, pady=15)
        self.entries_inf.append(self.et3.get())

        bt1 = tk.Button(self, text="<-", command=lambda: attr_main.show_frame())
        bt1.grid(column=0, row=0, sticky="NW")

        bt2 = tk.Button(self, text="Enter")
        bt2.grid(column=2, row=4)


    # def check_entry
