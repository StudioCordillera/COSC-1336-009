########################################
## Name: Matthew                   #####
## Date: October 22, 2025          #####
## Project Name: Integer Doubler   #####
##               program           #####
## Status: In-Progress             #####
## --------------------------------#####
## Project Functions               #####
##  - Take 1 inputs from user      #####
##  - Calculate 2 times the input  #####
##  - Display the result           #####
##      - 2 times input            #####
##  - Look stylish with labeler    #####
##    functions                    #####
########################################


# ------------------------------------ #
# Main function
# ------------------------------------ #

def main():

    # Call header
    header()

    # Getting data from users
    # Declare input as numberOne (integer)
    numberOne = int(input('Enter the Integer: '))

    # Doubling the value of numberOne and store it in doubleValue
    doubleValue = numberOne * 2

    # Display Title: Results and print the verbal expression
    print('\nResults')
    print('2 times', numberOne, 'is', doubleValue)

    # Call footer
    footer()


# ------------------------------------ #
# Functions
# ------------------------------------ #

## Header function | to display the title of the project
def header():
    print('----------------------------------------------')
    print('          Integer Doubler Program')
    print('            by: Matthew Ochoa')
    print("This program finds 2 times the user's entry")
    print('----------------------------------------------')

## Footer function | to notify user that the program has ended
def footer():
    print('\n----------------------------------------------')
    print('End of Project')
    print('----------------------------------------------')

main() 

