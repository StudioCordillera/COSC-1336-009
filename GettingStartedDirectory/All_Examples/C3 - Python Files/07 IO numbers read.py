# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
file = open('payroll.txt', 'r')

employeeRecord = file.readline()

while employeeRecord:
    print(employeeRecord)
    employeeRecord = file.readline()
    

file.close()

