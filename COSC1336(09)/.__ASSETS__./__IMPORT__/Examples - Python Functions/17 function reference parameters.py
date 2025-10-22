# Function definition is here
def changeMe( myList ):
   myList.append([1,2,3,4]);
   print ("Values inside the function: ", myList)

# Now you can call changeMe() function
myList = [10,20,30];
changeMe( myList );
print ("Values outside the function: ", myList)
