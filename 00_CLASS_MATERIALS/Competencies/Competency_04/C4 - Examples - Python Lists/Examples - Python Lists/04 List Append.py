#append to a list
myList = ['Hyundai', 'Mazda', 'Kia', 'Chevrolet', 'Lotus'] 
myList.insert(1, "Audi")
names = "Tweeter"
myList.append(names)
myList.extend(['Dodge', 'Ford', 'Toyota'])                         
myList.append(['Honda', 'Acura', 'Lexus'])                        

print('The entire list is ',myList )
print('The length of the list is ',len(myList))                                      

for elem in myList:
    print ("The value is ", elem, " and the length is ", len(elem))

    
print('length is more than 8 is ',[elem for elem in myList if len(elem) > 8] )           

print ('which has No Honda ',[elem for elem in myList if elem != "Honda"]   )

for elem in myList:
    print ("The value is ", elem, " and the count is ", myList.count(elem))

print ("The current list is ", myList)

print ('Repeat the list 2 times ',2 * myList )

print ('Repeat the first 3 elements 2 times ',2 * myList[:3] )
