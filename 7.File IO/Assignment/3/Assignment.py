# Search if the word “learning” exists in the file or not.

def check_word():
  with open("practice.txt","r") as f:
    data=f.read()
    if(data.find("learning") !=-1):
        print("Found")
    else:
        print("Not Found") 
check_word()





