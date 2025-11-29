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

            if (value > 5):
                return value
            else:
                print('\t\tError MSG! Enter values more than 5')

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


    # ask users to enetr value more than 5

    value = getIntegerData('\tEnter a number more than 0: ')
    
    # Display end of project
    projectEnd()
   
main()

# Trace: 
