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

    # display all even numbers between 1 and 20
    # set of number 1 and 20
    # sub set

    stopWatch = 1

    while (stopWatch <= 20): # SET

        # get subset
        if (stopWatch % 2 == 0):
           print(stopWatch, '\tI am AllyBaba')

        stopWatch = stopWatch + 1 # increment

    
    # Display end of project
    projectEnd()
   
main()

# Trace: 
