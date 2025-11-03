# getData1() gets the salary from the user input
def getData1():
    salary = float(input('Please enter your base salary '))
    return salary

# getData2() gets the bonus from the user input
def getData2():
    bonus = float(input('Please enter your the bonus '))
    return bonus

# main() performs all the programinng
def main():
    salary = getData1()
    bonus = getData2()

# main() is used to initiate the stage of the program
main()
