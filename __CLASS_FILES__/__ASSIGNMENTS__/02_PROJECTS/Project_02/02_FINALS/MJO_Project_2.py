########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Project: 02                     #####
## Status: IN PROGRESS             #####s
## Class: COSC 1336                #####
###############################################################
## Project 1 Objectives | Movie Ticket Revenue Calc          ##
###############################################################

# This function will display the start of the project
def projectStart():
    print('-' * 60)
    print('   Start of Project 2')
    print('-' * 60)
    print('\tDistribution of revenues for a Movie Theatre')
    print('-' * 60 + '\n')
    print('\tWritten by: Matthew Ochoa')
    print('\tDate: 11/03/2025\n')

# This function will display the start of the project
def projectEnd():
    print('\n' + '-' * 50)
    print('   End of Project 2')
    print('-' * 50 + '\n')

# This function will return an integer input from the user
def getIntegerData(prompt):
    value = int(input(prompt))
    return value

# This function will return a float input from the user
def getFloatData(prompt):
    value = float(input(prompt))
    return value

# This function will return a string input from the user
def getStringData(prompt):
    value = input(prompt)
    return value


###############################################################
##    My Code Below                                          ##
###############################################################

# Calc Revenue Func
def getCalcRevenue(childTickets, adultTickets, seniorTickets):

    gross = childTickets + adultTickets + seniorTickets
    theatre = gross * .8
    distro = gross * .2

    return gross, theatre, distro


# Summary Display Func
def displaySummary(totalTicketsSold, movieName, gross, theatre, distro):
    print('\n\t' + '-' * 50)
    print('\tSummary: Movie Income Distrobution')
    print('\t' + '-' * 50)
    print('\tMovie Name: ', movieName)
    print('\tTotal tickets sold: ', totalTicketsSold)
    print('\tGross revenue: $', format(gross, ',.2f'), '\n')
    print('\n\tTheatre keeps: $', format(theatre, ',.2f'))
    print('\tDistributor recieves: $', format(distro, ',.2f'))


###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 

    # Calls function to display the start of project
    projectStart()

    print('\t' + '-' * 50)
    print('\tBox Offic Entry')
    print('\t' + '-' * 50)

    # PROMPT user for name of the movie
    #  ------------------------------------------------------------------------
    movieName = getStringData('\tName of movie: ')

    # number of tickets sold for Children, Adults, and Seniors
    #  ------------------------------------------------------------------------
    #   Children = $6.00
    childTickets = getIntegerData('\tEnter number of Child tickets sold: ')

    #   Adults = $10.00
    adultTickets = getIntegerData('\tEnter number of Adult tickets sold: ')

    #   Seniors = $8.00
    seniorTickets = getIntegerData('\tEnter number of Senior tickets sold: ')
    
    # Get the # of total tickets sold 
    totalTicketsSold = childTickets + adultTickets + seniorTickets

    # Convert ticket vars to price equivelants
    childTickets = float(childTickets * 6)
    adultTickets = float(adultTickets * 10)
    seniorTickets = float(seniorTickets * 8)

    # Run calculations
    gross, theatre, distro = getCalcRevenue(childTickets, adultTickets, seniorTickets)

    # Display Summary
    displaySummary(totalTicketsSold, movieName, gross, theatre, distro)

    # Calls function to display the start of project
    projectEnd()

main() # calling the function main()