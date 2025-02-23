f = open("read.txt","r")  #opening file in read mode
data = f.read()  # reading file
print(data)
print(type(data))
f.close()


# for reading first 5 letters in file
f = open("read.txt","r")  #opening file 
data = f.read(5)  # reading file
print(data)
f.close()

# reading file line by line
f = open("read.txt","r")  #opening file 
data1 = f.readline()  # reading file line by line
print(data1) 
data2 = f.readline()  # reading file line by line
print(data2)
f.close()




