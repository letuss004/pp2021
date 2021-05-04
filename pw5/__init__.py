"""
Version:
    - 2.1.3
What's new:
    - Run by __init__
    - Extract pw4 into MVC model
    - Split class, file into correct packages
    - Arc theme
    - IO redirection
    - Compress file before close program
    - Delete after compress
    - No Error (I tried)
    - Extract file for get information
    - Override mark if sid and cid is overlap
    - Documentation is available
Feature:
    - Adding student information with function to constraint input domain
    - Adding course information with function to constraint input domain
    - Adding mark for course and student with function to constraint input domain
    - Show student information
    - Show course information
    - Show mark information
    - Comments
"""
from pw5.view.root import *
import pw5.model.file as file
from pw5.model.data_base import *

if __name__ == '__main__':
    #
    file.extract_data()
    file.read_data_from_file()
    #
    root = Root()
    root.mainloop()
    #
    file.write_data_to_file()
    file.compress_data()