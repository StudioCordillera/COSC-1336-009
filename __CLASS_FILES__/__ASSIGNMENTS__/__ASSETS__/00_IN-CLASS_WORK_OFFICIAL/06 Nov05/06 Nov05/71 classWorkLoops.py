# Ally Baba
# November, 2025
# Classwork #71
# ----------------------------
# Project Objectives
#   Learning Loops
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tLearning Loops")
    print("-" * 60)

# This fucntion will display the end of project
def projectEnd():
    print('\n')
    print('-' * 60)
    print('\tEnd of project')

# This function will get the user's entry for a float
def getFloatData(prompt):
    while (True):
        try:
            
            value = float(input(prompt))

            return value

        except ValueError:
            print('\t\tERRor MSG! Non numbers entered')

# This fucntion will get the user's entry for an integer
def getIntegerData(prompt):

    while (True):
        try:
            value = int(input(prompt))

            return value

        except ValueError:
            print('\t\tERRor MSG! Non numbers entered')

# This function will get the user's entry of string
def getStringData(prompt):
    value = input(prompt)

    return value

# This function will get a char input
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()

        if (value in ['Y', 'N']):
            return value
        else:
             print('\t\tERRor MSG! Enter Y or N')

def main():
    # Display start of project
    projectStart()

    dividend = getIntegerData('\tEnter dividend: ')
    divisor = getIntegerData('\tEnter divisor: ')

    try:
        result = dividend / divisor

        print('\tThe result is: ', result)

    except ZeroDivisionError:
        print('\t\tError MSG! Cannot divide by Zorro')
    
    
    # Display end of project
    projectEnd()
   
main()

# Trace: 
