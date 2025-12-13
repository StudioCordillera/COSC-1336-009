# ABC_MODULE

## Core Definition
**ABC (Abstract Base Classes)** module provides infrastructure for defining abstract base classes in Python. It enforces interface contracts by requiring subclasses to implement specific methods, ensuring consistent APIs across related classes.

**Tags**: #abc #abstract #interface #oop #inheritance #metaclass

---

## COMPLETE ABC MODULE QUICK REFERENCE

### ABC MODULE - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# CORE ABC CLASSES
# ═══════════════════════════════════════════════════════════════════════════
ABC                          # Base class | Inherit for ABC support | Returns ABC base class
ABCMeta                      # Metaclass | Manual metaclass specification | Returns metaclass for ABCs
abc.get_cache_token()        # None | Get current cache token | Returns int cache invalidation token

# ═══════════════════════════════════════════════════════════════════════════
# DECORATORS FOR ABSTRACT MEMBERS
# ═══════════════════════════════════════════════════════════════════════════
@abstractmethod              # Method | Mark as abstract (must override) | Raises TypeError if not implemented
@abstractclassmethod         # Class method (deprecated) | Mark abstract classmethod | Use @classmethod + @abstractmethod
@abstractstaticmethod        # Static method (deprecated) | Mark abstract staticmethod | Use @staticmethod + @abstractmethod
@abstractproperty            # Property (deprecated) | Mark abstract property | Use @property + @abstractmethod

# ═══════════════════════════════════════════════════════════════════════════
# VIRTUAL SUBCLASS REGISTRATION
# ═══════════════════════════════════════════════════════════════════════════
ABCMeta.register(subclass)   # ABC + class | Register virtual subclass | Returns registered subclass
@ABC.register                # Decorator | Register as virtual subclass | Returns decorated class

# ═══════════════════════════════════════════════════════════════════════════
# SUBCLASS CHECKING METHODS
# ═══════════════════════════════════════════════════════════════════════════
issubclass(C, ABC)           # Class + ABC | Check if subclass | Returns True/False
isinstance(obj, ABC)         # Object + ABC | Check if instance | Returns True/False
ABCMeta.__subclasshook__(C)  # Class | Custom subclass check | Returns True/False/NotImplemented

# ═══════════════════════════════════════════════════════════════════════════
# ABSTRACT METHOD COMBINATIONS
# ═══════════════════════════════════════════════════════════════════════════
@property + @abstractmethod  # Property | Abstract property getter | Must implement in subclass
@setter + @abstractmethod    # Property | Abstract property setter | Must implement in subclass
@deleter + @abstractmethod   # Property | Abstract property deleter | Must implement in subclass
@classmethod + @abstractmethod # Class method | Abstract classmethod | Must implement in subclass
@staticmethod + @abstractmethod # Static method | Abstract staticmethod | Must implement in subclass

# ═══════════════════════════════════════════════════════════════════════════
# INSPECTION AND INTROSPECTION
# ═══════════════════════════════════════════════════════════════════════════
ABC.__abstractmethods__      # ABC class | Get abstract method names | Returns frozenset of method names
hasattr(cls, '__abstractmethods__') # Class | Check if has abstract methods | Returns True/False
len(cls.__abstractmethods__) # ABC class | Count abstract methods | Returns int count
inspect.isabstract(cls)      # Class | Check if abstract (has abstract methods) | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# METACLASS OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════
class MyABC(metaclass=ABCMeta) # Explicit metaclass | Create ABC with metaclass | Returns ABC class
type.__subclasses__(ABC)     # ABC | Get direct subclasses | Returns list of subclasses
ABC._abc_registry            # ABC | Access virtual subclass registry | Returns WeakSet of registered classes
ABC._abc_cache               # ABC | Access instance cache | Returns WeakSet of cached instances
ABC._abc_negative_cache      # ABC | Access negative cache | Returns WeakSet of negative cache
ABC._abc_negative_cache_version # ABC | Get negative cache version | Returns int version number

