###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   November 3, 2025    |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|   REQUIREMENTS - Project 02                                |
|   Objectives: Movie Theater Revenue Distribution           |
|____________________________________________________________|

INPUTS (User Provided):
    - Movie name (string)
    - Number of child tickets sold (integer)
    - Number of adult tickets sold (integer) 
    - Number of senior tickets sold (integer)

PROCESSING:
    - Convert ticket quantities to revenue amounts:
      * Child tickets: $6.00 each
      * Adult tickets: $10.00 each
      * Senior tickets: $8.00 each
    - Calculate total tickets sold (sum of all types)
    - Calculate gross box office revenue (sum of all ticket revenue)
    - Calculate theater's share: 80% of gross
    - Calculate distributor's share: 20% of gross

DISPLAY:
    - Movie name
    - Total tickets sold
    - Gross box office revenue
    - Amount theater keeps (80%)
    - Amount distributor receives (20%)

FUNCTIONS:
    - projectStart(): Display program header and information
    - projectEnd(): Display program completion message
    - getIntegerData(prompt): Get integer input from user
    - getFloatData(prompt): Get float input from user
    - getStringData(prompt): Get string input from user
    - getCalcRevenue(): Calculate gross, theater share, distributor share
    - displaySummary(): Display formatted revenue distribution report
    - main(): Program orchestration and flow control

STATIC VARIABLES (Constants):
    - Child ticket price: $6.00
    - Adult ticket price: $10.00
    - Senior ticket price: $8.00
    - Theater percentage: 80% (0.8)
    - Distributor percentage: 20% (0.2)

______________________________________________________________
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#   SOPB
#  ------------------------------------------------------------------------
def projectStart():
    print('-' * 60)
    print('   Start of Project 2')
    print('-' * 60)
    print('\tDistribution of revenues for a Movie Theatre')
    print('-' * 60 + '\n')
    print('\tWritten by: Matthew Ochoa')
    print('\tDate: 11/03/2025\n')

    


#   EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print('\n' + '-' * 50)
    print('   End of Project 2')
    print('-' * 50 + '\n')


#   Get Integer Input
#  ------------------------------------------------------------------------
def getIntegerData(prompt):
    value = int(input(prompt))  # Get integer from user <
    return value                # Return to caller >


#   Get Float Input
#  ------------------------------------------------------------------------
def getFloatData(prompt):
    value = float(input(prompt))  # Get float from user <
    return value                  # Return to caller >


#   Get String Input
#  ------------------------------------------------------------------------
def getStringData(prompt):
    value = input(prompt)  # Get string from user <
    return value           # Return to caller >


#   Calculate Revenue Distribution
#  ------------------------------------------------------------------------
def getCalcRevenue(childTickets, adultTickets, seniorTickets):
    # Calculate gross box office revenue
    gross = childTickets + adultTickets + seniorTickets  # Sum all ticket revenue |
    
    # Calculate theater and distributor shares
    theatre = gross * .8   # Theater keeps 80% |
    distro = gross * .2    # Distributor gets 20% |
    
    return gross, theatre, distro  # Return all calculations >


#   Display Revenue Summary
#  ------------------------------------------------------------------------
def displaySummary(totalTicketsSold, movieName, gross, theatre, distro):
    print('\n\t' + '-' * 50)
    print('\tSummary: Movie Income Distrobution')
    print('\t' + '-' * 50)
    print('\tMovie Name: ', movieName)
    print('\tTotal tickets sold: ', totalTicketsSold)
    print('\tGross revenue: $', format(gross, ',.2f'), '\n')
    print('\n\tTheatre keeps: $', format(theatre, ',.2f'))
    print('\tDistributor recieves: $', format(distro, ',.2f'))


#   MAIN FUNCTION - Program Orchestration
#  ------------------------------------------------------------------------
def main(): 
    # Display program start
    projectStart()

    # Box office data entry header
    print('\t' + '-' * 50)
    print('\tBox Offic Entry')
    print('\t' + '-' * 50)

    # Get movie information
    movieName = getStringData('\tName of movie: ')  # <

    # Get ticket sales by category
    #   Children = $6.00
    childTickets = getIntegerData('\tEnter number of Child tickets sold: ')  # <
    
    #   Adults = $10.00
    adultTickets = getIntegerData('\tEnter number of Adult tickets sold: ')  # <
    
    #   Seniors = $8.00
    seniorTickets = getIntegerData('\tEnter number of Senior tickets sold: ')  # <
    
    # Calculate total tickets sold
    totalTicketsSold = childTickets + adultTickets + seniorTickets  # |
    
    # Convert ticket quantities to revenue amounts
    childTickets = float(childTickets * 6)    # Convert to $ value |
    adultTickets = float(adultTickets * 10)   # Convert to $ value |
    seniorTickets = float(seniorTickets * 8)  # Convert to $ value |
    
    # Calculate revenue distribution
    gross, theatre, distro = getCalcRevenue(childTickets, adultTickets, seniorTickets)  # <
    
    # Display revenue summary
    displaySummary(totalTicketsSold, movieName, gross, theatre, distro)  # >
    
    # Display program end
    projectEnd()


#   PROGRAM ENTRY POINT
#  ------------------------------------------------------------------------
main()