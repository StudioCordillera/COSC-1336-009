# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
def numberConvert(n):
    val = float(n)
    return val

file = open('payroll.txt', 'r')
numbers = file.readline()

while numbers:  

    #Then split that string to a list so I can use each number block individually...
    numbers = numbers.split()
    print ('The name is -> ', numbers[0])
    print ('The hourly wage is -> ',numbers[1])
    print ('The hours worked is -> ',numbers[2])

    totalPay = numberConvert(numbers[1]) * numberConvert(numbers[2])

    print('The total Pay is -> ', totalPay)
    

    print('\n')

    numbers = file.readline()
    
file.close()