# ═══════════════════════════════════════════════════════════════════════════
# UPDATE AND INVALIDATION (Python 3.7+)
# ═══════════════════════════════════════════════════════════════════════════
abc.update_abstractmethods(cls) # ABC class | Recalculate abstract methods | Returns None (modifies class)
abc.get_cache_token()        # None | Get cache invalidation token | Returns int token for cache management
```

### COMMON OPERATION EXAMPLES

```python
from abc import ABC, abstractmethod

# Basic abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Concrete implementation
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# This works
rect = Rectangle(5, 3)
print(rect.area())           # → 15

# This fails (missing implementations)
# shape = Shape()            # TypeError: Can't instantiate abstract class

# Virtual subclass registration
class MyList(list):
    pass

Shape.register(MyList)       # Register as virtual subclass
print(issubclass(MyList, Shape))  # → True
```

---

## DETAILED ABC OPERATIONS

### 1. CREATING ABSTRACT BASE CLASSES

```python
from abc import ABC, abstractmethod

# Method 1: Inherit from ABC (recommended, Python 3.4+)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """All animals must make a sound"""
        pass
    
    @abstractmethod
    def move(self):
        """All animals must be able to move"""
        pass

# Method 2: Explicit metaclass (older style)
from abc import ABCMeta

class Vehicle(metaclass=ABCMeta):
    @abstractmethod
    def start_engine(self):
        pass

# Method 3: Inheritance from explicit metaclass
class LandVehicle(Vehicle):
    @abstractmethod
    def drive(self):
        pass
```

### 2. ABSTRACT METHOD PATTERNS

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    # Basic abstract method
    @abstractmethod
    def process(self, data):
        """Process data (must implement)"""
        pass
    
    # Abstract method with default implementation
    @abstractmethod
    def validate(self, data):
        """Validate data with default behavior"""
        if not data:
            raise ValueError("Data cannot be empty")
        return True
    
    # Concrete method (not abstract)
    def log(self, message):
        """Logging is optional to override"""
        print(f"[LOG] {message}")

# Subclass can call super() for abstract methods with defaults
class CSVProcessor(DataProcessor):
    def process(self, data):
        return data.split(',')
    
    def validate(self, data):
        # Call parent's validation first
        super().validate(data)
        # Add additional validation
        return ',' in data
```

### 3. ABSTRACT PROPERTIES

```python
from abc import ABC, abstractmethod

class Person(ABC):
    # Abstract property (getter)
    @property
    @abstractmethod
    def name(self):
        """Person must have a name"""
        pass
    
    # Abstract property with setter
    @property
    @abstractmethod
    def age(self):
        """Person must have an age"""
        pass
    
    @age.setter
    @abstractmethod
    def age(self, value):
        """Age must be settable"""
        pass
    
    # Abstract property with deleter
    @property
    @abstractmethod
    def email(self):
        pass
    
    @email.deleter
    @abstractmethod
    def email(self):
        pass

# Concrete implementation
class Employee(Person):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._email = None
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value
    
    @email.deleter
    def email(self):
        self._email = None

# Usage
emp = Employee("Alice", 30)
print(emp.name)              # → "Alice"
emp.age = 31                 # Setter works
del emp.email                # Deleter works
```

### 4. ABSTRACT CLASS METHODS AND STATIC METHODS

```python
from abc import ABC, abstractmethod

class Database(ABC):
    # Abstract classmethod
    @classmethod
    @abstractmethod
    def connect(cls, connection_string):
        """Connect to database (class-level operation)"""
        pass
    
    # Abstract staticmethod
    @staticmethod
    @abstractmethod
    def validate_connection_string(conn_str):
        """Validate connection string format"""
        pass
    
    # Regular abstract method
    @abstractmethod
    def execute(self, query):
        """Execute query on connection"""
        pass

# Concrete implementation
class PostgresDB(Database):
    @classmethod
    def connect(cls, connection_string):
        print(f"Connecting to Postgres: {connection_string}")
        return cls(connection_string)
    
    @staticmethod
    def validate_connection_string(conn_str):
        return '://' in conn_str and '@' in conn_str
    
    def __init__(self, connection_string):
        self.conn_str = connection_string
    
    def execute(self, query):
        return f"Executing on Postgres: {query}"

# Usage
is_valid = PostgresDB.validate_connection_string("postgres://user@host")  # → True
db = PostgresDB.connect("postgres://user:pass@localhost:5432/mydb")
result = db.execute("SELECT * FROM users")
```

