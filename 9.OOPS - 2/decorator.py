# ----- cls decorator ---------
class Person:
    name = "Sanket"
    @classmethod
    def changeName(cls, name):
        cls.name = name
# Creating an instance of the Person class
p1 = Person()
# Changing the name using the class method
p1.changeName("rahul kumar")
# Printing the name attribute
print(p1.name)       # This will print "rahul kumar"
print(Person.name)   #changing attributes in class 
#This will also print "rahul kumar"


# ----- property decorator ---------
class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3 ) + "%"

stu1=Student(98,97,99)
print(stu1.percentage)

stu1.phy = 10   #changing physics marks
print(stu1.percentage)   # automatic change in percentage


