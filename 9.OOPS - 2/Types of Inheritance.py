# 1 Single Inheritance
class Parent:
    def f1(self):
        print("parent class")
class Child(Parent):
    def f2(self):
        print("child class")
c=Child()
c.f1()
c.f2()

# 2 Multi-level Inheritance
class Grandpa:
    def f1(self):
        print("Grandpapa class")
class Father(Grandpa):
    def f2(self):    
        print("Father class")
class Son(Father):
    def f3(self):    
        print("Son class")
s=Son()
s.f1()
s.f2()
s.f3()

# 3 Multiple Inheritance
class Father:
    def f1(self):
        print("Father class")
class Mother:
    def f2(self):
        print("Mother class")
class Son(Father,Mother): 
    def f3(self):
        print("Son class")
s=Son()
s.f1()
s.f2()
s.f3()

# 4 Heirarchical Inheritance
class Animal:           
    def hash(self):
        print("animal class")
class Dog(Animal):
    def speak(self):
        print("dog class")
class Cat(Animal):
    def speak(self):
        print("cat class")
class Cow(Animal):
    def speak(self):
        print("cow class")
c = Cow()
c.speak()
c.hash()


# 5 Hybrid Inheritance
class School: 
    def f1(self):
        print("f1 in school")

class Student1(School):
    def f2(self):
        print("f2 in student 1")

class Student2(Student1):
    def f3(self):
        print("f3 in student 2")

class Student3(Student2, Student1):  # multiple inheritance
    def f4(self):
        print("f4 in student 3")

s = Student3()
s.f4()
s.f2()
s.f3()