### 5. VIRTUAL SUBCLASS REGISTRATION

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

# Method 1: Register decorator
@Drawable.register
class Circle:
    def draw(self):
        print("Drawing circle")

# Method 2: Direct registration
class Square:
    def draw(self):
        print("Drawing square")

Drawable.register(Square)

# Method 3: Register multiple classes
class Triangle:
    def draw(self):
        print("Drawing triangle")

class Hexagon:
    def draw(self):
        print("Drawing hexagon")

for shape_class in [Triangle, Hexagon]:
    Drawable.register(shape_class)

# Check registrations
print(issubclass(Circle, Drawable))      # → True
print(issubclass(Square, Drawable))      # → True
print(issubclass(Triangle, Drawable))    # → True
print(issubclass(Hexagon, Drawable))     # → True

# Instance checks work too
circle = Circle()
print(isinstance(circle, Drawable))      # → True

# Note: Virtual subclasses don't need to implement abstract methods!
@Drawable.register
class BrokenShape:
    pass  # No draw() method, but registration still works

print(issubclass(BrokenShape, Drawable)) # → True
broken = BrokenShape()  # This works! No TypeError
# broken.draw()         # This fails: AttributeError
```

### 6. CUSTOM SUBCLASS HOOKS

```python
from abc import ABC, abstractmethod

class Sized(ABC):
    @abstractmethod
    def __len__(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, C):
        """
        Custom logic for subclass checking.
        If a class has __len__, consider it a subclass.
        """
        if cls is Sized:
            # Check if the class has __len__ method
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

# These classes don't inherit from Sized, but have __len__
class MyList:
    def __len__(self):
        return 0

class MyString:
    def __len__(self):
        return 0

# Automatic subclass recognition via __subclasshook__
print(issubclass(MyList, Sized))         # → True
print(issubclass(MyString, Sized))       # → True
print(issubclass(int, Sized))            # → False (no __len__)

# Built-in types also work
print(issubclass(list, Sized))           # → True
print(issubclass(dict, Sized))           # → True
print(issubclass(str, Sized))            # → True
```

### 7. MULTIPLE ABSTRACT BASE CLASSES

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Resizable(ABC):
    @abstractmethod
    def resize(self, scale):
        pass

class Rotatable(ABC):
    @abstractmethod
    def rotate(self, degrees):
        pass

# Multiple inheritance from ABCs
class Shape(Drawable, Resizable, Rotatable):
    """Must implement draw(), resize(), and rotate()"""
    pass

# Concrete implementation
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self):
        print(f"Drawing rectangle: {self.width}x{self.height}")
    
    def resize(self, scale):
        self.width *= scale
        self.height *= scale
        return self
    
    def rotate(self, degrees):
        if degrees == 90 or degrees == 270:
            self.width, self.height = self.height, self.width
        return self

# Usage
rect = Rectangle(10, 5)
rect.draw()                  # → "Drawing rectangle: 10x5"
rect.resize(2).draw()        # → "Drawing rectangle: 20x10"
rect.rotate(90).draw()       # → "Drawing rectangle: 10x20"
```

### 8. ABSTRACT BASE CLASS WITH CONCRETE METHODS

