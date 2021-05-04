from pw5.view.menu_frame import *


class Root(ThemedTk):
    def __init__(self):
        super(Root, self).__init__()
        # setting main windows and attribute
        self.geometry("450x450")
        self.title("Student Mark Management Version 2.1.3")
        self.MenuFrame = MenuFrame
        self.set_theme("arc")
        # create container
        self.container = Frame(self)
        self.container.pack(fill="both", expand=True)
        #
        self.show_frame(MenuFrame)

    def show_frame(self, frame_want_to_show):
        frame_showed = frame_want_to_show(self.container, self)
        frame_showed.pack(fill="both", expand=True)
        frame_showed.tkraise()
