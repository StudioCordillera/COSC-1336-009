"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    ULTIMATE PYTHON CLASS TEMPLATE                            ║
║              A Complete Self-Explanatory OOP Reference                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

This file demonstrates ALL essential class concepts in Python:
    • Class vs Instance attributes
    • Constructor (__init__)
    • Instance methods vs Class methods vs Static methods
    • Special/Magic methods (dunder methods)
    • Property decorators (getters/setters)
    • Inheritance
    • Encapsulation (public, protected, private)
    • Method overriding
    • String representation
"""


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 1: BASIC CLASS STRUCTURE
# ═══════════════════════════════════════════════════════════════════════════

class Student:
    """
    A comprehensive example demonstrating all essential class features.
    
    This docstring is accessible via Student.__doc__
    Good practice: Always include a brief description of the class purpose.
    """
    
    # ───────────────────────────────────────────────────────────────────────
    # CLASS ATTRIBUTES (Shared by ALL instances)
    # ───────────────────────────────────────────────────────────────────────
    
    school_name = "Python Academy"           # Shared by all Student objects
    total_students = 0                       # Tracks count across all instances
    valid_grades = ['A', 'B', 'C', 'D', 'F'] # Shared reference data
    
    
    # ───────────────────────────────────────────────────────────────────────
    # CONSTRUCTOR: Runs automatically when creating a new object
    # ───────────────────────────────────────────────────────────────────────
    
    def __init__(self, name, age, grade='A'):
        """
        Initialize a new Student instance.
        
        Args:
            name (str): Student's full name
            age (int): Student's age
            grade (str): Letter grade (default: 'A')
        
        The 'self' parameter refers to the instance being created.
        """
        # PUBLIC instance attributes (accessible anywhere)
        self.name = name
        self.age = age
        self.grade = grade
        
        # PROTECTED attribute (convention: single underscore)
        # Indicates "internal use" but still accessible
        self._student_id = Student.total_students + 1
        
        # PRIVATE attribute (name mangling: double underscore)
        # Python renames to _ClassName__attribute
        self.__gpa = 0.0
        
        # Instance-specific list (each object gets its own copy)
        self.courses = []
        
        # Update class attribute
        Student.total_students += 1
    
    
    # ───────────────────────────────────────────────────────────────────────
    # INSTANCE METHODS: Operate on individual objects (require 'self')
    # ───────────────────────────────────────────────────────────────────────
    
    def add_course(self, course_name):
        """Add a course to this student's schedule."""
        self.courses.append(course_name)
        return f"Added {course_name} to {self.name}'s schedule"
    
    def get_info(self):
        """Return formatted student information."""
        return (f"Name: {self.name}, Age: {self.age}, "
                f"Grade: {self.grade}, ID: {self._student_id}")
    
    def calculate_gpa(self):
        """Calculate and store GPA based on letter grade."""
        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        self.__gpa = grade_points.get(self.grade, 0.0)
        return self.__gpa
    
    
    # ───────────────────────────────────────────────────────────────────────
    # PROPERTY DECORATORS: Controlled access to attributes (getters/setters)
    # ───────────────────────────────────────────────────────────────────────
    
    @property
    def gpa(self):
        """Getter: Access GPA like an attribute (student.gpa)"""
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        """Setter: Validate before setting (student.gpa = 3.5)"""
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")
    
    @property
    def is_honor_student(self):
        """Computed property: No actual attribute, calculated on-the-fly"""
        return self.__gpa >= 3.5
    
    
    # ───────────────────────────────────────────────────────────────────────
    # CLASS METHODS: Operate on the class itself (use @classmethod)
    # ───────────────────────────────────────────────────────────────────────
    
    @classmethod
    def get_school_info(cls):
        """
        Access/modify class attributes.
        'cls' refers to the class (Student), not an instance.
        """
        return f"{cls.school_name} has {cls.total_students} students"
    
    @classmethod
    def set_school_name(cls, new_name):
        """Modify class attribute for ALL instances."""
        cls.school_name = new_name
    
    @classmethod
    def create_from_string(cls, student_string):
        """
        Alternative constructor (factory method).
        Example: Student.create_from_string("John,20,B")
        """
        name, age, grade = student_string.split(',')
        return cls(name, int(age), grade)
    
    
    # ───────────────────────────────────────────────────────────────────────
    # STATIC METHODS: Utility functions (use @staticmethod)
    # ───────────────────────────────────────────────────────────────────────
    
    @staticmethod
    def is_valid_grade(grade):
        """
        No access to instance or class.
        Pure utility function related to the class concept.
        """
        return grade in Student.valid_grades
    
    @staticmethod
    def grade_to_points(grade):
        """Convert letter grade to numeric points."""
        conversion = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        return conversion.get(grade, 0.0)
    
    
    # ───────────────────────────────────────────────────────────────────────
    # SPECIAL/MAGIC METHODS: Customize object behavior (dunder methods)
    # ───────────────────────────────────────────────────────────────────────
    
    def __str__(self):
        """
        User-friendly string representation.
        Called by: print(student), str(student)
        """
        return f"Student({self.name}, Grade: {self.grade})"
    
    def __repr__(self):
        """
        Developer-friendly representation (should be unambiguous).
        Called by: repr(student), or in interactive console
        """
        return f"Student('{self.name}', {self.age}, '{self.grade}')"
    
    def __eq__(self, other):
        """
        Define equality comparison.
        Called by: student1 == student2
        """
        if not isinstance(other, Student):
            return False
        return self.name == other.name and self.age == other.age
    
    def __lt__(self, other):
        """
        Define less-than comparison (enables sorting).
        Called by: student1 < student2, sorted([students])
        """
        return self.name < other.name
    
    def __len__(self):
        """
        Define length behavior.
        Called by: len(student)
        """
        return len(self.courses)
    
    def __getitem__(self, index):
        """
        Enable indexing: student[0] returns first course.
        Makes object iterable-like.
        """
        return self.courses[index]
    
    def __del__(self):
        """
        Destructor: Called when object is deleted.
        Use cautiously - not always called immediately!
        """
        Student.total_students -= 1


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 2: INHERITANCE
# ═══════════════════════════════════════════════════════════════════════════