```python
from abc import ABC, abstractmethod

class Collection(ABC):
    """Abstract collection with some concrete methods"""
    
    @abstractmethod
    def add(self, item):
        """Add item (must implement)"""
        pass
    
    @abstractmethod
    def remove(self, item):
        """Remove item (must implement)"""
        pass
    
    @abstractmethod
    def __len__(self):
        """Get size (must implement)"""
        pass
    
    # Concrete methods (provided by ABC)
    def is_empty(self):
        """Check if empty (concrete implementation)"""
        return len(self) == 0
    
    def clear(self):
        """Clear all items (concrete implementation using abstract methods)"""
        while not self.is_empty():
            # Assumes items can be iterated (subclass responsibility)
            for item in self:
                self.remove(item)
                break
    
    @abstractmethod
    def __iter__(self):
        """Iterate items (must implement)"""
        pass

# Concrete implementation
class ListCollection(Collection):
    def __init__(self):
        self._items = []
    
    def add(self, item):
        self._items.append(item)
    
    def remove(self, item):
        self._items.remove(item)
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)

# Usage - concrete methods work automatically
col = ListCollection()
print(col.is_empty())        # → True (uses concrete method)
col.add(1)
col.add(2)
print(col.is_empty())        # → False
col.clear()                  # Concrete method using abstract ones
print(col.is_empty())        # → True
```

### 9. INSPECTION AND INTROSPECTION

```python
from abc import ABC, abstractmethod
import inspect

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def honk(self):
        print("Beep!")

class PartialCar(Vehicle):
    def start(self):
        print("Starting...")
    # Missing stop() implementation

class CompleteCar(Vehicle):
    def start(self):
        print("Starting...")
    
    def stop(self):
        print("Stopping...")

# Check for abstract methods
print(Vehicle.__abstractmethods__)           # → frozenset({'start', 'stop'})
print(PartialCar.__abstractmethods__)        # → frozenset({'stop'})
print(CompleteCar.__abstractmethods__)       # → frozenset()

# Check if class is abstract
print(inspect.isabstract(Vehicle))           # → True
print(inspect.isabstract(PartialCar))        # → True
print(inspect.isabstract(CompleteCar))       # → False

# Count abstract methods
print(len(Vehicle.__abstractmethods__))      # → 2
print(len(PartialCar.__abstractmethods__))   # → 1
print(len(CompleteCar.__abstractmethods__))  # → 0

# Check if has abstract methods attribute
print(hasattr(Vehicle, '__abstractmethods__'))     # → True
print(hasattr(CompleteCar, '__abstractmethods__')) # → True (but empty)

# Get all abstract method names
for method_name in Vehicle.__abstractmethods__:
    print(f"Abstract method: {method_name}")
    # → Abstract method: start
    # → Abstract method: stop

# Try to instantiate
try:
    v = Vehicle()  # TypeError
except TypeError as e:
    print(f"Error: {e}")
    # → Error: Can't instantiate abstract class Vehicle with abstract methods start, stop

try:
    pc = PartialCar()  # TypeError
except TypeError as e:
    print(f"Error: {e}")
    # → Error: Can't instantiate abstract class PartialCar with abstract method stop

cc = CompleteCar()  # Works!
cc.start()          # → "Starting..."
```

### 10. DYNAMIC ABSTRACT METHOD UPDATES

```python
from abc import ABC, abstractmethod, update_abstractmethods

class DynamicBase(ABC):
    @abstractmethod
    def method1(self):
        pass

# Dynamically add abstract method
def new_abstract_method(self):
    pass

new_abstract_method.__isabstractmethod__ = True
DynamicBase.method2 = new_abstract_method

# Update abstract methods (Python 3.7+)
update_abstractmethods(DynamicBase)

# Now check abstract methods
print(DynamicBase.__abstractmethods__)  # → frozenset({'method1', 'method2'})

# Manual abstract method marking
class ManualABC(ABC):
    def manual_method(self):
        pass

# Mark as abstract manually
ManualABC.manual_method.__isabstractmethod__ = True
update_abstractmethods(ManualABC)

print(ManualABC.__abstractmethods__)  # → frozenset({'manual_method'})
```

### 11. CACHE TOKEN FOR INVALIDATION

