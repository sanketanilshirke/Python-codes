#if we don't have txt file and we open it in write mode 
#then python automatically create us a new file 

f = open("demo write.txt","w+")   #w+ is write and read mode
f.write("This is write file")
f.seek(0)   # Move pointer to the start of the file
print(f.read())
f.close() #closing file

 