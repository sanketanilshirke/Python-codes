# 1. Inheritance Program
class Sanket:
    def f1(self):
        print("f1 function")
class Baba(Sanket):  
    def f2(self):
        print("f2 function")   
b=Baba()
b.f1()
b.f2()


# 2. Super Keyword
class Sanket:
    def f1(self):
        print("f1 function")
class Baba(Sanket):     
    def f2(self):
        super().f1()
        print("f2 function")
        super().f1()
b=Baba()
b.f2()


# 3
i,j=100,200       #Global Variables
class Father:
    a,b=1,2      #Class Variable
    
class Son(Father):
    x,y=10,20     #Class Variables

    def add(self,p,q):
        print(p+q)
        print(self.x+self.y)
        print(Father.a+Father.b)   #access another class variables 
        print(self.a+self.b)   #access another class variables (here self only becoz of the inheritance)
        print(i+j)
s=Son()
s.add(5,5)







