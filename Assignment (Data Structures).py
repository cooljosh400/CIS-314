import random
ColumnA = {"baseball","football","hockey", "basketball","tennis","swimming","boxing","golf","Rugby","bowling"} # A set of sports
ColumnB = ["bowling","Rugby","golf","boxing","swimming","tennis","basketball","hockey","football","baseball"] # A List of sports in reverse


#print (ColumnA[3]) <-- This will cause an error because sets are not indexed or ordered 
for item3 in (ColumnA):
    if item3 == "hockey":
        print ("prints the third element in the set:",item3)#This will work bypassing the rules of sets printing the 3rd element in the set
        print()

        print("prints the third element in the list:",ColumnB[2]) #in the list since it is indexed I can just print the 3rd element
        print()


        print ("random version of the set: ",ColumnA) #sets are not ordered so they will always be random
        print()
random.shuffle(ColumnB)# rearranges the order of the list in columnB


print("random version of the list: ",ColumnB)
print()

ColumnA.add("water polo")# adds "water polo" into the set
print ("Adds water polo into the set: ",ColumnA)
print()

ColumnB.append("skating") # adds "skating" to the end of the list
print ("Adds skating to the end of list: ",ColumnB)
print()

ColumnB.pop(0) #pops the first element out
print ("First list element removed: ",ColumnB)
print()

for x in ColumnA:
    if "baseball" in x:
        ColumnA.remove ("baseball")
        break
print("First set element removed: ",ColumnA) #removes whatever the first element is in the set
print()

index = 8
ColumnB.pop(index)
print("Removed football from the list: ",ColumnB,"\n") #removes football from the list using its index

ColumnA.remove("football")
print("football has now been removed from the set: ",ColumnA,"\n") #removes football from the set using .remove method