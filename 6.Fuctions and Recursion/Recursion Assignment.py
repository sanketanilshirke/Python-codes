#Write a recursive function to calculate the sum of first n natural numbers. 
def sum(n):
    if( n == 1):  
        return 1
    else: 
        return n + sum(n - 1)
print(sum(3))

# Write a recursive function to print all elements in a list.
#  Hint : use list & index as parameters.
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits=("mango","chiku","papaya","banana")
print_list(fruits)



#countdown code
def countdown(n):
    # Base case: if n is 0, stop
    if n == 0:
        return
    # Recursive case: print n and call countdown with n-1
    else:
        print(n)
        countdown(n - 1)

# Example usage
countdown(5)