class Voice:
    @staticmethod  #decorator
    def Cat():   #does not contain any parameter
     print("Meow Meow")

v= Voice()
Voice.Cat()    #can be access by using class name
   