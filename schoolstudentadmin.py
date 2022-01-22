#Data class
class Data(db.Model):
    #Information about Data
    __tablename__="student"
    eno=db.Column(db.String(120),primary_key=True, unique=True)
    passw=db.Column(db.String(120))
    Name=db.Column(db.String(120))
    classs=db.Column(db.String(120))
    ContactNo=db.Column(db.String(120))
    Address=db.Column(db.String(120))
    Emailid=db.Column(db.String(120))
    result=db.Column(db.String(120))
    fees=db.Column(db.String(120))
    gives = db.relationship('Data3', secondary='sqrel', lazy='dynamic',
                            backref=db.backref('takenby', lazy='dynamic'))
  
    def __init__(self, eno, passw,Name,classs,Contactno,Add,ema,res,fees):
        #Person has a eno
        self.eno=eno
        #Person has a passw
        self.passw=passw
        #Person has a name 
        self.Name=Name
        #Person has a classs
        self.classs=classs
        #Person has a contactNo
        self.ContactNo=Contactno  
        #Person has a add
        self.Address=Add
        #Person has a ema
        self.Emailid=ema
        #Person has a res
        self.result=res
        #Person has a dees
        self.fees =fees


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

