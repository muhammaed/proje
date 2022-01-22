#employee class
from typing import AsyncGenerator


class employee(object):
    #information about employee
    #attribute = age, name, addres
    #behaviour = pass
    #String = her hanse bir sayi tamamladir meselen her hansi iscinin yasi = age=30 
    #interger = her hansi bir iscinin adi adresi ve s gosterir qosa dirnaql yazilir = football_club = "barcelona"
    pass
employee1 = employee()
####atributes

#Footballer class
class footballer:
    #information about footballer
    age=30
    footbal_club= "barcelona"
# f1 ucun butun fottballer ozelliyini dasidiq
f1 = footballer()

#print bununla yazilanlari cap edirik

print(f1)
print(f1.age)
print(f1.footbal_club)

#print futbolcunu real-madrid klubuna transfer edek

f1.footbal_club = "real-madrid"
print(f1.footbal_club)


######Method

#Square class
class square(object):
    #informtion about square
    edge = 5
    def area(self): # Definition method = self bir varablies deyerlendirme heyata kecirir
        area = self.edge * self.edge # 5*5
        print("Area: ", area)
        ######
s1 = square()   

print(s1)
print(s1.edge)
print(s1.area())


#EMP class
class EMP(object):
    #informtion about EMP
    age = 30   
    salary = 1000

    def ageSlaryRatio(self):
        print(self.age / self.salary)


s1 = EMP() 
s1.ageSlaryRatio()

#animal class
class animal(object):
    #informtion about animal
   age = 3   #stringer
   name = "dog"  #interger

def __init__(self, name, age):
    self.name= name
    self.age= age

def getAge(self):
    return self.age

def getName(self):
    print(self.name)


A1 = animal("dog", 2)
A2 = animal("cat", 3)
A3 = animal("bird", 5)



#Parents

#Animal class
class animal(object):
    def __init__(self, name, age):
        print("Animal creade:")
        self.name= name
        self.age= age

    def toString(self):
        print("Animal jump:")

    def  wolk(self):
        print("animal wolk:")    


#child

#Monkey class child

class monkey(animal):
    def __init__(self):
        super().__init__() # Valideyn olan yerden cagirdim monkey ucun
        print("Monkey is created")

    def toString(self):
        print("monkey")

    def climb(self):
        print("Monkey can climb") 



#Parents

#people class
class people(object):
    #information about people
    def __init__(self):
        print("People is created")

    def toLife(self) :
        print("People is life")   


    def wolk(self):
        print("people is wolk")


#child
# Child class
class mahammad(people):

    def __init__(self):
        super(). __init__()
        print("mahammad is person")

    def toLife(self):
        print("mahammad is life") 


    def hacker(self):
        print("mahammad is hacker")

class aqil(people):

    def __init__(self):
        super(). __init__()
        print("Aqil is person")

    def toLife(self):
        print("Aqil is life")


    def programning(self):
        print("Aqil is developer")


m1 =mahammad()
m1.toLife()
m1.wolk()
m1.hacker()

print("-----")

a1 = aqil()
a1.toLife()
a1.wolk()
a1.programning()


#parents
class website(object):
    def __init__(self, name, surname):
        self.name= name
        self.surname= surname

    def login(self):
        print(self.name + "" + self.surname)


#child
class website1(website):
    def __init__ (self, name, surname, id):
        website. __init__(self, name, surname)
        self.id = id
    def loginsystem(self):
        print(self.name + "" + self.surname +""+ self.id)


class website2(website):
    def __init__(self, name, surname, email):
        website. __init__(self, name, surname)
        self.email= email

    def umpersystems(self):
        print(self.name + "" + self.surname + "" + self.email)


p1 = website1("surname", "name", "234")        
p2 = website2("surname", "name", "mahammad.kamilov@khazar.org")


class mother(object):
    def __init__():
        print('matanat is person')
    
    def getname(self):
       print('matanat')


    def getsurname(self):
       print('kamilova')

    def getemail(self):
        print('@maili.com')

    def getwalk(self):
        print('people is walk')


class mahammad(mother):
    def __init__():
        super(). __init__()
        print('mahammad is person')

    
    def getname(self):
       print('mahammad')


    def getsurname(self):
       print('kamilov')

    def getemail(self):
        print('@mail.com')    

    def gethacker(self):
       print('mahammad is hacker')




mo = mother()   
mo.getname()
mo.getsurname()
mo.getemail()

print('----------')

ma = mahammad()
ma.getname()
ma.getsurname()
ma.getemail()
ma.hacker()
ma.getwalk()



class penguin(object):
    def swim(self):
        print('penguin can swim')

    def fly(self):
        print('penguin cannot fly')



class parrot(object):
    def swim(self):
        print('penguin cannot swim')

    def fly(self):
        print('penguin can fly')        

#POLYPHORMISM
def fly_test(bird):
      bird_fly


pe = penguin()
pe.swim()
pe.fly()
pa = parrot()
pa.swim()
pa.fly()


#POLYPHORMISM
fly_test(pa)
fly_test(pe)

