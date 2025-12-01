# Python OOP Term Definitions Dictionary

## Overview
Comprehensive definitions for every term in the Python OOP model, organized alphabetically within categories.

---

## A

### argument
The actual value passed to a function/method when calling it.
```python
def greet(name):    # name is parameter
    print(name)
greet("Alice")      # "Alice" is argument
```

### attribute
A name bound to a value, accessed via dot notation (`obj.attr`).
**Location**: Class namespace or instance namespace
**Example**: `person.name`, `Car.wheels`

### attribute value
The specific data currently stored in an attribute.
```python
obj.x = 10  # 10 is the attribute value
```

---

## B

### behavior
General term for the actions an object or class can perform.
**Context**: Instance behavior (via instance methods), class-level behavior (via class/static methods)

### bound method
A method that has been bound to a specific instance, automatically passing `self` when called.
```python
class Counter:
    def increment(self): pass

c = Counter()
m = c.increment  # m is a bound method
m()              # calls increment with c as self
```

---

## C

### call signature
The definition specifying how a function/method can be invoked (parameters, return type).
```python
def process(data: str, mode: int = 1) -> bool:  # This is the call signature
    pass
```

### callable attribute
An attribute that can be called (functions, methods).
**Examples**: Methods, functions defined in class body

### callable view
Another term for bound method; a method bound to an instance ready to call.

### class
The blueprint/template defining structure and behavior for creating objects.
```python
class Person:  # Person is a class
    pass
```

### class attribute
Any attribute stored in the class namespace, accessible via the class or its instances.
```python
class Dog:
    species = "Canis familiaris"  # class attribute
```

### class body
The indented code block within a class definition.
```python
class Example:
    # This entire indented section is the class body
    x = 10
    def method(self):
        pass
```

### class definition
The source code block defining a class (from `class` keyword to end of body).

### class method
A method decorated with `@classmethod` that receives the class as first argument (`cls`).
```python
class Account:
    @classmethod
    def from_dict(cls, data):  # class method
        return cls(**data)
```

### class method definition
The `def` statement creating a class method (with `@classmethod` decorator).

### class name
The identifier given to a class.
```python
class MyClass:  # "MyClass" is the class name
    pass
```

### class namespace
The dictionary-like structure (`__dict__`) storing a class's attributes and methods.
```python
class Example:
    x = 10

print(Example.__dict__)  # class namespace
```

### class object
The class as a runtime object that can be assigned, passed, and inspected.
```python
MyClass = Person  # Person as class object
```

### class type
The metatype of a class, usually `type`.
```python
class Person: pass
print(type(Person))  # <class 'type'>
```

### class variable
A mutable data attribute stored at class level, shared across all instances.
```python
class Counter:
    count = 0  # class variable
```

### class-level behavior
Actions performed via class methods or static methods.

### cls
Conventional first parameter name for class methods, referring to the class itself.
```python
@classmethod
def create(cls):  # cls refers to the class
    return cls()
```

### constructor
The `__new__` method responsible for creating new instances.
```python
class Custom:
    def __new__(cls):
        instance = super().__new__(cls)
        return instance
```

---

## D

### data attribute (on class)
Non-callable class attributes (typically variables or constants).

### data attribute (on instance)
Non-callable instance attributes (instance variables).

### default parameter value
The fallback value assigned to optional parameters.
```python
def connect(host, port=80):  # 80 is default parameter value
    pass
```

### descriptor
An object defining `__get__`, `__set__`, and/or `__delete__` to control attribute access.
```python
class Descriptor:
    def __get__(self, obj, objtype=None):
        return "value"
    
class MyClass:
    attr = Descriptor()  # descriptor
```

### descriptor attribute
An attribute following the descriptor protocol.

### dunder methods
Methods with double underscores (e.g., `__init__`, `__str__`) implementing Python's data model protocols.
```python
class Book:
    def __init__(self, title):  # dunder method
        self.title = title
    def __str__(self):          # dunder method
        return self.title
```

---

## F

### field
Generally synonymous with "attribute" or "instance variable," referring to data stored in a class or instance.
```python
class Point:
    def __init__(self, x, y):
        self.x = x  # field (instance variable)
        self.y = y  # field (instance variable)
```

### function
A callable object defined with `def` or `lambda`.

### function defined in class body
Any function defined within a class definition block.
```python
class Example:
    def method(self):  # function defined in class body
        pass
```

### function object
A function as a first-class value that can be assigned and passed.
```python
def greet(): pass
f = greet  # f holds function object
```

---

## G

### global variable
A variable defined at module scope, accessible throughout the module.
```python
GLOBAL_VAR = 100  # global variable

def function():
    print(GLOBAL_VAR)
```

---

## I

### identity
The unique identifier of an object (returned by `id(obj)`), determining if references point to same object.
```python
x = [1, 2]
y = x
print(id(x) == id(y))  # True, same identity
```

### initializer
The `__init__` method that sets up initial state when an instance is created.
```python
class Person:
    def __init__(self, name):  # initializer
        self.name = name
```

### instance
An object created from a class; has the "is an instance of" relationship with its class.
```python
class Dog: pass
buddy = Dog()  # buddy is an instance
```

### instance attribute
An attribute stored in an instance's namespace (`__dict__`), unique to that instance.
```python
class Person:
    def __init__(self, name):
        self.name = name  # instance attribute

p = Person("Alice")
```

### instance behavior
Actions an instance can perform via its methods, determined by class definition and instance state.

### instance method
A method operating on instance data, receiving `self` as first parameter.
```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):  # instance method
        self.count += 1
```

