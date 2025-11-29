# Ally Baba
# November, 2025
# Classwork #44
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

    # enter integers until -999

    while (True):
        value = getIntegerData('\tEnter an integer. -999 will terminate: ')

        if (value == -999):
            print('\tTah Tah')
            break
        
    # Display end of project
    projectEnd()
   
main()

# Trace: 70....... 53(12)>55(T)>57>58>61(33)>55(T)>57>58>61(0)>55(F)>63>64>68
