null=set( ) 
print(null) #Print null set

null.add(1)  #adds an element 
null.add(2)  #adds an element 
null.add(3)  #adds an element 
null.add((10,20))  #adds an element 
null.add( "malikk")  #adds an element 
print(null)

null.remove("malikk")  #removes the element
print(null)

null.pop( )  #removes a random value 
print(null)

null.clear( )  #empties the set
print(null)

s1={1,2,3,4,5}
s2={4,5,6,7,8}
a=s1.union( s2 )  #combines both set values & returns new 
print(a)
b=s1.intersection( s2 )  #combines common values & returns new
print(b)