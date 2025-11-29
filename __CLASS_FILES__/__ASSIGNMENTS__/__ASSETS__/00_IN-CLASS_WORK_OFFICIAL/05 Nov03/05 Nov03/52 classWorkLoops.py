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
    # -999 is called SENTINEL
    # Check before loop
    # Pre_read & inside loop update-read

#   Pre-read before loop
    value = getIntegerData("\tEnter an integer. -999 will terminate: ")

    while (value != -999):

        # Update LOOp
        value = getIntegerData("\tEnter an integer. -999 will terminate: ")

    
    # Display end of project
    projectEnd()
   
main()

# Trace: 51(2)>53(T)>54(23)>53(T)>54(-23)>53(T)>54(-999)>53(F)>60
