# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
def numberConvert(n):
    val = float(n)
    return val

fileInput = open('payroll.txt', 'r')
numbers = fileInput.readline()

while numbers:  

    #Then split that string to a list so I can use each number block individually...
    numbers = numbers.split()
    print ('The name is -> ', numbers[0])
    print ('The hourly wage is -> ',numbers[1])
    print ('The hours worked is -> ',numbers[2])

    hoursWorked = numberConvert(numbers[2])
    hourlyRate =  numberConvert(numbers[1])

    if hoursWorked <= 40:
        totalPay = hoursWorked * hourlyRate
    else:
        totalPay = 40 * hourlyRate + (hoursWorked - 40) * hourlyRate * 1.5

    print('The total Pay is -> ', totalPay)

    print('\n')

    numbers = fileInput.readline()
    
fileInput.close()

