# Display Start of Program Boiler SOPB
#  ------------------------------------------------------------------------
def projectStart():
    print(' ' * 4, '-'* 80, '\n',' ' * 4, 'Start of Project 4')
    print(' ' * 5, 'Written by: Matthew Ochoa')
    print(' ' * 5,'Date: 11/25/2025 ')
    print(' ' * 4,'-' * 80)
    print('\t  PROGRAM NAME | PURPOSE')
    print(' ' * 4,'-' * 80, '\n')

# Display End of Program Boiler EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print(' ' * 4,'-' * 80, '\n')
    print( ' ' * 5, 'End of Project')
    print(' ' * 4,'-' * 80)    

# example of 80 '-' dashes with a 76 count after a tab
projectStart()
print(f'\t  User\'s Entry\n\t','-' * 76)
print('\n\t  PROGRAM STUFF HERE\n')
print('\n\t\t  ERRORS SPACING\n')
projectEnd()



import os
#--------------------------------
clear = lambda: os.system('cls')
clear()


# OR



'''
import os
def clear():
    os.system('cls')
clear()
'''

