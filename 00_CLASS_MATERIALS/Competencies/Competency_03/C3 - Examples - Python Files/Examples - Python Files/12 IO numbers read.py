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

employeeRecord = fileInput.readline()

while employeeRecord:  

    #Then split that string to a list to use each block individually...
    employeeRecord = employeeRecord.split()
    print ('The name is -> ', employeeRecord[0])
    print ('The hourly wage is -> ',employeeRecord[1])
    print ('The hours worked is -> ',employeeRecord[2])

    hoursWorked = numberConvert(employeeRecord[2])
    hourlyRate =  numberConvert(employeeRecord[1])

    if hoursWorked <= 40:
        totalPay = hoursWorked * hourlyRate
    else:
        totalPay = 40 * hourlyRate + (hoursWorked - 40) * hourlyRate * 1.5

    print('The total Pay is -> ', totalPay)

    print('\n')

    lines = employeeRecord[0] +  "  " + str(totalPay) + '\n'
    fileOutput.writelines(lines)

    employeeRecord = fileInput.readline()
    
fileInput.close()
fileOutput.close()


