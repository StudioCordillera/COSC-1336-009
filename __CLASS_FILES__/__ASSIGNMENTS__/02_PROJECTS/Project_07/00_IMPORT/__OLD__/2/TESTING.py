import os

def clearTerminal():
    os.system('cls')














def validate(userInput, vType, choices, items):
    pass
    

def valSSN(userInput):
    pass


def main():
    items = ['Initials', 'Last', 'First','SSN','Dependents', 'Wage', 'Email', 'eID']
    prompt = '\tChoose an option:'
    vType = 'items'
    options = ['Manually Edit Fields','Finalize Employee', 'Cancel']

    itemsOptionsMenu(prompt, vType, options, items)



main()

'''

1. Initials
2. Last
3. First
4. SSN
5. Dependents
6. Wage
7. Email
8. eID
Choose Option:
	#. Manually edit fields
	a. Finalize Employee
	c. Cancel Employee Edit

'''

#    clearTerminal()
#    print('\n\t\tNot a valid option!\n\t\tPress \'enter\'')
#    input()
#    clearTerminal()