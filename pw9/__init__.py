"""
Version:
    - 3.0.0
What's new:
    - Using mysql database
    - Sorting student dob is quite bad (fix in next version)
Feature:
    - Sorting list by name, id, gpa,....
    - Add README.md
    - Extract pw4 into MVC model. Split class, file into correct packages
    - Arc theme
    - IO redirection
    - Compress file before close program
    - Delete file after compress
    - No Error (I tried)
    - Extract file for get information

    - Override mark if sid and cid is overlap
    - Documentation and comments are available
    - Adding student, course, mark information with constraint input domain method
    - Show student, course, mark information
"""

from pw9.view.root import Root

if __name__ == '__main__':
    root = Root()
    root.mainloop()
