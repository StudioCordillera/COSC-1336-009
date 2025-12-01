# Python OOP Term Hierarchy

## Overview
This document organizes all Python OOP terms into a clear conceptual hierarchy, showing relationships between concepts and eliminating redundancy.

---

## 1. CORE ENTITIES

### class
The fundamental blueprint for creating objects.

- **class object** - The class as a first-class runtime entity
- **class type** - The metatype of a class (usually `type`)
- **class definition** - The source code block defining the class
  - **class body** - The indented code block within the class definition
  - **class name** - The identifier given to the class

### object
Any value in Python; the base of everything.

- **instance** - An object created from a class
  - **instance object** - The instance as a runtime entity

### module
A file containing Python code; provides a namespace for organization.

---

## 2. IDENTITY & TYPING

### identity
The unique ID of an object (`id(obj)`), determining if two references point to the same object.

### type
The class an object is an instance of, determining its behavior and structure.

### instance-of
The relationship between an object and its class (tested with `isinstance()`).

---

## 3. NAMESPACES

### namespace
A mapping from names to objects (typically a dictionary).

- **class namespace** - The namespace holding a class's attributes (`Class.__dict__`)
- **instance namespace** - The namespace holding an instance's attributes (`instance.__dict__`)

---

## 4. ATTRIBUTES & VARIABLES

### attribute
A name bound to a value, accessed via dot notation.

#### Class-level attributes

- **class attribute** - Any attribute stored in the class namespace
  - **class variable** - Mutable data stored at class level, shared across instances
  - **data attribute (on class)** - Non-callable class attributes

#### Instance-level attributes

- **instance attribute** - Attribute stored in an instance's namespace
  - **instance variable** - Mutable data unique to each instance
  - **data attribute (on instance)** - Non-callable instance attributes

#### Special attribute types

- **property** - A descriptor providing computed attribute access
  - **descriptor** - An object defining `__get__`, `__set__`, and/or `__delete__`
- **slot** - Pre-declared attributes using `__slots__` (memory optimization)

### variable
A name bound to a value in a specific scope.

- **local variable** - Variable within a function scope
- **nonlocal variable** - Variable from enclosing function scope
- **global variable** - Variable in module scope
- **field** - Synonymous with "attribute" in data context (often instance variable)

---

## 5. VALUES & STATE

### value
The data content of an object or attribute.

- **attribute value** - The specific data stored in an attribute
- **stored value** - The actual data persisted in memory
- **default parameter value** - The fallback value for optional parameters

### state
The collective values defining an object's condition.

- **object state** - All attribute values comprising an object's current data
- **value set** - The complete collection of values at a point in time

---

## 6. CALLABLES & METHODS

### function
A callable object defined with `def` or `lambda`.

- **function object** - A function as a first-class value
- **module-level function** - Function defined at module scope
- **function defined in class body** - Any function defined within a class

#### method
A function designed to operate on class or instance data.

##### Instance methods
- **instance method** - Method operating on instance state
  - **instance method definition** - The `def` statement in class body with `self`

##### Class methods
- **class method** - Method operating on class-level data
  - **class method definition** - Method decorated with `@classmethod`, receives `cls`

##### Static methods
- **static method** - Utility function in class namespace
  - **static method definition** - Method decorated with `@staticmethod`

##### Special methods
- **special method** - Methods implementing Python protocols
  - **dunder methods** - Methods with double underscores (e.g., `__init__`)
  - **constructor** - The `__new__` method creating instances
  - **initializer** - The `__init__` method setting initial state

#### Behavior categories
- **behavior** - General term for what an object/class can do
- **class-level behavior** - Actions performed via class methods or static methods
- **instance behavior** - Actions performed via instance methods

### bound method
A method connected to a specific instance.

- **callable view** - A method bound to an instance, ready to call
- **runtime behavior** - The actual execution of instance methods

---

## 7. CALL INTERFACE & PARAMETERS

### call signature
The definition of how a function/method can be called.

- **parameter** - A variable in the function definition
  - **method parameter** - Parameters in a method signature