class GraduateStudent(Student):
    """
    Inherits all attributes and methods from Student (parent/base class).
    Demonstrates method overriding and extension.
    """
    
    def __init__(self, name, age, grade, thesis_topic):
        """
        Call parent constructor with super()
        Then add child-specific attributes
        """
        super().__init__(name, age, grade)  # Initialize parent class
        self.thesis_topic = thesis_topic
        self.is_graduate = True
    
    def get_info(self):
        """
        METHOD OVERRIDING: Replace parent's implementation.
        Can still access parent method with super()
        """
        parent_info = super().get_info()  # Get parent's version
        return f"{parent_info}, Thesis: {self.thesis_topic}"
    
    def defend_thesis(self):
        """Child-specific method (not in parent class)."""
        return f"{self.name} is defending thesis on: {self.thesis_topic}"


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 3: DEMONSTRATION & TESTING
# ═══════════════════════════════════════════════════════════════════════════

def run_comprehensive_demo():
    """Execute all examples to demonstrate class functionality."""
    
    print("="*80)
    print("ULTIMATE CLASS TEMPLATE DEMONSTRATION")
    print("="*80)
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[1] CREATING INSTANCES")
    print("-" * 80)
    
    student1 = Student("Alice Johnson", 20, "A")
    student2 = Student("Bob Smith", 21, "B")
    student3 = Student.create_from_string("Charlie Brown,19,C")  # Factory method
    
    print(f"Created: {student1}")
    print(f"Created: {student2}")
    print(f"Created: {student3}")
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[2] CLASS vs INSTANCE ATTRIBUTES")
    print("-" * 80)
    
    print(f"School Name (class attribute): {Student.school_name}")
    print(f"Total Students (class attribute): {Student.total_students}")
    print(f"Student1 name (instance attribute): {student1.name}")
    print(f"Student2 name (instance attribute): {student2.name}")
    
    # Modify class attribute affects ALL instances
    Student.set_school_name("Advanced Python Academy")
    print(f"\nAfter changing school name:")
    print(f"Via class: {Student.school_name}")
    print(f"Via student1: {student1.school_name}")
    print(f"Via student2: {student2.school_name}")
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[3] INSTANCE METHODS")
    print("-" * 80)
    
    print(student1.add_course("Python Programming"))
    print(student1.add_course("Data Structures"))
    print(student2.add_course("Web Development"))
    
    print(f"\n{student1.name}'s courses: {student1.courses}")
    print(f"{student2.name}'s courses: {student2.courses}")
    print(f"Note: Each instance has its own course list!")
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[4] ENCAPSULATION (Public, Protected, Private)")
    print("-" * 80)
    
    print(f"Public attribute (name): {student1.name}")
    print(f"Protected attribute (_student_id): {student1._student_id}")
    print(f"Private attribute (__gpa) accessed via property: {student1.gpa}")
    
    # Direct access to private is mangled
    print(f"Private via name mangling: {student1._Student__gpa}")
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[5] PROPERTY DECORATORS (Getters/Setters)")
    print("-" * 80)
    
    student1.calculate_gpa()  # Calculate based on grade
    print(f"GPA via property getter: {student1.gpa}")
    print(f"Is honor student? {student1.is_honor_student}")
    
    # Using setter with validation
    try:
        student1.gpa = 3.8  # Valid
        print(f"Updated GPA: {student1.gpa}")
        student1.gpa = 5.0  # Invalid - will raise error
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[6] CLASS METHODS")
    print("-" * 80)
    
    print(Student.get_school_info())  # Call on class itself
    print(student1.get_school_info())  # Or on instance (same result)
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[7] STATIC METHODS")
    print("-" * 80)
    
    print(f"Is 'A' a valid grade? {Student.is_valid_grade('A')}")
    print(f"Is 'Z' a valid grade? {Student.is_valid_grade('Z')}")
    print(f"Grade 'B' points: {Student.grade_to_points('B')}")
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[8] MAGIC METHODS")
    print("-" * 80)
    
    print(f"__str__: {str(student1)}")
    print(f"__repr__: {repr(student1)}")
    print(f"__eq__: student1 == student2? {student1 == student2}")
    print(f"__len__: Number of courses for student1: {len(student1)}")
    print(f"__getitem__: First course: {student1[0]}")
    
    # Sorting uses __lt__
    students = [student2, student1, student3]
    students.sort()
    print(f"Sorted students: {[s.name for s in students]}")
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[9] INHERITANCE")
    print("-" * 80)
    
    grad_student = GraduateStudent("Diana Prince", 25, "A", "AI Ethics")
    print(f"Graduate student: {grad_student}")
    print(f"Info (overridden): {grad_student.get_info()}")
    print(f"Child-specific method: {grad_student.defend_thesis()}")
    print(f"Inherited method: {grad_student.add_course('Advanced ML')}")
    print(f"Grad student courses: {grad_student.courses}")
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[10] DOCSTRINGS & INTROSPECTION")
    print("-" * 80)
    
    print(f"Class docstring: {Student.__doc__[:50]}...")
    print(f"Method docstring: {Student.add_course.__doc__}")
    print(f"Class name: {Student.__name__}")
    print(f"Instance type: {type(student1)}")
    print(f"Is instance of Student? {isinstance(student1, Student)}")
    print(f"Is subclass? {issubclass(GraduateStudent, Student)}")
    
    # ─────────────────────────────────────────────────────────────────────
    print("\n[11] ATTRIBUTE LISTING")
    print("-" * 80)
    
    print("Student1 attributes:")
    for attr in dir(student1):
        if not attr.startswith('_'):  # Skip private/magic methods
            print(f"  • {attr}: {getattr(student1, attr, 'N/A')}")
    
    print("\n" + "="*80)
    print("END OF DEMONSTRATION")
    print("="*80)


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 4: QUICK REFERENCE GUIDE
# ═══════════════════════════════════════════════════════════════════════════

