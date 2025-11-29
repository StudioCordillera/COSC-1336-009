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
fileOutput = open('expenses.txt', 'w')

numbers = fileInput.readline()

while numbers:  

    #Then split that string to a list to use each block individually...
    numbers = numbers.split()
    
    name = numbers[0]
    wage = numbers[1]
    hours = numbers[2]
    
    print (name)
    print ('The hourly wage is -> ', wage)
    print ('The hours worked is -> ', hours)

    hoursWorked = numberConvert(hours)
    hourlyRate =  numberConvert(wage)

    if hoursWorked <= 40:
        totalPay = hoursWorked * hourlyRate
    else:
        totalPay = 40 * hourlyRate + (hoursWorked - 40) * hourlyRate * 1.5

    print('The total Pay is -> ', totalPay)

    print('\n')

    lines = name +  "  " + str(totalPay) + '\n'
    fileOutput.writelines(lines)

    numbers = fileInput.readline()
    
fileInput.close()
fileOutput.close()


