# Ally Baba
# November, 2025
# Classwork #89
# ----------------------------
# Project Objectives
#   Learning Lists
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tLearning Lists")
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
    value = input(prompt).strip(' ')

    return value

# This function will get a char input
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()

        if (value in ['B', 'C', 'X']):
            return value
        else:
             print('\t\tERRor MSG! Enter B | C | X')

def main():
    # Display start of project
    projectStart()

    # enter values until -999

    myValues = [] # empty list

    while (True):
        value = getIntegerData('\tEnter integers | -999 will terminate: ')

        if (value == -999):
            print('\tTah Tah')
            break

        myValues.append(value) # adding to the list

    # display all the entered value
    print('\tValues entered: ', myValues)
    print('\t# of values: ', len(myValues))
    print('\tSum of values: ', sum(myValues))
    
    # Display end of project
    projectEnd()
   
main()

# Trace:








