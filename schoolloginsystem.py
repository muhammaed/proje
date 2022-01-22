 #loginsystem class
class ScoolLoginSystem:
    #Information about loginsystem

        def __init__(self):
            self.user_id = input("Please enter your user id: ")
            self.user_password = input("Please enter your password: ")

        def login(self):
            username = self.user_id
            password = self.user_password
            if len(username) <= 5 and len(password) <= 5:
                print("Logging In")
            else:
                print("Error! Max Length is 5 chars.") #return back to 
                login 

        def check_system(self):
            registered_user = {
             "test@gmail.com": "test"
            }
            if self.user_id in registered_user:
                print("Successful")
            else:
                new_user = input("Id not found! Are you are new user?\n [Y]es or [N]o\n")
                new_user = new_user.lower()
                if new_user == "Y":
                   return back 
                elif new_user == "N": #how to return back to main login system
                   new_username = input("Please enter your user id: ")
                   new_userpassword = input("Please enter your password: ")
                else:
                   return #back to login system


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

