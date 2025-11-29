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

    # enter integers until 0
    # display how many numbers entered
    # display the sum of numbers

    counter = 0 # sets the stopwatch
    sumNumbers = 0 # accumulator

#   Pre-read before loop
    value = getIntegerData("\tEnter an integer. 0 will terminate: ")

    while (value != 0):

        counter = counter + 1 # increment by 1
        sumNumbers = sumNumbers + value # adding the entered valid numbers

        # Update LOOp
        value = getIntegerData("\tEnter an integer. 0 will terminate: ")

    print('\tNumber of value entered: ', counter)
    print('\tThe sums: ', sumNumbers)

    
    # Display end of project
    projectEnd()
   
main()

# Trace: 70....... 53(12)>55(T)>57>58>61(33)>55(T)>57>58>61(0)>55(F)>63>64>68
