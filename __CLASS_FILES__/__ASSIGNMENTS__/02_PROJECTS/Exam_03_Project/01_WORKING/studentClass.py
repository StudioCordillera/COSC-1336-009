"""
Student Class Module

Provides a simple Student class for managing exam scores and calculating averages.

Public API (__all__):
    ```python
    ['Student']
    ```

Class Signatures:
    ```python
    class Student:
        __init__(self, name: str, exam1: float, exam2: float, exam3: float) -> None
        examAvg(self) -> float
    ```
    
Attributes:
    ```python
    name: str  # Student's full name
    exam1: float  # First exam score (0.0 - 100.0)
    exam2: float  # Second exam score (0.0 - 100.0)
    exam3: float  # Third exam score (0.0 - 100.0)
    ```

Module Metadata:
    ```python
    __version__ = '1.0'
    __author__ = 'Matthew Ochoa'
    __date__ = 'December 6, 2025'
    ```

Usage:
    ```python
    from studentClass import Student
    
    student = Student("Alice", 95.5, 87.0, 92.5)
    print(f"Average: {student.examAvg()}")
    ```

Author: Matthew Ochoa
Date: December 6, 2025
Version: 1.0
"""

__all__ = ['Student']
__version__ = '1.0'
__author__ = 'Matthew Ochoa'
__date__ = 'December 6, 2025'


class Student:
    """
    Student data class for managing exam scores and calculating averages.
    
    Methods:
        ```python
        __init__(name: str, exam1: float, exam2: float, exam3: float) -> None
        examAvg() -> float
        ```
    
    Attributes:
        ```python
        name: str  # Student's full name
        exam1: float  # First exam score (0.0 - 100.0)
        exam2: float  # Second exam score (0.0 - 100.0)
        exam3: float  # Third exam score (0.0 - 100.0)
        ```
    
    Example:
        ```python
        student = Student("John Doe", 85.5, 92.0, 88.5)
        student.examAvg()  # 88.67
        print(f"{student.name}: {student.examAvg():.2f}")  # John Doe: 88.67
        ```

__________________________________________________________________________________
                                                                           2025@MO
    """

    name: str
    exam1: float
    exam2: float
    exam3: float

    def __init__(self, name: str, exam1: float, exam2: float, exam3: float) -> None:
        """
        Initialize a Student instance with name and three exam scores.
        
        Signature:
            ```python
            def __init__(self, name: str, exam1: float, exam2: float, exam3: float) -> None
            ```
        
        Parameters:
            ```python
            name: str  # Student's full name
            exam1: float  # First exam score (0.0 - 100.0)
            exam2: float  # Second exam score (0.0 - 100.0)
            exam3: float  # Third exam score (0.0 - 100.0)
            ```
        
        Returns:
            ```python
            None
            ```
        
        Example:
            ```python
            student = Student("Jane Smith", 95.0, 87.5, 92.0)
            student.name  # 'Jane Smith'
            student.exam1  # 95.0
            ```

__________________________________________________________________________________
                                                                           2025@MO
        """
        self.name = name
        self.exam1 = exam1
        self.exam2 = exam2
        self.exam3 = exam3

    def examAvg(self) -> float:
        """
        Calculate the average of all three exam scores.
        
        Signature:
            ```python
            def examAvg(self) -> float
            ```
        
        Returns:
            ```python
            float  # Average exam score (sum of three exams divided by 3)
            ```
        
        Example:
            ```python
            student = Student("Bob Johnson", 90.0, 85.0, 95.0)
            student.examAvg()  # 90.0
            round(student.examAvg(), 2)  # 90.0
            ```
        
        Note:
            Result is not rounded. Use `round()` or format strings for precision control.
        
__________________________________________________________________________________
                                                                           2025@MO
        """
        return ((self.exam1 + self.exam2 + self.exam3) / 3)
