# Name: Ally Baba
# Date: June 1, 2022
# Project Name: Template
# Status: Completed
# -----------------------------------------------------
# This program will ask users to enter an integer.
# The program will calculate the result (2 times the integer)
# Then, it will display the result
# -----------------------------------------------------
# 
def main():
    header()

    # Getting data from users
    numberOne = int(input('Enter the Integer: '))

    # Doubling the value
    doubleValue = numberOne * 2

    # Display the result
    print('\nResults')
    print('2 times', numberOne, 'is', doubleValue)

    footer()

# This function will display the header of the project
def header():
    print('----------------------------------------------')
    print('          Template')
    print("This program find 2xUser's entry")
    print('----------------------------------------------')

# This function will display the end of the project
def footer():
    print('\n----------------------------------------------')
    print('End of Project')
    print('----------------------------------------------')

main() 