```python
from abc import ABC, get_cache_token

class CachedABC(ABC):
    pass

# Get current cache token
token1 = get_cache_token()
print(f"Initial token: {token1}")

# Register a virtual subclass
class MyClass:
    pass

CachedABC.register(MyClass)

# Token changes after registration
token2 = get_cache_token()
print(f"After registration: {token2}")
print(f"Token changed: {token1 != token2}")  # → True

# Use tokens for cache invalidation in custom code
class CacheManager:
    def __init__(self):
        self.cache = {}
        self.token = get_cache_token()
    
    def get_cached_value(self, key):
        current_token = get_cache_token()
        if current_token != self.token:
            print("Cache invalidated!")
            self.cache.clear()
            self.token = current_token
        return self.cache.get(key)
    
    def set_cached_value(self, key, value):
        self.cache[key] = value
```

### 12. ACCESSING INTERNAL ABC STRUCTURES

```python
from abc import ABC

class MyABC(ABC):
    pass

class SubClass1(MyABC):
    pass

class SubClass2(MyABC):
    pass

# Register virtual subclass
class VirtualSub:
    pass

MyABC.register(VirtualSub)

# Access registry (WeakSet of registered virtual subclasses)
print(MyABC._abc_registry)
# → WeakSet with VirtualSub

# Access cache (WeakSet of instances for isinstance checks)
print(MyABC._abc_cache)
# → WeakSet (caches isinstance results)

# Access negative cache (for failed isinstance checks)
print(MyABC._abc_negative_cache)
# → WeakSet

# Access negative cache version
print(MyABC._abc_negative_cache_version)
# → Integer version number

# Get direct subclasses
print(type.__subclasses__(MyABC))
# → [SubClass1, SubClass2]

# Note: These are implementation details and may change
```

---

## PRACTICAL PROJECT PATTERNS

### Pattern 1: Plugin System Architecture
```python
from abc import ABC, abstractmethod

class Plugin(ABC):
    """Base class for all plugins"""
    
    @abstractmethod
    def initialize(self):
        """Initialize plugin resources"""
        pass
    
    @abstractmethod
    def execute(self, *args, **kwargs):
        """Execute plugin functionality"""
        pass
    
    @abstractmethod
    def cleanup(self):
        """Clean up plugin resources"""
        pass
    
    @property
    @abstractmethod
    def name(self):
        """Plugin name"""
        pass
    
    @property
    @abstractmethod
    def version(self):
        """Plugin version"""
        pass

class PluginManager:
    def __init__(self):
        self.plugins = []
    
    def register_plugin(self, plugin):
        if not isinstance(plugin, Plugin):
            raise TypeError(f"{plugin} is not a valid Plugin")
        self.plugins.append(plugin)
    
    def execute_all(self, *args, **kwargs):
        for plugin in self.plugins:
            plugin.initialize()
            try:
                plugin.execute(*args, **kwargs)
            finally:
                plugin.cleanup()

# Concrete plugin
class LoggingPlugin(Plugin):
    def initialize(self):
        print("Initializing logging...")
    
    def execute(self, *args, **kwargs):
        print(f"Logging: {args}, {kwargs}")
    
    def cleanup(self):
        print("Cleaning up logging...")
    
    @property
    def name(self):
        return "Logger"
    
    @property
    def version(self):
        return "1.0.0"
```

### Pattern 2: Data Validation Framework
```python
from abc import ABC, abstractmethod

class Validator(ABC):
    """Abstract validator for data validation"""
    
    @abstractmethod
    def validate(self, value):
        """
        Validate value.
        Returns: (is_valid: bool, error_message: str or None)
        """
        pass
    
    @abstractmethod
    def get_error_message(self, value):
        """Get descriptive error message"""
        pass

class RangeValidator(Validator):
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
    
    def validate(self, value):
        is_valid = self.min_val <= value <= self.max_val
        error = None if is_valid else self.get_error_message(value)
        return is_valid, error
    
    def get_error_message(self, value):
        return f"Value {value} not in range [{self.min_val}, {self.max_val}]"

class StringLengthValidator(Validator):
    def __init__(self, max_length):
        self.max_length = max_length
    
    def validate(self, value):
        is_valid = len(value) <= self.max_length
        error = None if is_valid else self.get_error_message(value)
        return is_valid, error
    
    def get_error_message(self, value):
        return f"String length {len(value)} exceeds max {self.max_length}"

class ValidationChain:
    def __init__(self):
        self.validators = []
    
    def add_validator(self, validator):
        if not isinstance(validator, Validator):
            raise TypeError("Must be a Validator")
        self.validators.append(validator)
    
    def validate(self, value):
        errors = []
        for validator in self.validators:
            is_valid, error = validator.validate(value)
            if not is_valid:
                errors.append(error)
        return len(errors) == 0, errors
```

