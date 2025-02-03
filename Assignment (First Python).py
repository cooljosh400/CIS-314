import keyword
password = input("Enter a valid password:" ) #input a password for the user
if password in keyword.kwlist:               #checks if password is in Keyword list
    print ("Not a valid password")
else: print ("valid password")
