#append to a list
myList = ['Hyundai', 'Mazda', 'Kia', 'Chevrolet', 'Lotus'] 
myList.insert(2, "Audi")                                
print('1.',myList[0])

# add a score
names = "Tweeter"
myList.append(names)
print('2.',myList[5])

#
print('3.',myList)

#
myList.extend(['Dodge', 'Ford', 'Toyota'])                         
print('4.',myList )

print('5.',len(myList))                                          

print('6.',myList[-1] )

print('7.',myList[7] )

myList.append(['Honda', 'Acura', 'Lexus'])                        

print('8.',myList )

print('9.',len(myList))                                      

print('10.',myList[-1] )

print('11.',myList[7] )

print('12.',[elem for elem in myList if len(elem) > 8] )           

print ('13.',[elem for elem in myList if elem != "Honda"]   )            

print ('14.',[elem for elem in myList if myList.count(elem) == 5] )

print ('15.',2*myList[:3] )



