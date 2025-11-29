# Ally Baba
# October 27, 2025
# Classwork #25
# ----------------------------
# Project Objectives
#   Find the perimeter of triangle
#   Users will enter 3 sides(float)
#   perimeter = add 3 sides
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tArea of Triangle")
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
    sideOne = float(input("\tLength of side one: "))
    sideTwo = float(input("\tLength of side two: "))
    sideThree = float(input("\tLength of side three: "))

    # Adding the three sides to get perimeter          
    perimeterTriangle = sideOne + sideTwo + sideThree
    
    # display summary
    print('\n')
    print('-' * 60)
    print('\tSummary')
    print('-' * 60)
    print("\tPerimeter of triangle :", format(perimeterTriangle, ".2f"))
    
    # Display end of project
    projectEnd()
          
main()

# Trace: 29>22>24>10>11>12>13>14>27>17>18>19>20>30
