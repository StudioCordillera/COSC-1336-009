# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
vList = []
sum = 0
file = open('test2.txt', 'r')

while 1: 
        numbers = file.readline()
        
        if numbers:
                sum = sum + int(numbers)
                vList.append(int(numbers))
        
        if not numbers: 
                break # end of file
        
        numbers = numbers[:-1] # strip end of line
        
print (sum)
print(vList)






