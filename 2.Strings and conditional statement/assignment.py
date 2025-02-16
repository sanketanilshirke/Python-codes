#Python script that takes a user's first name as input and prints the length of the name
first_name = input("Please enter your first name:")
print("The length of your first name is:", len( first_name))
print(first_name[0])#access character in string

#wap to find the occurence of $ in a string
user_string = input("Please enter a string: ")
count = user_string.count('$')
print("The $ sign appears",count ,"times in the string")

#program to check no entered by user is odd or even 
a=int(input("enter a number:"))
if a%2==0:
    print("even")
else :
    print("odd")
    
# wap to find greatest of 3 numbers entered by user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
greatest = max(num1, num2, num3)
print("The greatest of the three numbers is:",greatest)

#check the number is multiple by 7 or not
num=int(input("enter a number:"))
if (num%7==0):
 print("yes its multiple of 7")
else:
 print("not multiple of 7")   

