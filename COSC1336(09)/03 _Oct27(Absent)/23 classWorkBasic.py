# Ally Baba
# October 27, 2025
# Classwork #16
# ----------------------------
# Project Objectives
#   Learning the basics of Python
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tLearning basics of Python")
    print("-" * 60)

# This fucntion will display the end of project
def projectEnd():
    print('\n')
    print('-' * 60)
    print('\tEnd of project')

def main():
    # Display start of project
    projectStart()

    # Assign variable
    print('\tUser entry')
    valueOne = int(input('\tEnter an integer: '))
    valueTwo = int(input('\tEnter another integer: '))

    # Adding the numbers
    sumValues = valueOne + valueTwo                   

    # display summary
    print('\n')
    print('-' * 60)
    print('\tSummary')
    print('-' * 60)
    print('\tThe sum is: ', sumValues)
    
    # Display end of project
    projectEnd()
          
main()

# Trace: 29>22>24>10>11>12>13>14>27>17>18>19>20>30
