########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 27                 #####
## --------------------------------#####
## Project Objectives              #####
##   Learning the basics of Python #####
########################################

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

def main():
    # Display start of project
    projectStart()

    # Assign variable
    print('\tUser entry')
    hoursWorked = float(input('\tHow many hours did you work? '))
    wage = float(input('\tWhat is your wage? $'))
    
    # Multiplying hours worked
    grossPay = hoursWorked * wage

    # Call Summary
    displaySummary(grossPay)

    # Display end of project
    projectEnd()


# Function displays the summary
def displaySummary(grossPay):
    print('\n')
    print('-' * 60)
    print('\tSummary of Gross Pay')
    print('-' * 60)
    print('\tThe Gross pay is: $', format(grossPay, ".2f"), sep = '')
          
main()

# Trace: 2
