# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
def number_convert(n):
    val = int(n)
    return val

file = open('payroll.txt', 'r')

employeeRecord = file.readline()

while employeeRecord:
    
    
    # Then split that string to a list so I can use
    # each field individually...
    employeeRecord = employeeRecord.split()
    print (employeeRecord)

    print ('The name is -> ', employeeRecord[0])
    print ('The hourly wage is -> ',employeeRecord[1])
    print ('The hours worked is -> ',employeeRecord[2])
    print ('The Gender is -> ',employeeRecord[3])
    print('\n')

    employeeRecord = file.readline()
file.close()

