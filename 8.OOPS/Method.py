class Student:
    def __init__(self, fullname):   # constructor
        print(fullname)
    
    def m1(self,xyz):                #method
        print("m1 method")
        print(xyz)

     
s1 = Student("ram")  # instance / object
s1.m1("abc")