# Ally Baba
# October 29, 2025
# Classwork #27
# ----------------------------
# Project Objectives
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tLearning Functions")
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
    

def main():
    # Display start of project
    projectStart()

    # Assign variable
    print('\tUser entry')
    
    hoursWorked = getFloatData('\tHow many hours did you work? ')
    wage = getFloatData('\tEnter your wage: $')
    
    # Multiplying hours worked
    
    # display summary
    print('\tHours worked: ', hoursWorked)
    
    # Display end of project
    projectEnd()

   
main()

# Trace: 2