### Pattern 3: Repository Pattern (Database Abstraction)
```python
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')

class Repository(ABC, Generic[T]):
    """Abstract repository for data access"""
    
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[T]:
        """Find entity by ID"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[T]:
        """Find all entities"""
        pass
    
    @abstractmethod
    def save(self, entity: T) -> T:
        """Save entity"""
        pass
    
    @abstractmethod
    def delete(self, entity: T) -> None:
        """Delete entity"""
        pass
    
    @abstractmethod
    def exists(self, id: int) -> bool:
        """Check if entity exists"""
        pass

class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

class StudentRepository(Repository[Student]):
    def __init__(self):
        self._data = {}
        self._next_id = 1
    
    def find_by_id(self, id: int) -> Optional[Student]:
        return self._data.get(id)
    
    def find_all(self) -> List[Student]:
        return list(self._data.values())
    
    def save(self, entity: Student) -> Student:
        if entity.id is None:
            entity.id = self._next_id
            self._next_id += 1
        self._data[entity.id] = entity
        return entity
    
    def delete(self, entity: Student) -> None:
        if entity.id in self._data:
            del self._data[entity.id]
    
    def exists(self, id: int) -> bool:
        return id in self._data
```

### Pattern 4: Strategy Pattern with ABC
```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    """Abstract sorting strategy"""
    
    @abstractmethod
    def sort(self, data: list) -> list:
        """Sort data and return sorted list"""
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Strategy name"""
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        data = data.copy()
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data
    
    @property
    def name(self) -> str:
        return "Bubble Sort"

class QuickSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)
    
    @property
    def name(self) -> str:
        return "Quick Sort"

class Sorter:
    def __init__(self, strategy: SortStrategy):
        if not isinstance(strategy, SortStrategy):
            raise TypeError("Must provide a SortStrategy")
        self.strategy = strategy
    
    def sort(self, data: list) -> list:
        print(f"Using {self.strategy.name}")
        return self.strategy.sort(data)
```

### Pattern 5: Template Method Pattern
```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Template method pattern for data processing"""
    
    def process_file(self, filepath: str) -> dict:
        """Template method - defines the algorithm structure"""
        # Step 1: Load data
        data = self.load_data(filepath)
        
        # Step 2: Validate
        if not self.validate_data(data):
            raise ValueError("Invalid data")
        
        # Step 3: Transform
        transformed = self.transform_data(data)
        
        # Step 4: Save
        result = self.save_data(transformed)
        
        # Step 5: Cleanup
        self.cleanup()
        
        return result
    
    @abstractmethod
    def load_data(self, filepath: str):
        """Load data from file (must implement)"""
        pass
    
    @abstractmethod
    def transform_data(self, data):
        """Transform data (must implement)"""
        pass
    
    @abstractmethod
    def save_data(self, data):
        """Save processed data (must implement)"""
        pass
    
    def validate_data(self, data) -> bool:
        """Validate data (optional to override)"""
        return data is not None
    
    def cleanup(self):
        """Cleanup resources (optional to override)"""
        pass

class CSVProcessor(DataProcessor):
    def load_data(self, filepath: str):
        with open(filepath, 'r') as f:
            return [line.strip().split(',') for line in f]
    
    def transform_data(self, data):
        # Convert to dict format
        headers = data[0]
        return [dict(zip(headers, row)) for row in data[1:]]
    
    def save_data(self, data):
        print(f"Saving {len(data)} records")
        return {"status": "success", "count": len(data)}
    
    def validate_data(self, data) -> bool:
        return super().validate_data(data) and len(data) > 0
```

