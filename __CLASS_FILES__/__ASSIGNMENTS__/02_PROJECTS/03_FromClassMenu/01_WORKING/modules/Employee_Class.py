class Employee:
    '''Stores Item instance State | serves item standards'''
    def __init__(self, last:str = 'Last', first:str = 'First', dependents:int = 0, wage:float = 0.00, ssn:str = '123456789'):
        # Instance Attributes
        self.last = last
        self.first = first
        self.__dependents = dependents
        self.__wage = wage
        self.__ssn = ssn
   
        # Derived Instance Attributes
        self.initials, self.email, self.__l4ssn, self.__eID  = self.derived_vars(last, first, ssn)
       

    
    def derived_vars(self, last, first, ssn):
        """Company Provided - Derived Employee Variables"""

        initials = (f"{first[:1]}{last[:1]}").upper()
        self.initials = initials

        email = (f"{initials[:1]}{last}@example.com").lower() # TODO | REPLACE DOMAIN WITH VAL FROM COLLECTIONS
        self.email = email

        l4ssn = ssn[-4:]
        self.__l4ssn = l4ssn
        
        eID = (f"{last}.{l4ssn}").lower()
        self.__eID = eID


        return self.initials, self.email, self.__l4ssn, self.__eID
    
    @property
    def dependents(self):
        return self.__dependents
    @property
    def wage(self):
        return self.__wage
    @property
    def ssn(self):
        return self.__ssn

    @dependents.setter
    def dependents(self, value):
        if value >=0:
            if value <=10:
                self.__dependents = value
            else:
                raise ValueError("Value must be maximum 10")

        else:
            raise ValueError("Value must be non-negative")

    @wage.setter
    def wage(self, value):
        if value >0:
            self.__wage = float((f"{value:.2f}"))
        else:
            raise ValueError("Value must be greater than 0")

    @ssn.setter
    def ssn(self, value):
        if len(value) != 9 and len(value) !=11:
            raise ValueError("Value must be formatted in xxxxxxxxx or xxx-xx-xxxx format")
        elif len(value) == 9 and str(value).isnumeric() == True:
            self.__ssn = value
        elif len(value) == 11:
            if value[3] == '-' and value[6] == '-':
                self.__ssn = value
            else:
                raise ValueError("Check \'-\' Placement...")
        else:
            raise ValueError("Not formatted correctly")
            







'''
Input-driven (stored)
~~~~~~~~~~~~~~~~~~~~~
- first: str
  - stored as lowercase
  - validated: non-empty, alphabetical (simple check)

- last: str
  - stored as lowercase
  - validated: non-empty, alphabetical

- dependents: int
  - validated range: 0-10 inclusive

- wage: int
  - stored as integer (e.g. 20)
  - formatted for display as: f"${wage}"

- ssn: str (canonical internal storage)
  - internal canonical form: "xxxxxxxxx" (9 digits, no dashes)
  - accepted input forms:
    - "xxxxxxxxx" (all digits)
    - "xxx-xx-xxxx" (with dashes)
  - repository / helper normalizes to canonical string or raises if invalid
  - formatted for display as: "xxx-xx-xxxx"


Derived / computed (not stored)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- initials: str
  - (f"{first[:1]}{last[:1]}").upper()  -> "FL"

- email: str
  - domain is provided by repository (`repo.get_domain()`)
  - f"{first}{last}@{domain}"

- ssn_last4: str
  - ssn[-4:]

- employee_id (eID): str
  - f"{last}.{ssn_last4}"
  - used to identify/select employees in menus
'''