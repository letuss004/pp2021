
from Func1 import *
from Func2 import *
from FuncMenu import *


class Root(tk.Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.geometry("400x400")
        self.title("Student Mark Management")

        container = tk.Frame(self)
        container.grid()

        self.frame_dic = {}

        for i in (MenuFrame, Func1Frame, Func2Frame):
            frame = i(container, self)
            self.frame_dic[i] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(MenuFrame)

    def show_frame(self, frame_input):
        frame_showed = self.frame_dic[frame_input]
        frame_showed.tkraise()