### Pattern 6: Observer Pattern Interface
```python
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    """Abstract observer"""
    
    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        """Called when subject changes"""
        pass

class Subject(ABC):
    """Abstract subject (observable)"""
    
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer) -> None:
        """Attach an observer"""
        if not isinstance(observer, Observer):
            raise TypeError("Must be an Observer")
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        """Detach an observer"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self) -> None:
        """Notify all observers"""
        for observer in self._observers:
            observer.update(self)
    
    @abstractmethod
    def get_state(self):
        """Get current state (must implement)"""
        pass

class StockMarket(Subject):
    def __init__(self):
        super().__init__()
        self._price = 0.0
    
    def set_price(self, price: float):
        self._price = price
        self.notify()
    
    def get_state(self):
        return {"price": self._price}

class StockDisplay(Observer):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, subject: Subject) -> None:
        state = subject.get_state()
        print(f"{self.name}: Stock price is now ${state['price']:.2f}")
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: Attempting to Instantiate Abstract Class
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# WRONG
try:
    shape = Shape()  # TypeError
except TypeError as e:
    print(e)
    # → Can't instantiate abstract class Shape with abstract method area

# RIGHT
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)  # Works!
```

### Error 2: Forgetting to Implement Abstract Method
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

# WRONG - missing move()
class Dog(Animal):
    def speak(self):
        return "Woof!"
    # Missing move() implementation

try:
    dog = Dog()  # TypeError
except TypeError as e:
    print(e)
    # → Can't instantiate abstract class Dog with abstract method move

# RIGHT - implement all abstract methods
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
    def move(self):
        return "Walking on four legs"

cat = Cat()  # Works!
```

### Error 3: Incorrect Decorator Order
```python
from abc import ABC, abstractmethod

class Configuration(ABC):
    # WRONG - abstractmethod should be innermost
    @abstractmethod
    @property
    def database_url(self):
        pass
    
    # RIGHT - property should be outermost
    @property
    @abstractmethod
    def api_key(self):
        pass
    
    # WRONG - abstractmethod should be innermost
    @abstractmethod
    @classmethod
    def from_file(cls, filepath):
        pass
    
    # RIGHT - classmethod should be outermost
    @classmethod
    @abstractmethod
    def from_env(cls):
        pass
```

### Error 4: Virtual Subclass Doesn't Check Implementation
```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

# Virtual subclass registration doesn't validate implementation
@Drawable.register
class BrokenShape:
    pass  # No draw() method!

# This works (no error during registration)
broken = BrokenShape()

# But this fails at runtime
try:
    broken.draw()  # AttributeError
except AttributeError as e:
    print(e)
    # → 'BrokenShape' object has no attribute 'draw'

# RIGHT - Always implement required methods even for virtual subclasses
@Drawable.register
class ProperShape:
    def draw(self):
        print("Drawing shape")

proper = ProperShape()
proper.draw()  # Works!
```

### Error 5: Calling super() on Abstract Method
```python
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def process(self):
        pass  # No implementation

class Derived(Base):
    def process(self):
        # WRONG - calling super() on abstract method with no body
        super().process()  # Does nothing (just returns None)
        print("Derived processing")

# RIGHT - Only call super() if base has implementation
class BaseWithDefault(ABC):
    @abstractmethod
    def process(self):
        print("Base processing")  # Has implementation

class DerivedGood(BaseWithDefault):
    def process(self):
        super().process()  # Works! Calls base implementation
        print("Derived processing")
