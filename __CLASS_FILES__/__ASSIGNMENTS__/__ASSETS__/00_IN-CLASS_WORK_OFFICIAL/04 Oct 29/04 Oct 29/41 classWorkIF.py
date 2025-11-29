# Ally Baba
# October 29, 2025
# Classwork #35
# ----------------------------
# Project Objectives
#   Learning IFs
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tLearning IFs")
    print("-" * 60)

# This fucntion will display the end of project
def projectEnd():
    print('\n')
    print('-' * 60)
    print('\tEnd of project')

# This function will get the user's entry for a float
def getFloatData(prompt):
    value = float(input(prompt))

    return value

# This fucntion will get the user's entry for an integer
def getIntegerData(prompt):
    value = int(input(prompt))

    return value

# This function will get the user's entry of string
def getStringData(prompt):
    value = input(prompt)

    return value

def main():
    # Display start of project
    projectStart()

    # Assign variable
    print('\tUser entry')
    value = getIntegerData('\tEnter an integer: ')
    
    # ?? Display if multiple of 5 or 7 or not
    if (value % 5 == 0 or value % 7 == 0):
        print('\tIt is multiple of 5 or 7')
    else:
        print('\tIt is not multiple of 5 or 7')

    
    # display summary
    
    # Display end of project
    projectEnd()
   
main()

# Trace: 
