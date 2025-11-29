#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\|/////////////////////////////#
#////////////////////| EMPLOYEE | CLASS |\\\\\\\\\\\\\\\\\\\\\#
#______________/////////////////|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
class Employee:                 
    def __init__(self, last, first, dependents, wage, SSN):
        self.__last = str(last)
        self.__first = str(first)
        self.__dependents = 0
        self.__wage = 0
        self.__SSN = 000000000

        
    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<< METHODS | ACCESSORS >>>>>>>>>>>>>>>>>>#
    #///////////////////////////|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

    def set_first(self, first):
        self.__name = self.__first
    def set_last(self, last):
        self.__name = self.__last
    def set_dependents(self, dependents):
        self.__name = self.__dependents
    def set_wage(self, wage):
        self.__name = self.__wage
    def set_SSN(self, SSN):
        self.__name = self.__SSN

    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<| METHODS | MUTATORS |>>>>>>>>>>>>>>>>>>#
    #///////////////////////////|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

    def get_first(self):
        return self.__first
    def get_last(self):
        return self.__last
    def get_dependents(self):
        return self.__dependents
    def get_wage(self):
        return self.__wage
    def get_SSN(self):
        return self.__SSN
    
    #_________________________________________________________#
    #<<<<<<<<<<<<<<<<<| METHODS | OPERATORS |>>>>>>>>>>>>>>>>>#
    #///////////////////////////|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
    #                                                         #
    #   State Management | Menu Iteration | Saving | Loadng   #
    #_________________________________________________________#



#_______________________________________________________________#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#///////////////////////////////////////////////////////////////#
