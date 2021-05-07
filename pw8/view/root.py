from pw8.view.menu_frame import *
from ttkthemes import *
import pw8.model.file as file
import pw8.control.controller as controller
import threading
import time


class Root(ThemedTk):
    def __init__(self):
        super(Root, self).__init__()
        #
        self.extract()
        # setting main windows and attribute
        self.geometry("450x450")
        self.title("Student Mark Management Version 2.1.5")
        self.MenuFrame = MenuFrame
        self.set_theme("arc")
        # create container
        self.container = Frame(self)
        self.container.pack(fill="both", expand=True)
        #
        self.show_frame(MenuFrame)
        #
        thread = threading.Thread(target=self.pickle_background_thread)
        thread.daemon = True
        thread.start()

    def show_frame(self, frame_want_to_show):
        frame_showed = frame_want_to_show(self.container, self)
        frame_showed.pack(fill="both", expand=True)
        frame_showed.tkraise()

    def pickle_background_thread(self):
        while True:
            print("Database is updated !!!")
            file.write_data_by_pickle()
            controller.compress_data()
            time.sleep(1)

    def extract(self):
        print("Extracted")
        controller.extract_data()
        file.read_data_by_pickle()