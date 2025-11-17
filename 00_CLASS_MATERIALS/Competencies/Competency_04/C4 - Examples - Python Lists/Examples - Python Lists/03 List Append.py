#append to a list
myList = ['Hyundai', 'Mazda', 'Kia', 'Chevrolet', 'Lotus'] 
myList.insert(1, "Audi")
names = "Tweeter"
myList.append(names)
myList.extend(['Dodge', 'Ford', 'Toyota'])                         
myList.append(['Honda', 'Acura', 'Lexus'])                        

print('The entire list is ',myList )
print('The length of the list is ',len(myList))                                      

print ('Repeat the first 3 elements 2 times ',2 * myList[:3] )
