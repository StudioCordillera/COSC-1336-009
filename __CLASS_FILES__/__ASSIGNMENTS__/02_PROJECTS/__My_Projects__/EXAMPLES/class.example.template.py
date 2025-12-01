"""
Python Class Template - Complete Documentation & Reference

This template demonstrates all essential OOP concepts in Python without
thematic context. Use this as a reference for understanding class structure,
methods, attributes, and inheritance patterns.

Concepts covered:
    - Class vs Instance attributes
    - Constructor (__init__)
    - Instance methods, Class methods, Static methods
    - Special/Magic methods (dunder methods)
    - Property decorators (getters/setters)
    - Inheritance and method overriding
    - Encapsulation (public, protected, private)
"""


# ==============================================================================
# BASIC CLASS STRUCTURE
# ==============================================================================

class ExampleClass:
    """
    Main class demonstrating core OOP concepts.
    
    Docstring is accessible via ExampleClass.__doc__
    Best practice: Always document class purpose and usage.
    """
    
    # --------------------------------------------------------------------------
    # CLASS ATTRIBUTES (Shared by ALL instances)
    # --------------------------------------------------------------------------
    
    class_attribute = "Shared by all instances"
    instance_count = 0
    valid_options = ['option1', 'option2', 'option3']
    
    
    # --------------------------------------------------------------------------
    # CONSTRUCTOR (Runs automatically when object is created)
    # --------------------------------------------------------------------------
    
    def __init__(self, param1, param2, param3='default'):
        """
        Initialize a new instance.
        
        Args:
            param1: First parameter description
            param2: Second parameter description
            param3: Optional parameter with default value
        
        'self' refers to the specific instance being created.
        """
        # PUBLIC instance attributes (accessible from anywhere)
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        
        # PROTECTED attribute (convention: single underscore)
        # Indicates internal use, but still technically accessible
        self._internal_id = ExampleClass.instance_count + 1
        
        # PRIVATE attribute (double underscore causes name mangling)
        # Python renames to _ClassName__attribute_name
        self.__private_value = 0.0
        
        # Instance-specific list (each object has its own copy)
        self.item_list = []
        
        # Update class-level counter
        ExampleClass.instance_count += 1
    
    
    # --------------------------------------------------------------------------
    # INSTANCE METHODS (Operate on specific object instances)
    # --------------------------------------------------------------------------
    
    def instance_method(self, value):
        """
        Instance method has access to instance data via 'self'.
        Can read and modify instance attributes.
        """
        self.item_list.append(value)
        return f"Added {value} to list"
    
    def get_summary(self):
        """Return formatted information about this instance."""
        return (f"Param1: {self.param1}, Param2: {self.param2}, "
                f"ID: {self._internal_id}")
    
    def calculate_value(self):
        """Calculate and store a value based on instance data."""
        # Example calculation logic
        self.__private_value = len(self.item_list) * 10
        return self.__private_value
    
    
    # --------------------------------------------------------------------------
    # PROPERTY DECORATORS (Controlled attribute access)
    # --------------------------------------------------------------------------
    
    @property
    def private_value(self):
        """
        Getter: Access private attribute like a regular attribute.
        Usage: obj.private_value (no parentheses)
        """
        return self.__private_value
    
    @private_value.setter
    def private_value(self, value):
        """
        Setter: Validate before setting value.
        Usage: obj.private_value = new_value
        """
        if value >= 0:
            self.__private_value = value
        else:
            raise ValueError("Value must be non-negative")
    
    @property
    def computed_property(self):
        """
        Computed property: No backing attribute, calculated on access.
        Useful for derived values.
        """
        return self.__private_value > 50
    
    
    # --------------------------------------------------------------------------
    # CLASS METHODS (Operate on the class itself, not instances)
    # --------------------------------------------------------------------------
    
    @classmethod
    def get_class_info(cls):
        """
        Class method accesses class-level data via 'cls'.
        Can read/modify class attributes.
        Cannot access instance attributes.
        """
        return f"{cls.__name__} has {cls.instance_count} instances"
    
    @classmethod
    def modify_class_attribute(cls, new_value):
        """Modify class attribute - affects ALL instances."""
        cls.class_attribute = new_value
    
    @classmethod
    def alternative_constructor(cls, data_string):
        """
        Factory method: Alternative way to create instances.
        Usage: obj = ExampleClass.alternative_constructor("data1,data2,data3")
        """
        param1, param2, param3 = data_string.split(',')
        return cls(param1, param2, param3)
    
    
    # --------------------------------------------------------------------------
    # STATIC METHODS (Utility functions, no access to class or instance)
    # --------------------------------------------------------------------------
    
    @staticmethod
    def validate_input(value):
        """
        Static method: Pure utility function.
        No access to 'self' or 'cls'.
        Related to class concept but doesn't need class/instance data.
        """
        return value in ExampleClass.valid_options
    
    @staticmethod
    def utility_function(input_data):
        """Generic utility related to class functionality."""
        # Example: data transformation, validation, etc.
        return input_data.upper() if isinstance(input_data, str) else input_data
    
    
    # --------------------------------------------------------------------------
    # SPECIAL/MAGIC METHODS (Customize object behavior)
    # --------------------------------------------------------------------------
    
    def __str__(self):
        """
        Informal string representation for end users.
        Called by: print(obj), str(obj)
        """
        return f"ExampleClass({self.param1}, {self.param2})"
    
    def __repr__(self):
        """
        Formal string representation for developers.
        Should ideally be valid Python code to recreate object.
        Called by: repr(obj), or typing object name in console
        """
        return f"ExampleClass('{self.param1}', '{self.param2}', '{self.param3}')"
    
    def __eq__(self, other):
        """
        Define equality comparison.
        Called by: obj1 == obj2
        """
        if not isinstance(other, ExampleClass):
            return False
        return (self.param1 == other.param1 and 
                self.param2 == other.param2)
    
    def __lt__(self, other):
        """
        Define less-than comparison (enables sorting).
        Called by: obj1 < obj2, sorted([objects])
        """
        return self.param1 < other.param1
    
    def __len__(self):
        """
        Define length behavior.
        Called by: len(obj)
        """
        return len(self.item_list)
    
    def __getitem__(self, index):
        """
        Enable indexing and iteration.
        Called by: obj[index]
        Makes object subscriptable.
        """
        return self.item_list[index]
    
    def __setitem__(self, index, value):
        """
        Enable item assignment.
        Called by: obj[index] = value
        """
        self.item_list[index] = value
    
    def __contains__(self, item):
        """
        Enable membership testing.
        Called by: item in obj
        """
        return item in self.item_list
    
    def __del__(self):
        """
        Destructor: Called when object is garbage collected.
        Use carefully - timing is unpredictable!
        """
        ExampleClass.instance_count -= 1


