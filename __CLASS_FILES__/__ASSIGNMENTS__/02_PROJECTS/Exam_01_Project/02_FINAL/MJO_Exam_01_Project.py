########################################
## Matthew Ochoa                   #####
## November 24, 2025               #####
## Project: 01 (Exam_01)           #####
## Status: COMPLETE                #####
## Class: COSC 1336                #####
########################################
''' Project 1 Objectives | Rent & Late Payment Calculator     

    GET INPUT
        Name
        Payment Day
        Month
        Year
        Usage Fees
        
    VALIDATE
        Data types of input variables
        Greater than 0 integer values from input variables
    
    PROCESS
    
    OUTPUT


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
def getDataInput(monthList, inFunc):

    tenant, month = '', ''
    day, year = 0, 0
    usageFees = 0.0
    
    
    varKeys = {
    
        'Tenant': {
            'prompt' : '\tEnter tenant name: ',
            'variable': tenant
        },
        
        'Month': {
            'prompt' : '\tEnter payment month: ',
            'variable': month
        },
        'Day':{
            'prompt' : '\tEnter payment day: ',
            'variable' : day,
        },
        'Year':{
            'prompt' : '\tEnter payment year: ',
            'variable': year
        },
        'Usage Fee': {
            'prompt' : '\tEnter usage fee: ',
            'variable' : usageFees
        }
    }
    
    
    
    
    for key in varKeys:
        # varKeys[key].items()
        # varKeys[key]['prompt']
        # varKeys[key]['variable']
        
        while True:
            try:
                varKeys[key]['variable'] = shenanigans(varKeys[key]['prompt'])
                
                if (varKeys[key] == 'month'):
                    break
                else:
                    print('\t\tONLY MONTHS IN FULL OR ABBREVIATED NOTATION!!')
                
            except ValueError:
                print(f'\t\tONLY {type(varKeys[key]['variable'])} TYPE VARIABLES!!')

            
    # tenant = shenanigans('\tEnter the Day: ')
    # day = shenanigans('\tEnter the Day: ')
    # year = shenanigans('\tEnter the Year: ')
    # usageFees = shenanigans('\tEnter Usage Fees: ')
    # 
    # month = shenanigans('\tEnter the Month: ')
    
    tenant = tenant.lower().capitalize()
    month = month.strip().lower().capitalize()

    return tenant, day, month, year, usageFees 


def shenanigans(dataType, prompt, listNeeded):
 
    while True:
        if dataType is str:
                variable = getStringData(prompt).strip().lower()
                
                if listNeeded is not None:
                    if variable not in listNeeded:
                        print('\t\tENTER A MONTH!!')
                    else:
                        break
                else:
                    break

        elif dataType is int:
            try:
                variable = getIntegerData(prompt)
                if (variable > 0):
                    break
                else:
                    print('\t\tONLY POSITIVE + NON-ZERO NUMBERS!!')
            except ValueError:
                print('\t\tONLY INTEGER DATA!!')

        elif dataType is float:
            try:
                variable = getFloatData(prompt)
                if (variable > 0):
                    break
                else:
                    print('\t\tONLY POSITIVE + NON-ZERO NUMBERS!!')
            except ValueError:
                print('\t\tONLY NUMERICAL DATA!!')
                
    return variable
                    
  
# Calculate Totals
#  ------------------------------------------------
def calcTotals(day, usageFees):

    monthlyRent = 2500

    # 1-3 days into month
    if (day < 4):
        # Then no fine 
        daysLate = 0
        lateFees = 0

    # Later than 3 days - 30 days
    elif (day < 31):
        # Then fined $10/days (late)
        daysLate = day - 3
        lateFees = daysLate * 10

    # Over 30 Days late
    else:
        # Then flat rate of $2000
        daysLate = 30
        lateFees = 2000
    
    # $2,500 + additional monthly usage fees & late fees
    totalDue = monthlyRent + usageFees + lateFees

    return daysLate, monthlyRent, lateFees, totalDue



###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 
    
    monthList = {
        'january': 1, 'jan': 1,
        'february': 2, 'feb': 2, 
        'march': 3, 'mar': 3, 
        'april': 4, 'apr': 4, 
        'may': 5, 'may': 5, 
        'june': 6, 'jun': 6,
        'july': 7, 'jul': 7,
        'august': 8, 'aug': 8,
        'september': 9, 'sep': 9, 'sept': 9,
        'october': 10, 'oct': 10,
        'november': 11, 'nov': 11,
        'december': 12, 'dec': 12,
        }
    
    inFunc = {
        'INT': getIntegerData,
        'STR': getStringData,
        'FLOAT': getFloatData,
        'CHAR': getCharData
    }
    
    # Calls function to display the start of project
    projectStart()

    # Get user data
    tenant, day, month, year, usageFees = getDataInput(monthList, inFunc)

    # Get Calculated Totals
    daysLate, monthlyRent, lateFees, totalDue = calcTotals(day, usageFees)

    # Call Display Func
    displaySummary(day, month, year, tenant, daysLate, monthlyRent, usageFees, lateFees, totalDue)

    # Calls function to display the end of project
    projectEnd()
      


main() # calling the function main()