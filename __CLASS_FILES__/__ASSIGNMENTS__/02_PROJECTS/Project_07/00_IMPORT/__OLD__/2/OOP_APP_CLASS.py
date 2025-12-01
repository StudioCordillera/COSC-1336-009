import os
import OOP_EMPLOYEE_CLASS


def clearTerminal():
    os.system('cls')


class App:
    def __init__(self):
        # Employee storage
        self.__employees = {}  # Dictionary: eID -> Employee object
        self.__current_employee = None  # For employee being registered
        
        # Company settings
        self.company_name = "Company Name"
        self.company_domain = "example.com"
        
        # Field configurations for employee registration
        self.employee_fields = {
            'first': {
                'prompt': '\tProvide First Name: ',
                'setter': 'set_first',
                'getter': 'get_first',
                'type': 'text'
            },
            'last': {
                'prompt': '\tProvide Last Name: ',
                'setter': 'set_last',
                'getter': 'get_last',
                'type': 'text'
            },
            'dependents': {
                'prompt': '\tProvide # of Dependents (0-10): ',
                'setter': 'set_dependents',
                'getter': 'get_dependents',
                'type': 'number'
            },
            'ssn': {
                'prompt': '\tProvide Employee SSN: ',
                'setter': 'set_ssn',
                'getter': 'get_ssn',
                'type': 'ssn'
            },
            'wage': {
                'prompt': '\tProvide Employee Wage: ',
                'setter': 'set_wage',
                'getter': 'get_wage',
                'type': 'number'
            }
        }

    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<< MAIN APPLICATION FLOW >>>>>>>>>>>>>>>>#
    #_________________________________________________________#

    def run(self):
        """Main application loop"""
        running = True
        while running:
            clearTerminal()
            choice = self.show_main_menu()
            
            if choice == 'r':
                self.register_employee_flow()
            elif choice == 'm':
                self.manage_employees_flow()
            elif choice == 'c':
                self.change_settings_flow()
            elif choice == 'e':
                running = False
                print('\n\tExiting...\n')

    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<< EMPLOYEE REGISTRATION >>>>>>>>>>>>>>>>#
    #_________________________________________________________#

    def register_employee_flow(self):
        """Complete flow for registering a new employee"""
        clearTerminal()
        print('\n\t=== REGISTER NEW EMPLOYEE ===\n')
        
        # Step 1: Collect employee data
        employee_data = self.collect_employee_data()
        if employee_data is None:  # User cancelled
            return
        
        # Step 2: Confirm data
        confirmed = self.confirm_employee_data(employee_data)
        if not confirmed:
            return
        
        # Step 3: Create employee object with derived fields
        self.create_employee(employee_data)
        
        print('\n\tEmployee successfully registered!\n')
        input('\tPress Enter to continue...')

    def collect_employee_data(self):
        """Collect all employee data from user"""
        data = {}
        
        for field, config in self.employee_fields.items():
            while True:
                print(config['prompt'])
                value = input('\t')
                
                # Basic validation (you can expand this)
                if value.strip():
                    data[field] = value
                    break
                else:
                    print('\n\tValue cannot be empty. Try again.\n')
        
        return data

    def confirm_employee_data(self, data):
        """Show data and allow user to confirm or edit"""
        while True:
            clearTerminal()
            print('\n\t=== CONFIRM EMPLOYEE INFO ===\n')
            print('\tProvided Employee Info:\n')
            
            # Display all fields with numbers
            fields = list(data.keys())
            for i, field in enumerate(fields, 1):
                display_name = field.replace('_', ' ').title()
                print(f'\t{i}. {display_name}: {data[field]}')
            
            print('\n\tChoose an option:\n')
            print('\t\t#. Change selected item (1-5)')
            print('\t\ta. Change all items')
            print('\t\tf. Finalize employee')
            print('\t\tc. Cancel registration')
            
            choice = input('\n\t').lower().strip()
            
            if choice == 'f':
                return True
            elif choice == 'c':
                return False
            elif choice == 'a':
                data = self.collect_employee_data()
            elif choice.isdigit() and 1 <= int(choice) <= len(fields):
                # Edit specific field
                field = fields[int(choice) - 1]
                config = self.employee_fields[field]
                print(f'\n{config["prompt"]}')
                new_value = input('\t')
                if new_value.strip():
                    data[field] = new_value

    def create_employee(self, data):
        """Create Employee object with derived fields"""
        # Generate derived fields
        initials = data['first'][0].upper() + data['last'][0].upper()
        email = f"{data['first'].lower()}{data['last'][0].lower()}@{self.company_domain}"
        l4ssn = int(data['ssn'][-4:])
        eID = f"{data['last'].lower()}{l4ssn}"
        
        # Create employee object
        employee = OOP_EMPLOYEE_CLASS.Employee(
            last=data['last'],
            first=data['first'],
            dependents=int(data['dependents']),
            wage=float(data['wage']),
            ssn=int(data['ssn']),
            initials=initials,
            email=email,
            l4ssn=l4ssn,
            eID=eID
        )
        
        # Store in employees dictionary
        self.__employees[eID] = employee

    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<< EMPLOYEE MANAGEMENT >>>>>>>>>>>>>>>>>>#
    #_________________________________________________________#

    def manage_employees_flow(self):
        """Manage existing employees"""
        clearTerminal()
        
        if not self.__employees:
            print('\n\tNo employees registered yet.\n')
            input('\tPress Enter to continue...')
            return
        
        # Show list of employees
        print(f'\n\t{self.company_name} | {self.company_domain}')
        print('\t' + '='*40 + '\n')
        print('\teID\t\t| Employee')
        print('\t' + '-'*40)
        
        for eID, emp in self.__employees.items():
            print(f'\t{eID}\t\t| {emp.get_last()}, {emp.get_first()}')
        
        print('\n\tProvide an eID to manage (or \'c\' to cancel): ')
        choice = input('\t').strip()
        
        if choice == 'c':
            return
        
        if choice in self.__employees:
            self.manage_single_employee(choice)
        else:
            print('\n\tInvalid eID.\n')
            input('\tPress Enter to continue...')

    def manage_single_employee(self, eID):
        """Manage a specific employee"""
        employee = self.__employees[eID]
        
        while True:
            clearTerminal()
            print(f'\n\t=== MANAGE EMPLOYEE: {employee.get_last()}, {employee.get_first()} ===\n')
            print('\tChoose an option:\n')
            print('\t\te. Edit Employee Info')
            print('\t\ta. Archive Employee')
            print('\t\td. Delete Employee')
            print('\t\tc. Cancel')
            
            choice = input('\n\t').lower().strip()
            
            if choice == 'e':
                self.edit_employee(employee)
            elif choice == 'a':
                print('\n\t(Archive functionality not yet implemented)')
                input('\tPress Enter to continue...')
            elif choice == 'd':
                if self.confirm_delete(eID):
                    del self.__employees[eID]
                    print('\n\tEmployee deleted.\n')
                    input('\tPress Enter to continue...')
                    return
            elif choice == 'c':
                return

    def edit_employee(self, employee):
        """Edit employee information"""
        clearTerminal()
        print('\n\t=== EDIT EMPLOYEE ===\n')
        print('\t(Edit functionality not yet implemented)')
        input('\tPress Enter to continue...')

    def confirm_delete(self, eID):
        """Confirm employee deletion"""
        employee = self.__employees[eID]
        print(f'\n\tAre you sure you want to DELETE {eID}: {employee.get_last()}, {employee.get_first()}?')
        print('\n\t\ty. Yes, delete employee')
        print('\t\tc. Cancel')
        
        choice = input('\n\t').lower().strip()
        return choice == 'y'

    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<< SETTINGS MANAGEMENT >>>>>>>>>>>>>>>>>>#
    #_________________________________________________________#

    def change_settings_flow(self):
        """Change company settings"""
        clearTerminal()
        print('\n\t=== COMPANY SETTINGS ===\n')
        print(f'\t1. Company Name: {self.company_name}')
        print(f'\t2. Domain: {self.company_domain}')
        print('\n\tChoose an option (# to edit, c to cancel): ')
        
        choice = input('\t').strip()
        
        if choice == '1':
            print('\n\tEnter new company name: ')
            new_name = input('\t')
            if new_name.strip():
                self.company_name = new_name
                print('\n\tCompany name updated!')
        elif choice == '2':
            print('\n\tEnter new domain: ')
            new_domain = input('\t')
            if new_domain.strip():
                self.company_domain = new_domain
                print('\n\tDomain updated!')
        
        if choice in ['1', '2']:
            input('\n\tPress Enter to continue...')

    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<<<<<< MENU HELPERS >>>>>>>>>>>>>>>>>>>>>#
    #_________________________________________________________#

    def show_main_menu(self):
        """Display main menu and get user choice"""
        print('\n\t=== MAIN MENU ===\n')
        print('\tChoose an option:\n')
        print('\t\tr. Register New Employee')
        print('\t\tm. Manage Employees Collection')
        print('\t\tc. Change Company Settings')
        print('\t\te. Exit')
        
        return input('\n\t').lower().strip()

    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<< UTILITY METHODS >>>>>>>>>>>>>>>>>>>>>>#
    #_________________________________________________________#
    
    def get_employees(self):
        """Return all employees"""
        return self.__employees


#_________________________________________________________#
#<<<<<<<<<<<<<<<<<<<< RUN APPLICATION >>>>>>>>>>>>>>>>>>>>#
#_________________________________________________________#

if __name__ == '__main__':
    app = App()
    app.run()