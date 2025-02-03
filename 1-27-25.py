x =("a", "b", "c", "d") #creates a tuple called x
x += tuple("e")
print(x)
print (x[0]) #calls tuple x at index 0
x1 ={"a", "b", "c", "d"} # creates set called x1
print (x1)
print ("a" in x1) #checks if "a" is in the set x1 
x1.add ("e") #adds "e" to set x1
print (x1)
x2 =["a", "b", "c", "d"] #creates a list 
x2.append("e")
print (x2)
x2.insert(4,"e")