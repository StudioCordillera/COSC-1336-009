# ---------------------------------------------
# Name: She Man
# Date: November 1, 2025
# Project: Project 3
# Status: WIP
# Class: COSC 1336
# ---------------------------------------------
# Project Objectives
# AllyBaba Bank charges a flat fee of $10 per month for maintaining a checking
# account. In addition, the bank applies a fee per check based on the number
# of checks written in the past month
# ---------------------------------------------

# This function will display the start of the project
def projectStart():
    print('Start of Project 3')
    print('Written by: King AllyBaba')
    print('Date: ')
    print('-' * 50 + '\n')
    print('\tBank Fees')
    print('-' * 50 + '\n')

# This function will display the start of the project
def projectEnd():
    print('-' * 50 + '\n')
    print('End of Project 3')

# This function will return an integer input from the user
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))

            if (value > 0):
                return value
            else:
                print('\t\tError MSG! No negative values')
        except ValueError:
            print('\t\tError MSg! Not an integer')

# This function will return a float input from the user
def getFloatData(prompt):
    value = float(input(prompt))
    return value

# This function will return a string input from the user
def getStringData(prompt):
    month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

    while (True):
        value = input(prompt)

        if (value.upper() in month):
            return value
        else:
            print('\t\tError MSG! Wromg Month')

# This fucntion will display the summary
def displayResult(month, countCheck, totalFee):
    print('\n')
    print('-' * 50)
    print('\tMonthly Fee summary')
    print('-' * 50)
    print('\tThe month of :' , month)
    print('\tFor writing ', countCheck, ' the bank fee is $', format(totalFee, '.2f'), sep = '')

# This fucntion will fidn the bank fee
def findBankFee(countCheck):
    BASIC_FEE = 10.00

    if (countCheck >= 60):
        bankFee = 0.04
    elif (countCheck >= 40):
        bankFee = 0.06
    elif (countCheck >= 20):
        bankFee = 0.08
    else:
        bankFee = 0.10

    totalFee = BASIC_FEE + bankFee * countCheck 

    return totalFee

# This fucntion get a char entry
def getCharData(prompt):
    while (True):
        value = input(prompt)

        if (value.upper() in ['Y', 'N']):
            return value
        else:
            print('\t\tERRor MSG! Invalid entry')
                
def main(): 
    # Calls function to display the start of project
    projectStart()

    while (True):
        # Get user's input
        month = getStringData('\tEnter the month: ')
        countCheck = getIntegerData('\tEnter number of checks: ')

        # calculation
        totalFee = findBankFee(countCheck)   

        # Display
        displayResult(month, countCheck, totalFee)

        cmd = getCharData('\tY to continue! N to exit')

        if (cmd == 'N'):
            print('\tTah tah')
            break

    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()


