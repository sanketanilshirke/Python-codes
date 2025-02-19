#Print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i=i+1
    
# Print numbers from 100 to 1.
i=100
while i>=1:
    print(i)
    i=i-1

#Print the multiplication table of a number n.
no = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(no * i)
    i += 1 

# Print the elements of the following list using a loop: 
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
num=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i=0
while i<len(num):
    print(num[i]) #num[0], num[2], num[3]
    i+=1

#  Search for a number x in this tuple using loop:
#  (1, 4, 9, 16, 25, 36, 49, 64, 81,100) 
nums=(1, 4, 9, 16, 25, 36, 49, 64, 81,100) 
x=36 #searching for 36
i=0
while i<len(nums):
    if(nums [i]==x):
        print("FOUND",i)
        break
    else:
        print("finding...")
    i+=1


    