# ==============================================================================
# INHERITANCE (Extending existing classes)
# ==============================================================================

class ChildClass(ExampleClass):
    """
    Inherits all attributes and methods from ExampleClass (parent/base class).
    Can add new functionality and override existing methods.
    """
    
    def __init__(self, param1, param2, param3, child_param):
        """
        Initialize child class.
        Must call parent constructor to initialize inherited attributes.
        """
        # Call parent class constructor
        super().__init__(param1, param2, param3)
        
        # Add child-specific attributes
        self.child_param = child_param
        self.child_attribute = True
    
    def get_summary(self):
        """
        METHOD OVERRIDING: Replace parent's implementation.
        Can still access parent version using super()
        """
        parent_summary = super().get_summary()
        return f"{parent_summary}, Child Param: {self.child_param}"
    
    def child_specific_method(self):
        """New method only available in child class."""
        return f"Child-specific functionality: {self.child_param}"


# ==============================================================================
# USAGE EXAMPLES
# ==============================================================================

def demonstrate_basic_usage():
    """Examples showing how to use the class."""
    
    print("=" * 70)
    print("CLASS USAGE DEMONSTRATION")
    print("=" * 70)
    
    # Creating instances
    print("\n[1] Creating Instances:")
    obj1 = ExampleClass("value1", "value2", "value3")
    obj2 = ExampleClass("valueA", "valueB")  # Uses default param3
    obj3 = ExampleClass.alternative_constructor("x,y,z")
    
    print(f"Object 1: {obj1}")
    print(f"Object 2: {obj2}")
    print(f"Object 3: {obj3}")
    
    # Class vs Instance attributes
    print("\n[2] Class vs Instance Attributes:")
    print(f"Class attribute (shared): {ExampleClass.class_attribute}")
    print(f"Instance count: {ExampleClass.instance_count}")
    print(f"Object 1 param1: {obj1.param1}")
    print(f"Object 2 param1: {obj2.param1}")
    
    # Instance methods
    print("\n[3] Instance Methods:")
    print(obj1.instance_method("item1"))
    print(obj1.instance_method("item2"))
    print(f"Object 1 items: {obj1.item_list}")
    print(f"Object 2 items: {obj2.item_list}")
    
    # Properties
    print("\n[4] Property Access:")
    obj1.calculate_value()
    print(f"Private value (via property): {obj1.private_value}")
    print(f"Computed property: {obj1.computed_property}")
    
    # Class methods
    print("\n[5] Class Methods:")
    print(ExampleClass.get_class_info())
    
    # Static methods
    print("\n[6] Static Methods:")
    print(f"Is 'option1' valid? {ExampleClass.validate_input('option1')}")
    print(f"Is 'invalid' valid? {ExampleClass.validate_input('invalid')}")
    
    # Magic methods
    print("\n[7] Magic Methods:")
    print(f"String representation: {str(obj1)}")
    print(f"Developer representation: {repr(obj1)}")
    print(f"Length: {len(obj1)}")
    print(f"Equality: obj1 == obj2? {obj1 == obj2}")
    
    # Inheritance
    print("\n[8] Inheritance:")
    child = ChildClass("p1", "p2", "p3", "child_value")
    print(f"Child object: {child}")
    print(f"Overridden method: {child.get_summary()}")
    print(f"Child-specific: {child.child_specific_method()}")
    print(f"Inherited method: {child.instance_method('inherited')}")
    
    print("\n" + "=" * 70)


