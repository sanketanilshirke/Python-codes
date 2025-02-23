#WAF that replace all occurrences of “Java” with “python” in above file.
# Hi everyone
#  we are learning File I/O
#  using Java. 
# I like programming in Java.

with open("practice.txt","r") as f:
    data=f.read()
     
new_data=data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
     f.write(new_data)
  