"""
QUICK SYNTAX REFERENCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─ CLASS DEFINITION ──────────────────────────────────────────────────────────┐
│ class ClassName:                                                            │
│     class_attribute = value    # Shared by all instances                    │
│                                                                             │
│     def __init__(self, param):                                              │
│         self.instance_attr = param  # Unique to each instance               │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ METHOD TYPES ──────────────────────────────────────────────────────────────┐
│ Instance Method:    def method(self, args):      # Operates on instance     │
│ Class Method:       @classmethod                                            │
│                     def method(cls, args):        # Operates on class       │
│ Static Method:      @staticmethod                                           │
│                     def method(args):             # Utility function        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ PROPERTIES ────────────────────────────────────────────────────────────────┐
│ @property                                                                   │
│ def attribute(self):          # Getter: obj.attribute                       │
│     return self._attribute                                                  │
│                                                                             │
│ @attribute.setter                                                           │
│ def attribute(self, value):   # Setter: obj.attribute = value               │
│     self._attribute = value                                                 │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ INHERITANCE ───────────────────────────────────────────────────────────────┐
│ class ChildClass(ParentClass):                                              │
│     def __init__(self, args):                                               │
│         super().__init__(parent_args)  # Call parent constructor            │
│         self.child_attr = value                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ COMMON MAGIC METHODS ──────────────────────────────────────────────────────┐
│ __init__(self, ...)       Constructor                                       │
│ __str__(self)             Informal string (print, str)                      │
│ __repr__(self)            Official representation                           │
│ __eq__(self, other)       Equality (==)                                     │
│ __lt__(self, other)       Less than (<), enables sorting                    │
│ __len__(self)             Length (len)                                      │
│ __getitem__(self, key)    Indexing ([])                                     │
│ __del__(self)             Destructor                                        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─ ENCAPSULATION CONVENTIONS ─────────────────────────────────────────────────┐
│ public_attr       Public: No restrictions                                   │
│ _protected_attr   Protected: Internal use (convention only)                 │
│ __private_attr    Private: Name mangling to _ClassName__private_attr        │
└─────────────────────────────────────────────────────────────────────────────┘

BEST PRACTICES:
✓ Use descriptive class names (PascalCase)
✓ Write docstrings for classes and methods
✓ Initialize all instance attributes in __init__
✓ Use properties for controlled attribute access
✓ Keep methods focused and single-purpose
✓ Favor composition over inheritance when appropriate
✓ Use class methods for alternative constructors
✓ Use static methods for utilities related to class concept
"""


# ═══════════════════════════════════════════════════════════════════════════
# RUN DEMONSTRATION
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    run_comprehensive_demo()
