# 1
class Account:
    def __init__(self,acc_no,acc_pwd):
        self.acc_no= acc_no
        self.__acc_pwd= acc_pwd   # Making private attribute
    
    def reset_pwd(self):     # Function is inside the Class
        print(self.__acc_pwd)  # Private attribute accessible inside class

acc1=Account(12345,"BABA@123")
print(acc1.acc_no)
acc1.reset_pwd()
print(acc1.__acc_pwd)  # Private attribute not accessible outside class


# 2
class Person:
    __name = "anonymous" # Private Attribute

    def __method(self):    # Private method 
        print("Private Method",self.__name)

    def welcome(self):
        self.__method()   #accessing private method by this class internal fuction
        print(self.__name)  #accessing private attribute

p1=Person()
p1.welcome()
print(p1.__name)  #gives error
p1.__method()   #gives error


