# Function definition is here
def changeMe( myList ):
   "This changes a passed list into this function"
   myList = [1,2,3,4]; # This would assign new reference in mylist
   print ("Values inside the function: ", myList)

# Now you can call changeMe() function
myList = [10,20,30];
changeMe( myList );
print ("Values outside the function: ", myList)
