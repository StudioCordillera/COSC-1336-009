# Python OOP Domain Terms Reference

## Overview
This document defines the membership terms in the domains of **Class** and **Object** in Python's Object-Oriented Programming model.

---

## CLASS DOMAIN

### Identity & Namespace

#### class (type)
The blueprint or template that defines the structure and behavior for creating objects. A class is itself an object of type `type`.

```python
class Person:  # Person is a class
    pass

print(type(Person))  # <class 'type'>
```

#### class object (type instance)
The class as a runtime object that can be referenced, passed around, and inspected. When you define a class, Python creates a class object.

```python
MyClass = Person  # class object can be assigned to variables
print(MyClass)    # <class '__main__.Person'>
```

#### class namespace (namespace)
The dictionary-like structure (`__dict__`) that stores the class's attributes, methods, and other members.

```python
class Example:
    class_var = 42
    
print(Example.__dict__)  # Shows class namespace
```

---

### Data in Class

#### class attribute (class namespace)
Any name bound in the class namespace, accessible via the class itself.

```python
class Counter:
    count = 0  # class attribute
    
print(Counter.count)  # Access class attribute
```

#### class variable (class namespace)
A mutable data attribute stored in the class namespace, shared across all instances.

```python
class BankAccount:
    interest_rate = 0.03  # class variable shared by all accounts
```

---

### Behavior on Class

#### function defined in class body (callable attribute)
Any function defined within the class definition block, stored in the class namespace.

```python
class Calculator:
    def add(self, a, b):  # function defined in class body
        return a + b
```

#### method (callable attribute)
A function defined in a class that operates on instances or the class itself. Context determines if it's an instance, class, or static method.

#### instance method definition (callable attribute)
A function defined in the class body with `self` as the first parameter, intended to operate on instance data.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def describe(self):  # instance method definition
        return f"This is a {self.brand}"
```

#### class method definition (callable attribute)
A method decorated with `@classmethod` that receives the class (`cls`) as the first argument, operating on class-level data.

```python
class Employee:
    company = "TechCorp"
    
    @classmethod
    def get_company(cls):  # class method definition
        return cls.company
```

#### static method definition (callable attribute)
A method decorated with `@staticmethod` that doesn't receive `self` or `cls`, functioning as a utility within the class namespace.

```python
class MathUtils:
    @staticmethod
    def add(a, b):  # static method definition
        return a + b
```

---

### Special Protocol

#### dunder methods (special attribute)
Methods with double underscores (e.g., `__init__`, `__str__`) that implement Python's data model protocols.

```python
class Book:
    def __init__(self, title):  # dunder method
        self.title = title
    
    def __str__(self):  # dunder method
        return f"Book: {self.title}"
```

#### property (descriptor attribute)
A descriptor that provides getter, setter, and deleter access to an attribute with custom logic.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def fahrenheit(self):  # property
        return self._celsius * 9/5 + 32
```

#### descriptor (descriptor attribute)
An object defining `__get__`, `__set__`, or `__delete__` that controls attribute access.

```python
class Descriptor:
    def __get__(self, obj, objtype=None):
        return "descriptor value"
    
class MyClass:
    attr = Descriptor()  # descriptor
```

---

### Interface

#### method parameter (call signature)
The parameters defined in a method's signature that determine how it can be called.

```python
class Greeter:
    def greet(self, name, greeting="Hello"):  # name and greeting are parameters
        return f"{greeting}, {name}!"
```

#### default parameter value (call signature)
A default value assigned to a parameter, making it optional in the call.

```python
def connect(self, host, port=80):  # 80 is default parameter value
    pass
```

---

## OBJECT DOMAIN

### Identity & Relation

#### object (runtime entity)
Any value in Python; everything is an object with identity, type, and value.

```python
x = 42          # x references an integer object
s = "hello"     # s references a string object
```

#### instance (instance-of)
A specific object created from a class, having the relationship "is an instance of" that class.

```python
class Dog:
    pass

buddy = Dog()  # buddy is an instance of Dog
print(isinstance(buddy, Dog))  # True
```

---

### Data on Object

#### instance attribute (instance namespace)
An attribute stored in an individual object's namespace (`__dict__`), unique to that instance.

```python
class Person:
    def __init__(self, name):
        self.name = name  # instance attribute

p1 = Person("Alice")
p2 = Person("Bob")
print(p1.name)  # "Alice" - unique to p1
```

#### instance variable (instance namespace)
Synonymous with instance attribute; a variable stored on an instance.

#### attribute value (stored value)
The actual data stored in an attribute at a given point in time.

```python
person.age = 30  # 30 is the attribute value
```

#### object state (value set)
The complete collection of all attribute values that define an object's current condition.

```python
class Point:
    def __init__(self, x, y):
        self.x = x  # part of object state
        self.y = y  # part of object state
```

---

### Behavior via Object

#### bound method (callable view)
A method that has been bound to a specific instance, automatically passing `self`.

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

c = Counter()
method = c.increment  # bound method
method()  # calls increment with c as self
```

#### instance behavior (runtime behavior)
The actions an instance can perform through its methods, determined by both the class definition and instance state.

---

### Self Reference

#### `self` (call signature)
The conventional name for the first parameter in instance methods, referring to the instance itself.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width    # self refers to the instance being created
        self.height = height
    
    def area(self):
        return self.width * self.height  # self accesses instance data
```

---

## Usage Notes

### Class vs Instance Attributes
```python
class Example:
    class_attr = "shared"  # Class attribute
    
    def __init__(self):
        self.instance_attr = "unique"  # Instance attribute

e1 = Example()
e2 = Example()

print(e1.class_attr)     # "shared" (accessed via instance)
print(Example.class_attr)  # "shared" (accessed via class)
print(e1.instance_attr)  # "unique" to e1
```

### Method Types Summary
- **Instance Method**: Takes `self`, operates on instance data
- **Class Method**: Takes `cls`, operates on class-level data
- **Static Method**: Takes neither, utility function in class namespace

### Attribute Lookup Order (MRO)
1. Instance `__dict__`
2. Class `__dict__`
3. Parent class `__dict__` (following MRO)
4. Raises `AttributeError` if not found

---

## Quick Reference

| Term | Domain | Location | Purpose |
|------|--------|----------|---------|
| class attribute | Class | Class namespace | Shared data/behavior |
| instance attribute | Object | Instance namespace | Per-object data |
| instance method | Class | Class namespace | Instance behavior definition |
| bound method | Object | Runtime | Instance behavior access |
| property | Class | Class namespace | Computed attributes |
| `self` | Both | Method signature | Instance reference |