- **argument** - The actual value passed when calling
- **default parameter value** - Optional parameter with fallback value

### self
The conventional first parameter of instance methods, referring to the instance.

- **self reference** - The binding of `self` to the current instance

### cls
The conventional first parameter of class methods, referring to the class.

---

## 8. CLASSIFICATION & CATEGORIES

These are descriptive labels used to categorize concepts:

- **runtime entity** - Something that exists during program execution
- **callable attribute** - An attribute that can be called (functions, methods)
- **special attribute** - Attributes with special meaning (dunders, descriptors)
- **descriptor attribute** - Attributes following the descriptor protocol

---

## TERM RELATIONSHIP DIAGRAM

```
Python Object Model
│
├── STRUCTURAL
│   ├── class (blueprint)
│   ├── object (runtime entity)
│   └── module (container)
│
├── ORGANIZATIONAL
│   ├── namespace (name→object mapping)
│   │   ├── class namespace
│   │   └── instance namespace
│   │
│   └── identity & type (object metadata)
│
├── DATA STORAGE
│   ├── attributes (named values)
│   │   ├── class attribute
│   │   └── instance attribute
│   │
│   └── state (value collections)
│
└── BEHAVIOR
    ├── functions (definitions)
    │   ├── module-level
    │   └── in class body → methods
    │       ├── instance method
    │       ├── class method
    │       ├── static method
    │       └── special method (dunder)
    │
    └── bound methods (runtime callables)
```

---

## SIMPLIFIED MAPPING

### When defining a class:
```python
class MyClass:              # class definition, creates class object
    class_var = 10          # class attribute (class variable)
    
    def __init__(self):     # instance method definition (dunder method)
        self.x = 5          # creates instance attribute
    
    def method(self):       # instance method definition
        pass
    
    @classmethod
    def cls_method(cls):    # class method definition
        pass
    
    @staticmethod
    def static():           # static method definition
        pass
    
    @property
    def computed(self):     # property (descriptor)
        return self.x * 2
```

### When creating an instance:
```python
obj = MyClass()             # obj is instance (object)
obj.method()                # obj.method is bound method
print(obj.x)                # obj.x accesses instance attribute
print(obj.computed)         # property getter called
```

### Namespace locations:
- `MyClass.__dict__` contains: `class_var`, `method`, `cls_method`, `static`, `computed`
- `obj.__dict__` contains: `x`

---

## KEY DISTINCTIONS

### Attribute vs Variable
- **Attribute**: Name accessed via dot notation (`obj.attr`)
- **Variable**: Name in a scope (local, global, nonlocal)
- Instance attributes are stored as entries in the instance's `__dict__`

### Method Definition vs Bound Method
- **Method definition**: Function in class body (stored in class namespace)
- **Bound method**: Runtime object connecting method to instance

### Class Attribute vs Instance Attribute
- **Class attribute**: In `Class.__dict__`, shared by all instances
- **Instance attribute**: In `instance.__dict__`, unique per instance

### State vs Value
- **Value**: A single piece of data
- **State**: The complete set of all values in an object

### Descriptor vs Property
- **Descriptor**: Protocol (`__get__`, `__set__`, `__delete__`)
- **Property**: Built-in descriptor implementation

---

## CONSOLIDATED SYNONYM GROUPS

For clarity, these terms are essentially synonymous:

1. **Data storage on instance**:
   - instance attribute
   - instance variable
   - field (in data context)

2. **Data storage on class**:
   - class attribute
   - class variable

3. **Runtime callable**:
   - bound method
   - callable view

4. **Function in class**:
   - method (when appropriate context)
   - function defined in class body

---

## USAGE RECOMMENDATION

When writing or discussing Python OOP:

- Use **class attribute** for any attribute on the class
- Use **instance attribute** for any attribute on an instance
- Use **method** with qualifiers: *instance method*, *class method*, *static method*
- Use **bound method** when referring to the runtime callable
- Use **property** for computed attributes
- Use **descriptor** when discussing the protocol itself
- Reserve **field** and **slot** for specific contexts (data classes, `__slots__`)

