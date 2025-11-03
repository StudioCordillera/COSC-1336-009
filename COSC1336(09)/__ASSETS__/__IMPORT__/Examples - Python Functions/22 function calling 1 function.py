# getData1() gets value from user input
def getData(prompt):
    value = float(input(prompt +'$'))
    return value

# processData() will find the totla salary
def processData(bonus, salary):
    return bonus + salary

#printData() will display results on the screen
def printData(totalSalary):
    print('My monthly income is $' + format(totalSalary, '7.2f'))

# main() performs all the programinng
def main():
    # getting users input for salary and bonus 
    salary = getData('Please enter your base salary ')
    bonus = getData('Please enter your the bonus ')

    # finding the total salary
    totalSalary = processData(bonus, salary)

    # display results to screen
    printData(totalSalary)

# main() is used to initiate the stage of the program
main()
