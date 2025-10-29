# Ally Baba
# October 27, 2025
# Classwork #24
# ----------------------------
# Project Objectives
#   Find the area of rectangle
#   Users will enter length and width (integers)
#   area = length * width
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tArea of Rectangle")
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
    length = int(input('\tEnter length of a rectangle: '))
    width = int(input('\tEnter width of rectangle: '))

    # Adding the numbers
    areaRectangle = length * width                  

    # display summary
    print('\n')
    print('-' * 60)
    print('\tSummary')
    print('-' * 60)
    print('\tThe area of rectangle is: ', areaRectangle)
    
    # Display end of project
    projectEnd()
          
main()

# Trace: 29>22>24>10>11>12>13>14>27>17>18>19>20>30
