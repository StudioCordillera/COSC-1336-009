
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|/////////////////////////////#
#////////////////////| EMPLOYEE | CLASS |\\\\\\\\\\\\\\\\\\\\\#
#______________/////////////////|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
class Employee:            

    def __init__(self, last:str, first:str, dependents:int, wage:float, ssn:int, initials:str, email:str, l4ssn:int, eID:str):

        # User Provided
        self.last = last
        self.first = first
        self.__dependents = dependents
        self.__wage = wage
        self.__ssn = ssn

        # Derived
        self.initials = initials
        self.email = email
        self.__l4ssn = l4ssn
        self.__eID = eID

        
    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<< METHODS | ACCESSORS >>>>>>>>>>>>>>>>>>#
    #///////////////////////////|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

    # User Provided
    def set_first(self, first):
        self.first = first
    def set_last(self, last):
        self.last = last
    def set_dependents(self, dependents):
        self.__dependents = dependents
    def set_wage(self, wage):
        self.__wage = wage
    def set_ssn(self, ssn):
        self.__ssn = ssn

    # Derived
    def set_initials(self, initials):
        self.initials = initials
    def set_email(self, email):
        self.email = email
    def set_l4ssn(self, l4ssn):
        self.__l4ssn = l4ssn
    def set_eID(self, eID):
        self.__eID = eID

    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<| METHODS | MUTATORS |>>>>>>>>>>>>>>>>>>#
    #///////////////////////////|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

    # Todo Return formatted versions for SSN, and wage when retrieved


    def get_first(self):
        return self.first
    def get_last(self):
        return self.last
    def get_dependents(self):
        return self.__dependents
    def get_wage(self):
        return self.__wage
    def get_ssn(self):
        return self.__ssn
    def get_initials(self):
        return self.initials
    def get_l4ssn(self):
        return self.__l4ssn
    def get_eID(self):
        return self.__eID
    

    
    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<| METHODS | OPERATORS |>>>>>>>>>>>>>>>>>#
    #///////////////////////////|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

    
    def get_variable(self, variable):
        pass
        

#_______________________________________________________________#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#///////////////////////////////////////////////////////////////#
