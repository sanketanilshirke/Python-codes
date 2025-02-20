def sanket(a,b): #parameters
    sum=a+b
    print(sum)
    return sum 
 
sanket(2,3) #callig fuction  ,  2 & 3 ->Arguments
sanket(4,5) #callig fuction
sanket(5,5) #callig fuction


#2
def calculate(a,b):
    return a + b
sum=calculate(100,299)
print(sum)

#3
def print_hello():  #No parameters
      print("hello")
print_hello()
print_hello()
print_hello()

#Average of 3 numbers
def avg(a,b,c):
  sum= a+b+c
  print(sum/3)
  return sum
avg(2,2,2)

#default parameter example
def cal_product(a=2,b=2):
   print (a * b)
   return a * b
cal_product()
 

#
def my_function(*kids):
  print(kids)
my_function("Emil", "Tobias", "Linus")



