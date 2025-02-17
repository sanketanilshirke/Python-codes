#WAP to ask the user to enter names of their 3 favourite movies and store them in list
movieslist=[]
m1=(input("1st:"))
m2=(input("2nd:"))
m3=(input("3rd:"))

movieslist.append(m1)
movieslist.append(m2)
movieslist.append(m3)
print(movieslist)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list=[1,2,3,4,3,2,1]
list2=list.copy()
list2.reverse()
if (list == list2):
    print("palindrome")
else:
    print("not palindrome")
    
    
# WAP to count the number of students with the “A” grade in the following tuple.
# ["C”, “D”, “A”, “A”, “B”, “B”, “A”]
grade= ["C", "D", "A", "A", "B", "B", "A"]
print(grade.count("A"))

# Store the above values in a list & sort them from “A” to “D”
grade.sort()
print(grade)