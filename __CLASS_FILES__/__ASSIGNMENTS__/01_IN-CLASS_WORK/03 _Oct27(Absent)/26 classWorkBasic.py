# Ally Baba
# October 27, 2025
# Classwork #25
# ----------------------------
# Project Objectives
#   Find the gross Pay
#   Users will enter hours worked snd wage
#   Gross pay = wage times hours worked
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tFinding Gross Pay")
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
    hoursWorked = float(input('\tHow many hours did you work? '))
    wage = float(input('\tWhat is your wage? $'))
    
    # Multiplying hours worked
    grossPay = hoursWorked * wage
    
    # display summary
    print('\n')
    print('-' * 60)
    print('\tSummary of Gross Pay')
    print('-' * 60)
    print('\tThe Gross pay is: $', format(grossPay, ".2f"), sep = '')
    
    # Display end of project
    projectEnd()
          
main()

# Trace: 29>22>24>10>11>12>13>14>27>17>18>19>20>30
