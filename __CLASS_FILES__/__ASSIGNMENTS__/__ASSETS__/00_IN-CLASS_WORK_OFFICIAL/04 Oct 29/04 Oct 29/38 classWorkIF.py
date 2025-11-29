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
    
    # ?? Display if even or odd
    if (value % 2 == 0):
        print('\tIt is EVEN')
    else:
        print('\tIt is ODD')

    
    # display summary
    
    # Display end of project
    projectEnd()
   
main()

# Trace: 47(value=22)>53(?T)>54>63
# Trace: 47(value=0)>53(?F)>55(?T)>56>63
# Trace: 47(value=-2)>53(?F)>55(?F)>57>58>63
