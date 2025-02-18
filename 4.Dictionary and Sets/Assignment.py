# Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
#  cat : “a small animal”
dict={}
dict["table"]=("a piece of furniture ","list of facts & figures")
dict["cat"]="a small animal"
print(dict)

#  You are given a list of subjects for students. Assume one classroom is required for 1
#  subject. How many classrooms are needed by all students.
#  ”python”, “java”, “C++”, “python”, “javascript”,
#  “java”, “python”, “java”, “C++”, “C”
set={"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(set))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value
empty_dict={}
a=int(input("enter physics marks:"))
empty_dict["physics"]=a
b=int(input("enter math marks::"))
empty_dict["math"]=b
c=int(input("enter chemistry marks::"))
empty_dict["chemistry"]=c
print(empty_dict)

# Figure out a way to store 9 & 9.0 as separate values in the set. 
# (You can take help of built-in data types) 
a={("int",9),("float",9.0)}
print(a)