### instance method definition
The `def` statement in a class body defining an instance method (with `self`).

### instance namespace
The dictionary-like structure (`__dict__`) storing an instance's attributes.
```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Bob")
print(p.__dict__)  # {'name': 'Bob'} - instance namespace
```

### instance object
The instance as a runtime entity.

### instance variable
Mutable data unique to each instance; synonymous with instance attribute.

### instance-of
The relationship between an object and its class, tested with `isinstance()`.
```python
class Dog: pass
d = Dog()
print(isinstance(d, Dog))  # True, d is instance-of Dog
```

---

## L

### local variable
A variable defined within a function scope.
```python
def example():
    x = 10  # local variable
```

---

## M

### method
A function defined in a class, designed to operate on class or instance data.

### method parameter
The parameters defined in a method's signature.
```python
class Calculator:
    def add(self, a, b):  # a and b are method parameters
        return a + b
```

### module
A file containing Python code, providing a namespace for organization.

### module-level function
A function defined at the top level of a module (not in a class).
```python
def helper():  # module-level function
    pass
```

---

## N

### namespace
A mapping from names to objects, typically implemented as a dictionary.
**Types**: module namespace, class namespace, instance namespace

### nonlocal variable
A variable from an enclosing function scope, accessed via `nonlocal` keyword.
```python
def outer():
    x = 10
    def inner():
        nonlocal x  # refers to x in outer scope
        x += 1
```

---

## O

### object
Any value in Python; everything is an object with identity, type, and value.
```python
x = 42      # integer object
s = "hello" # string object
class C: pass
c = C()     # instance object
```

### object state
The complete collection of all attribute values defining an object's current condition.
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# A Point's state is determined by x and y values
```

---

## P

### parameter
A variable in a function/method definition.
```python
def greet(name):  # name is a parameter
    print(name)
```

### property
A descriptor providing getter, setter, and deleter access to an attribute with custom logic.
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def fahrenheit(self):  # property
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
```

---

## R

### runtime behavior
The actual execution of methods during program execution.

### runtime entity
Something that exists during program execution (objects, instances).

---

## S

### self
The conventional first parameter name for instance methods, referring to the instance itself.
```python
class Person:
    def __init__(self, name):
        self.name = name  # self refers to the instance
```

### self reference
The binding of `self` to the current instance in method calls.

### slot
Pre-declared attribute using `__slots__` for memory optimization.
```python
class Point:
    __slots__ = ['x', 'y']  # only these attributes allowed
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### special attribute
Attributes with special meaning in Python (dunders, descriptors).

### special method
Methods implementing Python's data model protocols (dunder methods).

### state
See "object state"

### static method
A utility function in class namespace that doesn't receive `self` or `cls`.
```python
class Math:
    @staticmethod
    def add(a, b):  # static method
        return a + b
```

### static method definition
The `def` statement creating a static method (with `@staticmethod` decorator).

### stored value
The actual data persisted in memory for an attribute.

---

## T

### type
The class an object is an instance of, determining its behavior and structure.
```python
class Person: pass
p = Person()
print(type(p))  # <class '__main__.Person'>
```

---

## V

### value
The data content of an object or attribute.

### value set
The complete collection of values at a point in time; synonymous with state.

### variable
A name bound to a value in a specific scope.
**Types**: local, nonlocal, global, class variable, instance variable

---

## TERM-TO-CONCEPT MAPPING

| Term | Concept Layer | Code Location | Access Pattern |
|------|---------------|---------------|----------------|
| class | Core Entity | Source code | `class Name:` |
| instance | Core Entity | Runtime | `obj = Class()` |
| class attribute | Data Storage | Class `__dict__` | `Class.attr` |
| instance attribute | Data Storage | Instance `__dict__` | `obj.attr` |
| instance method | Behavior Definition | Class body | `def method(self):` |
| bound method | Behavior Access | Runtime | `obj.method` |
| property | Computed Attribute | Class body | `@property` |
| descriptor | Access Protocol | Class body | `__get__/__set__/__delete__` |
| namespace | Organization | `__dict__` | `.dict__` |
| dunder method | Special Protocol | Class body | `__method__` |

---

## CONCEPTUAL RELATIONSHIPS

```
CLASS DEFINITION
    ├─ creates → CLASS OBJECT
    │   ├─ has → CLASS NAMESPACE
    │   │   ├─ contains → CLASS ATTRIBUTES
    │   │   └─ contains → METHOD DEFINITIONS
    │   └─ has → CLASS TYPE (usually 'type')
    │
    └─ used to create → INSTANCES
        ├─ have → INSTANCE NAMESPACE
        │   └─ contains → INSTANCE ATTRIBUTES
        ├─ have → IDENTITY (id())
        ├─ have → TYPE (the class)
        ├─ have → STATE (all attribute values)
        └─ access methods as → BOUND METHODS
```

---

## QUICK LOOKUP: TERM DISAMBIGUATION

**When you see "attribute":**
- On class? → class attribute
- On instance? → instance attribute
- Is it a property/descriptor? → special attribute
- Is it callable? → method

**When you see "method":**
- Has `self`? → instance method
- Has `cls`? → class method  
- Has neither? → static method
- Has double underscores? → dunder method (special method)

**When you see "variable":**
- In function? → local variable
- In enclosing function? → nonlocal variable
- In module? → global variable
- On class? → class variable
- On instance? → instance variable (usually just called instance attribute)

**When you see "namespace":**
- `Class.__dict__`? → class namespace
- `instance.__dict__`? → instance namespace
- Module? → module namespace

