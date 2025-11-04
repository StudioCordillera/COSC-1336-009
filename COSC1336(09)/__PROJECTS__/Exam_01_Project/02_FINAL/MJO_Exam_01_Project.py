########################################
## Matthew Ochoa                   #####
## November 3, 2025                #####
## Project: 02                     #####
## Status: IN PROGRESS             #####
## Class: COSC 1336                #####
###############################################################
## Project 1 Objectives | Rent & Late Payment Calculator     ##
###############################################################

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


# Data Input | (User Prompted for variables)S
#  ------------------------------------------------
def getDataInput():

    tenant = getStringData('\tName of Tenant: ')
    day = getIntegerData('\tEnter the Day: ')
    month = getStringData('\tEnter the Month: ')
    year = getIntegerData('\tEnter the Year: ')
    usageFees = getFloatData('\tEnter Usage Fees: ')

    return tenant, day, month, year, usageFees 

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