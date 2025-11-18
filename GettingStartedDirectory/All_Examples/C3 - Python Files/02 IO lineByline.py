# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# read a file line by line and add the numbers read

fileOpen = open('test1.txt','r')

sums = 0

for baba in range(5):
    value = int(fileOpen.readline())
    
    if (value % 2 == 0):
        print (value)
        sums = sums + value
        


print('The sum of the numbers read -> ', sums)

fileOpen.close()