```

---

## PERFORMANCE TIPS

1. **Use ABC inheritance over explicit metaclass**
   ```python
   # Faster and more readable
   class MyABC(ABC):
       pass
   
   # Slower, older style
   class MyABC(metaclass=ABCMeta):
       pass
   ```

2. **Virtual subclass registration is faster than inheritance**
   ```python
   # If you don't need to enforce implementation at instantiation time
   class FastClass:
       def required_method(self):
           pass
   
   MyABC.register(FastClass)  # Faster than inheritance
   ```

3. **Cache isinstance/issubclass results**
   ```python
   # Python caches these automatically, but you can optimize further
   class TypeCache:
       def __init__(self):
           self._cache = {}
       
       def is_instance_of(self, obj, cls):
           obj_type = type(obj)
           key = (obj_type, cls)
           if key not in self._cache:
               self._cache[key] = isinstance(obj, cls)
           return self._cache[key]
   ```

4. **Minimize abstract methods**
   ```python
   # Too many abstract methods slow down class creation
   # Group related functionality
   class Minimal(ABC):
       @abstractmethod
       def process(self, data):
           """Single method handles multiple operations"""
           pass
   ```

5. **Use __subclasshook__ for interface checking**
   ```python
   # Faster than registration for protocol-like checks
   class Sized(ABC):
       @classmethod
       def __subclasshook__(cls, C):
           if cls is Sized:
               if any("__len__" in B.__dict__ for B in C.__mro__):
                   return True
           return NotImplemented
   ```

---

## BEST PRACTICES

1. **Always document abstract methods**
   ```python
   class Repository(ABC):
       @abstractmethod
       def save(self, entity):
           """
           Save entity to storage.
           
           Args:
               entity: The entity to save
           
           Returns:
               The saved entity with updated ID
           
           Raises:
               ValidationError: If entity is invalid
               StorageError: If save operation fails
           """
           pass
   ```

2. **Provide default implementations when possible**
   ```python
   class Collection(ABC):
       @abstractmethod
       def add(self, item):
           pass
       
       @abstractmethod
       def __len__(self):
           pass
       
       # Concrete method using abstract ones
       def is_empty(self):
           return len(self) == 0
   ```

3. **Use type hints with ABCs**
   ```python
   from abc import ABC, abstractmethod
   from typing import List, TypeVar, Generic
   
   T = TypeVar('T')
   
   class Container(ABC, Generic[T]):
       @abstractmethod
       def add(self, item: T) -> None:
           pass
       
       @abstractmethod
       def get_all(self) -> List[T]:
           pass
   ```

4. **Combine with Protocol for structural subtyping (3.8+)**
   ```python
   from typing import Protocol
   from abc import ABC, abstractmethod
   
   # Structural typing (duck typing)
   class Drawable(Protocol):
       def draw(self) -> None: ...
   
   # Nominal typing (explicit inheritance)
   class Shape(ABC):
       @abstractmethod
       def area(self) -> float:
           pass
   ```

5. **Test for abstract method coverage**
   ```python
   import inspect
   
   def test_abstract_implementation(cls):
       """Verify all abstract methods are implemented"""
       if inspect.isabstract(cls):
           abstract = cls.__abstractmethods__
           raise AssertionError(
               f"{cls.__name__} missing: {abstract}"
           )
   ```

---

## VERSION COMPATIBILITY

- **Python 3.4+**: `ABC` class introduced (simpler than metaclass)
- **Python 3.7+**: `update_abstractmethods()` function added
- **Python 3.8+**: Better integration with `typing.Protocol`
- **Python 3.9+**: Improved performance for `isinstance`/`issubclass`
- **Python 3.10+**: Better error messages for abstract classes

---

## RELATED MODULES

- **typing**: Type hints and Protocol for structural subtyping
- **collections.abc**: Collection abstract base classes
- **numbers**: Numeric abstract base classes
- **io**: I/O abstract base classes
- **inspect**: Introspection utilities for abstract classes

---

## SUMMARY

The `abc` module is essential for:
- **Interface definition**: Enforce contracts in class hierarchies
- **Framework design**: Create extensible plugin systems
- **Code organization**: Separate interface from implementation
- **Type checking**: Enable runtime type validation
- **Documentation**: Make API requirements explicit

Key concepts:
1. Use `@abstractmethod` to mark required methods
2. Inherit from `ABC` for automatic enforcement
3. Combine with `@property`, `@classmethod`, `@staticmethod`
4. Use virtual subclass registration for duck typing
5. Implement `__subclasshook__` for custom type checking
