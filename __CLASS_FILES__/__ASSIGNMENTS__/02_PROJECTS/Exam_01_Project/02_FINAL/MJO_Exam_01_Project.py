###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 12, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
from MyClasses import displayLabels, typeValidation
ExamOne=displayLabels.Context(1, '12/12/2025','AllyBaba House Rental', 'Late Payment Calculator')
END, START = ExamOne.END, ExamOne.START
nL, tab, tab1, lineGraph, shortBar, medBar, dashGraph = displayLabels.nL, displayLabels.tab, displayLabels.tab1, displayLabels.lineGraph, displayLabels.shortBar, displayLabels.medBar, displayLabels.dashGraph
v=V=typeValidation.validateInput
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   REQUIREMENTS - EXAM #1 PROJECT (Rent Calculator)          |
|_____________________________________________________________|
|                                                             |
|  OBJECTIVE:                                                 |
|    - Calculate monthly rent with late fees                  |
|    - Property: 2200 sq ft, 3 bed, 2 bath                    |
|    - Monthly rent: $2500 + usage fees                       |
|                                                             |
|  LATE FEE RULES (30-day month):                             |
|    - Days 1-3: No late fee                                  |
|    - Days 4-30: $10 per day after day 3                     |
|    - After day 30: Flat $2000 fee                           |
|                                                             |
|  INPUT:                                                     |
|    - Tenant name                                            |
|    - Month and year                                         |
|    - Day paid                                               |
|    - Usage fees                                             |
|                                                             |
|  OUTPUT:                                                    |
|    - Rental summary with all charges                        |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def calculateLateFee(day):
    if day <= 3:
        return 0, 0
    elif day <= 30:
        daysLate = day - 3
        return daysLate, daysLate * 10
    else:
        return 30, 2000

def main(): 
    START()
    
    print(f"{tab}AllyBaba House Rental Information{nL}")
    print(f"{tab}---- Input Section ------")
    
    tenantName = v(str, f"{tab}Name of tenant: ").strip().title()
    month = v(str, f"{tab}Enter the month: ").strip().title()
    
    while True:
        day = v(int, f"{tab}Enter day of the month:   ")
        if day < 1:
            print(f"{tab}Day must be at least 1!")
        else:
            break
    
    while True:
        usageFees = float(v(int, f"{tab}Enter usage fees: "))
        if usageFees < 0:
            print(f"{tab}Usage fees cannot be negative!")
        else:
            break
    
    monthlyRent = 2500.00
    daysLate, lateFee = calculateLateFee(day)
    totalDue = monthlyRent + usageFees + lateFee
    
    print(f"{nL+tab}Rental Summary")
    print(f"{tab}--- Rental Transaction for the month of {month} 2025 ------")
    print(f"{tab}Name of tenant{tab+tab+tab}{tenantName}")
    print(f"{tab}Day the rent is paid{tab+tab}{day}{nL}")
    print(f"{tab}Days Late{tab+tab+tab}{daysLate} days{nL}")
    print(f"{tab}Monthly rent{tab+tab+tab}${monthlyRent:.2f}")
    print(f"{tab}Usage fees{tab+tab+tab}${usageFees:.2f}")
    
    if day > 30:
        print(f"{tab}Late fees charges (onetime ){tab}${lateFee:.2f}")
    else:
        print(f"{tab}Late fees charges ($10/day){tab}${lateFee:.2f}")
    
    print(f"{nL+tab}Total Due for {month} 2025{tab+tab}${totalDue:.2f}")
    
    END()
      
main()