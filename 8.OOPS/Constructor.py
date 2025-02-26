# Program 1
class Student:
   def __init__(self,fullname):   #constructor
      self.name=fullname
      print("adding new student in Database..")
s1=Student("ram")           #instance / object
print(s1.name)

s2=Student("sita")           #instance / object
print(s2.name)



# Program 2
class Car:
    #Default Constructor
    def __init__(self): 
      pass
    
    # Parameterized Constructor
    def __init__(self,name,fullname):
      self.name=name
      self.fullname=fullname
c=Car("BMW","Mercedes")        
print(c.name)
print(c.fullname)



# Program 3
class Chotabheem:
    #Default Constructor
    def __init__(self): 
      print("Chin tapak dam dam")
c=Chotabheem()        

 