f = open("write.txt","w")  #opening file in write mode 
f.write("i want to learn js") #overwrite all data and add new data

f=open("write.txt","r") # read file
print(f.read())


# Add data without Overwrite previous data(Append)
f = open("write.txt","a")  #opening file in write mode 
f.write("\nThis is Appeand new line")

f=open("write.txt","r") # read file
print(f.read())

f.close() #closing file

 