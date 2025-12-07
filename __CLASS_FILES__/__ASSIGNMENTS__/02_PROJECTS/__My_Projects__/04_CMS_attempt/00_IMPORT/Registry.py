from typing import Dict
from EmployeeClass import Employee



class RegistryHolder(type):

    REGISTRY: Dict[str, "RegistryHolder"] = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        """
            Here the name of the class is used as key but it could be any class
            parameter.
        """
        # Only register subclasses, not the base class itself
        if name != 'BaseRegisteredClass':
            cls.REGISTRY[new_cls.__name__] = new_cls
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


class BaseRegisteredClass(metaclass=RegistryHolder):
    """
    Any class that will inherits from BaseRegisteredClass will be included
    inside the dict RegistryHolder.REGISTRY, the key being the name of the
    class and the associated value, the class itself.
    """


class RegisteredEmployee(BaseRegisteredClass, Employee):
    """  
    >>> def getVars(test):
    ... 
    ...     print (test)"""

    def __init__(self, last='Smith', first='Jeff', dependents=0, wage=10.00, ssn=111223456):
        self.last = last
        self.first = first
        self.dependents = dependents
        self.wage = wage
        self.ssn = ssn
        self.l4ssn = str(self.ssn)[-4:]
        self.eID = f"{self.last}.{self.l4ssn}"
        self.email = f"{first[1]}{last}@example.com"


    


def main():
    """
    Before subclassing
    >>> sorted(RegistryHolder.REGISTRY)
    ['BaseRegisteredClass']

    >>> class ClassRegistree(BaseRegisteredClass):
    ...    def __init__(self, *args, **kwargs):
    ...        pass

    After subclassing
    >>> sorted(RegistryHolder.REGISTRY)
    ['BaseRegisteredClass', 'ClassRegistree']
    """
    # Classes inherit from BaseRegisteredClass and auto-register
    class Manager(BaseRegisteredClass):
        pass
    
    class Developer(BaseRegisteredClass):
        pass
    
    # Look up class by name and instantiate
    ManagerClass = RegistryHolder.REGISTRY['Manager']
    manager = ManagerClass()


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    main()

