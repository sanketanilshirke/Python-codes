# 1. Method overloading
 
class A:
    def product(self, a, b):  
     print(a * b)
# we need to create new class with same name of function
class B:
    def product(self, a, b, c): 
      print(a * b * c)
a=A()
a.product(2,2)
b=B()
b.product(2,2,2)




# 2. Method Overriding
class Parent:
    Name="Sanket"
    def show(self): 
     print(self.Name)

class Child(Parent):
    Name="Sanket Shirke"
    def show(self):
     print(self.Name)
c=Child()
c.show()


class Parent():     
    def show(self):  
        print("Vishal")         
class Child(Parent):       
    def show(self):          
        print("bhau")          
p = Parent()  
c = Child()  
p.show()  
c.show()  


class Parent:     
    def show(self):  
        print("Vishal Shirke")         
class Child(Parent):       
   pass         
c = Child()  
c.show()

