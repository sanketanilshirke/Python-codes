dict={
    
    "key":"value",
    "name":"sanket",
    "cgpa": 7.93,
    "topics":("c","cpp","python"),
    "marks":[22,32,20],
    12:190
}
print(dict.keys()) #returns all keys 
print(dict.values()) #returns all values 
print(dict.items( ))  #returns all (key, val) pairs as tuples
print(len(dict)) 
print(dict.get("key"))  #returns the key according to value
print(dict.get("key22"))  #No Error->None

dict.update({"city":"pune"} )  #inserts the specified items to the dictionary
print(dict)
dict["surname"]="shrike"
print(dict)


del dict["cgpa"]   #delete key
print(dict)
print(dict.pop(12)) #get the removed value
print(dict)


