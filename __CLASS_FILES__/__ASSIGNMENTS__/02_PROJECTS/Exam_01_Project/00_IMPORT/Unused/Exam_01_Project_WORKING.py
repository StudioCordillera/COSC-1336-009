########################################
## Matthew Ochoa                   #####
## November 24, 2025               #####
## Project: 01 (Exam_01)           #####
## Status: IN PROGRESS             #####
## Class: COSC 1336                #####
########################################
''' 
Exam Project 1 Objectives | Rent & Late Payment Calculator



'''
###############################################################
'''
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message. Enter numbers ONLY!')

# This function will return a float input from the user
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print('\t\tError Message. Enter numbers ONLY!')

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

# Start of Project Func
#  ------------------------------------------------
def projectStart():
    print('-' * 60)
    print('   Start of Exam 1 Project')
    print('-' * 60, '\n')
    print('\tRent & Late Payment Calculator')
    print('\t' + '-' * 50 + '\n')
    print('\tWritten by: Matthew Ochoa')
    print('\tDate: 11/03/2025')

# End of Project Func
#  ------------------------------------------------
def projectEnd():
    print('\n' + '-' * 50)
    print('   End of Exam 1 Project')
    print('-' * 50 + '\n')



# Summary Display Func
#  ------------------------------------------------
def displaySummary(day, month, year, tenant, daysLate, monthlyRent, usageFee, lateFees, totalDue):

    print('\n\t' + '-' * 50)
    print('\tRental Summary')
    print('\t' + '-' * 50, '\n')
    print('\t--- Rental Transaction for the month of ', month, ' ', year, ' ------', '\n')
    print('\tName of tenant: ', tenant)
    print('\tDay the rent is paid: ', day)

    print('\n\tDays Late: ', daysLate, ' days')

    print('\n\tMonthly rent: $', monthlyRent)
    print('\tUsage Fee: $', usageFee)
    print('\tLate Fees Charges: $', lateFees)
    
    print('\n\tTotal Due for ', month, day, ',', year, ' rent: $', totalDue)


# Data Input | (User Prompted for variables)
#  ------------------------------------------------
def getDataInput():


    tenant = getStringData('\tName of Tenant: ')
    day = getIntegerData('\tEnter the day: ')
    month = getStringData('\tEnter the month: ')
    year = getIntegerData('\tEnter the year: ')
    usageFees = getFloatData('\tEnter usage fees: ')

    return tenant, day, month, year, usageFees 

# Months Handling | Checks and returns if month is in range and what value corresponds or a flag for not so
#  ------------------------------------------------
def handleMonths(monthIn):

    monthList = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = 1
    if monthIn in monthList:
        for month in monthList:
            month = month + 1
        

    return flag, 


# Calculate Totals
#  ------------------------------------------------
def calcTotals(day, usageFees):

    monthlyRent = 2500
    daysLate = 0

    # 1-3 days into month
    if (day < 4):
        # Then no fine 
        lateFees = 0

    # Later than 3 days - 30 days
    elif (day < 31):
        # Then fined $10/days (late)
        daysLate = day - 3
        lateFees = daysLate * 10

    # Over 30 Days late
    else:
        # Then flat rate of $2000
        daysLate = day - 3
        lateFees = 2000
    
    # $2,500 + additional monthly usage fees
    totalDue = monthlyRent + usageFees + lateFees

    return daysLate, monthlyRent, lateFees, totalDue



###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 
    
    # Calls function to display the start of project
    projectStart()

    # Get user data
    tenant, day, month, year, usageFees = getDataInput()

    # Get Calculated Totals
    daysLate, monthlyRent, lateFees, totalDue = calcTotals(day, usageFees)

    # Call Display Func
    displaySummary(day, month, year, tenant, daysLate, monthlyRent, usageFees, lateFees, totalDue)

    # Calls function to display the end of project
    projectEnd()
      


main() # calling the function main()

'''
'''







LATE PAYMENT RULES:
    1. On-Time Payment (Days 1-3):
        - No late fee if paid on or before day 3
        - lateFees = 0
    
    2. Late Payment (Days 4-30):
        - $10 per day late fee for each day after the 3rd
        - lateFees = (day - 3) * $10
        - Example: Day 4 = (4 - 3) * $10 = $10
    
    3. Severely Late Payment (After Day 30):
        - Flat late fee of $2,000
        - lateFees = $2,000


PROGRAM OUTPUT:
    Detailed summary including:
    - Tenant's name
    - Month and year
    - Rent payment day
    - Days late
    - Monthly rent ($2,500)
    - Usage fees
    - Late fees
    - Total amount due


FUNCTIONS:
    1. Function for getting validated integer data | x
    2. Function for getting validated float data | x
    3. Function for getting validated string data | x
    4. Function for data input collection (tenant, month, year, day, usage fees)
        - Input validation to prevent errors
    5. Function for displaying rental summary, total amount due, & late fees based on payment day
        - Month Handling
    6. Main function to orchestrate program flow



'''
def payDay():
    days = 60
    return days

def calcLateFeestwo(days):
    if (days < 4): 
            lateFees = 0 
    elif (days < 31): 
            lateFees = (days - 3) * 10
    elif (days > 30): 
            lateFees = 2,000 
            
    return lateFees

def main():
    
    days = payDay()
    
    lateFees = calcLateFeestwo(days)
    
    print(lateFees)
    
    
    
main()

'''

Scenari0
AllyBaba owns a residential property that is 2,200 sq. ft. in size, featuring 3 
bedrooms and 2 bathrooms. The monthly rent for this property is $2,500, with 
additional monthly usage fees as applicable. 
---------------------
This program calculates and summarizes the tenant’s total monthly payment, 
including any late fees based on the date the rent is paid. 
--------------
 
REQUIREMENTS
 - Assumption: Each month has 30 days.
 Late Payment Rules 
    if (days < 4): 
            lateFees = 0 
    elif (days < 31): 
            lateFees = (4 – 3) * $10 = $10 
    elif (days > 30): 
            lateFees = $2,000 

VARIABLES
• Tenant’s name 
• Month and year of rent payment 
• Day of the month the rent was paid 
• Monthly usage fees 
• Days late 
• Monthly rent ($2,500) 
• Late fees 
• Total amount due 

FUNCTIONS


• getInput
    • input validation
        • especially for date-related entries
        • positive numbers
• calcLateFees
• displayresultS


OPERATIONS
 
 

 


User Inputs: 
• Tenant’s name 
• Month and year of rent payment 
• Day of the month the rent was paid 
• Monthly usage fees 


Program Output: 
A detailed summary including: 
• Tenant’s name 
• Month and year 
• Rent payment day 
• Days late 
• Monthly rent ($2,500) 
• Usage fees 
• Late fees 
• Total amount due 



'''