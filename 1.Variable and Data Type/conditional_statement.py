light=input("Enter light colour:")
if (light=="red"):
    print("Stop")
elif (light=="yellow"):
    print("Look")
elif(light=="green"):
    print("Go")
else:
    print("Wrong input Entered")
    
    
marks=int(input("Enter Marks:"))
if(marks>90 and marks<=100):
    print("A")
elif(marks>100):
    print("Invalid input")
elif(marks>80 and marks<=90):
    print("B")
elif(marks>70 and marks<=80):
    print("C")
elif(marks<0):
    print("Invalid input")
else:
    print("D")
