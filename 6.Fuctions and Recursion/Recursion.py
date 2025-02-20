#recursive fuction
def show(n):
    if (n==0):
        return 
    print(n)
    show(n-1)
   
show(5) # i want to print 5, 4, 3, 2, 1  -> (n-1)


# 2 (Factorial)
def fact (n):
    if(n==1 or n==0):
        return 1
    elif (n<0):
        print("your number is negative")
    else:
        return fact(n-1)*n
print(fact(5))


# 2 (Factorial) dubey
def fact(n):
    if(n<=1): 
        return 1
    else:
        return n * fact(n-1)

print(fact(5))





