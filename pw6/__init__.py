"""
Version:
    - 2.1.4
What's new:
    - Using pickle for
    - Sorting list by name, id, gpa,...
    - Sorting student dob is quite bad (fix in next version)
    - Add README.md
Feature:
    - Extract pw4 into MVC model. Split class, file into correct packages
    - Arc theme
    - IO redirection
    - Compress file before close program
    - Delete file after compress
    - No Error (I tried)
    - Extract file for get information
    - Override mark if sid and cid is overlap
    - Documentation and comments are available
    - Adding student information with function to constraint input domain
    - Adding course information with function to constraint input domain
    - Adding mark for course and student with function to constraint input domain
    - Show student information
    - Show course information
    - Show mark information
"""
from pw6.view.root import Root
import pw6.model.file as file
import pw6.control.controller as controller

if __name__ == '__main__':
    #
    controller.extract_data()
    file.read_data_by_pickle()
    #
    root = Root()
    root.mainloop()
    #
    file.write_data_by_pickle()
    controller.compress_data()
