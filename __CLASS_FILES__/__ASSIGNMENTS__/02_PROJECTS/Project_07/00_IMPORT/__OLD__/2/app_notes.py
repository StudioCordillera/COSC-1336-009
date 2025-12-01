'''
__________________________________________________________________

    ______________________________
    | OPP - COFIG/MAP | UML SPEC | 
    |        ** INFORMAL **      |
    ------------------------------

    | CLASS DEF |
    ------------------------------

        | __DUNDERS__ |

        def __init__(isRunning):
            appMain() -> None


    | DATA ATTRIBUTES |
    ------------------------------
        - Employee Registry object (dict)
        - Running (bool)


    | METHODS |
    ------------------------------
    appMain():
        mainMenu()
    
    
        
    ------------------------------

__________________________________________________________________

| OPP - IMPORTS |

| OPP - ## |

| OPP - ## |

| OPP - ## |

__________________________________________________________________



> Start program

    > Main Menu

        Choose an option:

        	r. Register New Employee
        	m. Manage Employees Collection
        	c. Change Company Settings
        	e. exit

    > option r. New Employee
        > 1. Get input

            Provide First Name:
            	~

            Provide Last Name:
            	~

            Provide # of Dependents for Employee: (0-10)
            	~

            Provide SSN of Employee:
            	~

            Provide Employee Wage:
            	~

        > 1.1 Check input

            Provided Employee Info: (enter # to change)

            	1. First Name: ~
            	2.  Last Name: ~
            	3. Dependents: ~
            	4. 	  SSN: ~
            	5. 	 Wage: ~

            Choose Option:

            	#. Change selected item
            	a. Change all items
            	f. Finalize Employee In-Take
            	c. Cancel New Employee Registration

        > 1.2 Finalize Employee In-Take

            Employee Info
        
                Initials
                Last, First
                SSN
                Dependents
                Wage

                1. Email
                2. eID

            Choose Option:

            	#. Manually edit fields
            	f. Finalize Employee
            	c. Cancel Registration
        
    > Option m. Manage Employee Collection

        > 2 Show list of Employees

            Company Name | Domain.com
            _____________________________
            eID | Employee
            ...

        Provide an eID to manage an employee: (or c to cancel)
            ~

        > 2.1 Edit employee | eID provided

            Choose an option:

            	e. Edit Employee Info
            	a. Archive Employee
            	d. Delete Employee
            	c. Cancel


            > 2.2 Option e. Edit Employee info

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

            > 2.2 Option a. Archive Employee

                Are you sure you want to ARCHIVE eID: lName, fName?

                	y. Yes, archive employee
                	c. Cancel

            > 2.3 Option d. Delete Employee

                Are you sure you want to DELETE eID: lName, fName?

                	y. Yes, delete employee
                	c. Cancel

    > Option c. Change company info

        > Company Info Menu

            1. Company Name
            2. Domain

            Choose an option:

            	#. edit item
            	c. Cancel

    > Option 3.1 Change Company Name

        Insert new company name:
        	~
    
        Company Name will be changed from (old name) to (new name).
    
        Choose an option:
    
        	a. Apply changes
        	e. Edit New Company Name
        	c. Cancel

    > Option 3.2 Change Company Domain

        Insert new Domain:
        	~

    > Option 3.2 [case 1: domain extension not recognized OR format issues]

        Company Domain will be changed from (old domain) to (new domain).

        Warning: Domain extension not recognized.
        {and/or} : Warning: Format does not match standard (domain.com) format.

        Choose an option:

        	a. Apply Changes
        	e. Edit New Domain
        	c. Cancel

    > Option 3.2 [case 2: domain extension recognized, no format issues]

        Company Domain will be changed from (old domain) to (new domain).

        Choose an option:

        	a. Apply Changes
        	e. Edit New Domain
        	c. Cancel



'''

'''
All menus have 2 common behaviors

Field Menu:

example: ('~' = user input | (before 'enter'))

Provide your first name:
    ~

> INPUTS | 1) single line prompt | 2) returns input






'''