# ==============================================================================
# QUICK REFERENCE
# ==============================================================================

"""
SYNTAX QUICK REFERENCE:

CLASS DEFINITION:
    class ClassName:
        class_attribute = value
        
        def __init__(self, param):
            self.instance_attribute = param

METHOD TYPES:
    def instance_method(self, param):       # Access instance data
    
    @classmethod
    def class_method(cls, param):           # Access class data
    
    @staticmethod
    def static_method(param):               # No instance/class access

PROPERTIES:
    @property
    def attribute_name(self):               # Getter
        return self._value
    
    @attribute_name.setter
    def attribute_name(self, value):        # Setter
        self._value = value

INHERITANCE:
    class Child(Parent):
        def __init__(self, param):
            super().__init__(parent_param)
            self.child_attr = param

COMMON MAGIC METHODS:
    __init__(self, ...)         # Constructor
    __str__(self)               # Informal string (print)
    __repr__(self)              # Formal representation
    __eq__(self, other)         # Equality (==)
    __lt__(self, other)         # Less than (<)
    __len__(self)               # Length
    __getitem__(self, key)      # Indexing ([])
    __setitem__(self, key, val) # Assignment ([]=)
    __contains__(self, item)    # Membership (in)
    __del__(self)               # Destructor

ENCAPSULATION:
    self.public                 # No restriction
    self._protected             # Internal use (convention)
    self.__private              # Name mangling

BEST PRACTICES:
    ✓ Use PascalCase for class names
    ✓ Write docstrings for classes and methods
    ✓ Initialize all instance attributes in __init__
    ✓ Use properties for controlled access
    ✓ Keep methods focused and single-purpose
    ✓ Use @classmethod for alternative constructors
    ✓ Use @staticmethod for class-related utilities
"""


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    demonstrate_basic_usage()
