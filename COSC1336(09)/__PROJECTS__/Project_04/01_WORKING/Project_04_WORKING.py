########################################
## Matthew Ochoa                   #####
## November 06, 2025               #####
## Project: 04                     #####
## Status: FINISHED                #####
## Class: COSC 1336                #####
###############################################################
## Project 4 Objectives | Input > Calc (Handling) > Summary  ##
###############################################################

# This function will return an integer input from the user
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a float input from the user
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message.  Enter numbers ONLY!')

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value

# This function will return a string input from the user
def getCharData(prompt):

    while (True):
        value = input(prompt)

        value = value.upper()
        if (value in ['W', 'D', 'E']):
            return value

        print('\t\tERROR Message: Wrong selection')


###############################################################
##    My Code Below                                          ##
###############################################################

# Display Start of Program Boiler SOPB
#  ------------------------------------------------------------------------
def projectStart():
    print('Start of Project 4')
    print('Written by: Your Name')
    print('Date: Enter date ')
    print('-' * 50 )
    print('\tHere your write project information')
    print('-' * 50 + '\n')

# Display End of Program Boiler EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print('-' * 50)
    print('End of Project')



###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 

    # Display SOPB
    projectStart()



    # Display EOPB
    projectEnd()
      
main() # calling the function main()


'''

Employee Income Tax Calculator 

Write a python program that does ... for AllyBaba Automotive
    records
    analyzes weekly pay 

There are 25 employees in the company. 
  
Requirements 
    Prompt for Total Number of Employees 
        - # of employees to process. 

    Collect Employee Information 
    
    For each employee, prompt the user to enter the following: 
       Employee ID Number (integer) 
       Employee Name (string – allow spaces) 
       Pay Rate per Hour (floating-point value) 
       Type of Employee (0 for Union, 1 for Management) 
       Number of Dependents (integer, range: 0 to 10) 
       Collect Timesheet Information 
 
    For each employee, after entering their details, prompt the user to enter: 
       Number of Hours Worked This Week (floating-point value) 
 
       
   Calculations 
   Gross Pay 

    Union members paid
        - normal pay rate first 40 hours worked, and overtime hours = 1.5 normal over 40.  
    
    Management employees paid
        - normal pay rate all hours under 40 and overtime hours 
 
    Income Tax 
        All employees pay income tax based on the following distribution chart # Of dependent  Tax Rate (%) 
            0 to 2    30% 
            3 to 5    20% 
            Above 5   10% 

        Net Pay  
        Gross Pay minus Income Tax.  
 
    Input validation 
        The input should be checked for reasonable values. If a value is not reasonable, your program should print an informative error message and ask the user to re-enter the value. 

        The following data should not be blank 
            name 
            COSC 1337 – Fundamentals of Programming 
            Project Assignment #4- Employee Income Tax Calculator 
 
        The following data should be positive numbers (greater than 0) 
            employee id 
            pay rate 
        The following data should be non-negative (0 or larger) 
            hours worked 
            Employee type should be 0 or 1 
            # of dependents between 0 and 10 
 
    Output Requirements 
        - The payroll report should be formatted in a tabular (row and column) format with each column clearly labeled with a column heading.  
        - All dollar amounts should be formatted with 2 decimal places.  
        - Note: do not use tabs between the columns - use the setw manipulator to set the column width so that you can line up columns of numbers on - the decimal point. 
        - Print one line for each transaction that contains:  
            - employee ID number  
            - name  
            - gross pay  
            - income tax  
            - net pay  
        - The payroll summary report should print
            - total:
                gross pay
                net pay/week (all employees) 
 
    Other Requirements 
        Global variables - Do not use global variables in your programs. Declare all your variablesinside functions. 
        Create and use "struct" to hold the general employee information for one employee. 
        Use an array of structs to hold the employee information for all employees.  
        You should use a struct to represent the employee information for each employee.  
        Note: you should NOT include Timesheet information in this struct. Timecard information may change from one pay period to the next while employee information usually does not. In other words, an employee's information and information about a specific paycheck are 2 different things and logically should not be combined in the same struct (or object). 
        The timesheet information (hours worked) does not need to be stored in an array. 

        Your program should first input the employee master information into an array of structs
        Then use a separate loop to do the payroll processing for each employee (input the employee's hours worked and calculate their pay). 
 
    Note: Use the python string class for the employee’s name.  
    Warning: Input using the extractor operator (">>") is simple. However, when you mix the extractor operator with the getline function, things get tricky.  


___________________________________________________________

COSC 1337 – Fundamentals of Programming 
Project Assignment #4- Employee Income Tax Calculator 

___________________________________________________________

Sample Output 
(User entry is in RED) 
 
Project #4 
Written by: Ally Baba 
 
AllyBaba Automotive Group  
------------------------------------------------ 
Number of payrolls to be processed: 4 
------------------------------------------------ 
 
Employee #1 
Employee id: 22 
Employee name: Cindy Burke 
Pay rate: $15.00 
Type: 0 
Dependent: 2 
------------------------------------------------ 
Employee #2 
Employee id: 42 
Employee name: J. P. Morgan 
Pay rate: $12.50 
Type: 0 
Dependent: 1 
------------------------------------------------ 
 Employee #3 
Employee id: 41 
Employee name: Sue Kim 
Pay rate: $14.50 
Type: 0 
Dependent: 0 
------------------------------------------------ 
Employee #4 
Employee id: 45 
Employee name: Ernest Chavez 
Pay rate: $20.0 
Type: 1 
Dependent: 2 
------------------------------------------------ 
 
 Timesheet information: 
Hours worked for Cindy Burke: 40.0 
Hours worked for J. P. Morgan: 39.5 
Hours worked for Sue Kim: 45.0 
Hours worked for Ernest Chavez: 41.0 
_____________________________________________________________________________
 
COSC 1337 – Fundamentals of Programming 
Project Assignment #4- Employee Income Tax Calculator 

Summary: Payroll Report 
Number of Employee processed: 4 
------------------------------------------------------------------------------ 
ID  Name  Gross Pay Tax Net Pay 
------------------------------------------------------------------------------ 
22  Cindy Burke   600.00  180.00 420.00 
42  J. P. Morgan  493.75  148.13 345.62 
41  Sue Kim  688.75  206.63 482.12 
45  Ernest Chavez 820.00  246.00 574.00 
------------------------------------------------------------------------------ 
 Total Gross Pay  $2602.50 
 Total Net Pay    $1911.74 
------------------------------------------------------------------------------ 
 
End of Project 4 
 
 

'''