# --- Python Mini Project - Library Management System -----
# Create list_of_books.txt file 
# List of books :

import datetime
import os
os.getcwd()
#LMS class
class LMS:
    #Information about LMS
    """
    This class is used to keep records of books library.
    It has total four modules: 'Display Books', 'Lend Books', 'Add Books', 'Return Books'
    'list_of_books' should be txt file. 'library_name' should be string.
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        with open(self.list_of_books) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(id):{'books_title':line.replace("\n",""),'lender_name':'','lend_date':'', 'status':'Available'}})
            id += 1    

    def display_books(self):
        print("------------------------List of Books---------------------")
        print("Books ID","\t", "Title")
        print("----------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t", value.get("books_title"), "- [", value.get("status"),"]")

    def Issue_books(self):
        books_id = input("Enter Books ID : ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['status'] == 'Available':
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['lend_date']}")
                return self.lend_books()
            elif self.books_dict[books_id]['status'] == 'Available':
                your_name = input("Enter Your Name : ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['lend_date'] = current_date
                self.books_dict[books_id]['status']= 'Already Issued'
                print("Book Issued Successfully !!!\n")
        else:
            print("Book ID Not Found !!!")
            return self.Issue_books()

    def add_books(self):
        new_books = input("Enter Books Title : ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 20:
            print("Books title length is too long !!! Title length limit is 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as b:
                b.writelines(f"{new_books}\n")
            self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':'','lend_date':'', 'status':'Available'}})
            print(f"The books '{new_books}' has been added successfully !!!")

    def return_books(self):
        books_id = input("Enter Books ID : ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.return_books()
            elif not self.books_dict[books_id]['status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['lend_date'] = ''
                self.books_dict[books_id]['status']= 'Available'
                print("Successfully Updated !!!\n")
        else:
            print("Book ID Not Found !!!")

if __name__ == "__main__":
    try:
        mylms = LMS("list_of_books.txt", "Python's")
        press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}    
        
        key_press = False
        while not (key_press == "q"):
            print(f"\n----------Welcome To {mylms.library_name}'s Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "i":
                print("\nCurrent Selection : ISSUE BOOK\n")
                mylms.Issue_books()
                
            elif key_press == "a":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.add_books()

            elif key_press == "d":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                mylms.display_books()
            
            elif key_press == "r":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.return_books()
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong. Please check. !!!")

import sys
def Notebook():
    pass
class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
                "1": self.show_notes,
                "2": self.search_notes,
                "3": self.add_note,
                "4": self.modify_note,
                "5": self.quit
                }
    def display_menu(self):
        print("""
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
""")
    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))
    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")
    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)
    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)
if __name__ == "__main__":
    Menu().run()

