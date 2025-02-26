# Create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average.
class Student:
    def __init__ (self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def method(self):
            print(self.name,"avg is:",self.m1+self.m2+self.m3/3)
            
s=Student("Sanket",2,2,2)
s.method()
    


# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance
class Account:
    def __init__(self,balance,account_no):
        self.bal=balance
        self.acc_no=account_no

    def debit(self, amount):
        self.bal -=amount
        print("Debited amount = ",amount)
        print("total balance=", self.get_balance())

    def credit(self,amount):
        self.bal +=amount
        print("Credited Amount =",amount)
        print("total balance=", self.get_balance())
        
    def get_balance(self):
        return self.bal

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(5000)
  
