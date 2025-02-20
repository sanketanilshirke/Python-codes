# WAP to print the length of a list. ( list is the parameter)
def length(abc):
    print(len(abc))

list=["a","b","c",4,5,6,7,87,8]
length(list)

# WAP to print the elements of a list in a single line. ( list is the parameter)
def elements(abc):
    for i in abc:
     print(i)

list=["anumalik","babaji","chutiya",4,5,6,7,87,8]
elements(list)

# WAP to find the factorial of n. (n is the parameter)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial(5)

# WAP to convert USD to INR. 
def convert(dollar):
    india_rupee = dollar*83
    print(dollar, "USD =", india_rupee,"INR")
convert(10)



