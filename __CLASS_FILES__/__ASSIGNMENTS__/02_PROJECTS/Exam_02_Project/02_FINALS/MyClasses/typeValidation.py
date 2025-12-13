"""
Type Validation Module

Provides robust input validation functions for Python data types with comprehensive
error handling and user feedback. Ensures type-safe user input for interactive applications.

Public API (__all__):
    ```python
    ['validateInput', 'getBool', 'getFloat', 'getInt', 'getStr']
    ```

Function Signatures:
    ```python
    validateInput(varType: type, prompt: str) -> bool | int | float | str
    getBool() -> bool
    getFloat(userin: str) -> float | None
    getInt(userin: str) -> int | None
    getStr(userin: str) -> str | None
    tryLoop(varType: type, userin: str) -> varType | None  # Internal helper
    ```

Module Metadata:
    ```python
    __version__ = '1.0'
    __author__ = 'Matthew Ochoa'
    __date__ = 'December 6, 2025'
    ```

Usage:
    from typeValidation import validateInput
    
    age = validateInput(int, "Enter your age: ")
    score = validateInput(float, "Enter score: ")
    name = validateInput(str, "Enter name: ")
    confirmed = validateInput(bool, "Confirm? ")

Author: Matthew Ochoa
Date: December 6, 2025
Version: 1.0
"""

__all__ = ['validateInput', 'getBool', 'getFloat', 'getInt', 'getStr']
__version__ = '1.0'
__author__ = 'Matthew Ochoa'
__date__ = 'December 6, 2025'


def validateInput(varType: type, prompt: str):
    """
    Universal input validation dispatcher with type-safe guarantees.
    
    Continuously prompts user until valid input matching the specified type is received.
    Handles `bool`, `int`, `float`, and `str` types with specialized validation rules.
    
    Signature:
        ```python
        def validateInput(varType: type, prompt: str) -> bool | int | float | str
        ```
    
    Parameters:
        ```python
        varType: type  # Target data type (bool, int, float, or str)
        prompt: str  # User prompt message displayed during input request
        ```
    
    Returns:
        ```python
        bool | int | float | str  # Validated input matching varType
        ```
    
    Raises:
        ```python
        KeyError  # If varType is not in supported types (bool, int, float, str)
        ```
    
    Examples:
        ```python
        age = validateInput(int, "Enter age: ")  # Enter age: 25 -> 25
        score = validateInput(float, "Enter score: ")  # Enter score: 95.5 -> 95.5
        name = validateInput(str, "Enter name: ")  # Enter name: Alice -> 'Alice'
        confirmed = validateInput(bool, "Confirm? ")  # T/F prompt -> True/False
        ```
    
    Note:
        - Boolean input uses separate `getBool()` handler (T/F prompt)
        - Integer rejects float-formatted input (e.g., "42.0")
        - Float rejects integer-only input (e.g., "42" without decimal)
        - String rejects empty input and pure numerical strings
       
__________________________________________________________________________________
                                                                           2025@MO
    """
    dataTypes = {float: getFloat, int: getInt, str: getStr}

    while True:
        if varType is bool:
            return getBool()
        else:
            result = dataTypes[varType](input(prompt))
            if result is not None:
                return result


def getBool() -> bool:
    """
    Boolean input validation with case-insensitive T/F recognition.
    
    Continuously prompts user until valid 'T' (`True`) or 'F' (`False`) is entered.
    Input is case-insensitive: 't', 'T', 'f', 'F' all accepted.
    
    Signature:
        ```python
        def getBool() -> bool
        ```
    
    Returns:
        ```python
        bool  # True for 'T' input, False for 'F' input
        ```
    
    Examples:
        ```python
        getBool()  # Enter 'T' for true or 'F' for false... t -> True
        getBool()  # Enter 'T' for true or 'F' for false... F -> False
        ```
    
    Note:
        Invalid inputs display error message and re-prompt user.

__________________________________________________________________________________
                                                                           2025@MO
    """
    while True:
        userin = input('\tEnter \'T\' for true or \'F\' for false... ')

        if userin.upper() == 'T':
            return True
        elif userin.upper() == 'F':
            return False
        else:
            print('\tINVALID OPTION...')


def getFloat(userin: str) -> float | None:
    """
    Float input validation requiring explicit decimal notation.
    
    Validates string input as `float` type with strict decimal point requirement.
    Rejects integer-format numbers (e.g., "42") to enforce float clarity.
    
    Signature:
        ```python
        def getFloat(userin: str) -> float | None
        ```
    
    Parameters:
        ```python
        userin: str  # Raw user input string to validate
        ```
    
    Returns:
        ```python
        float | None  # Validated float if successful, None if invalid
        ```
    
    Validation Rules:
        - Must contain decimal point ('.')
        - Must be convertible to `float` type
        - Rejects integer-only format (e.g., "42" rejected, "42.0" accepted)
    
    Examples:
        ```python
        getFloat("95.5")  # -> 95.5
        getFloat("42")  # -> None (Integer data is not a supported Float input...)
        getFloat("invalid")  # -> None (Value Not Acceptable for <class 'float'> type input...)
        ```
    
    Note:
        Returns `None` on validation failure, allowing retry loop in caller.

__________________________________________________________________________________
                                                                           2025@MO
    """
    result=tryLoop(float, userin)

    if '.' not in userin and isinstance(result, float):
        print('\tInteger data is not a supported Float input...')
    elif isinstance(result, float):
        return result


def getInt(userin: str) -> int | None:
    """
    Integer input validation rejecting float-formatted input.
    
    Validates string input as `int` type with strict format checking.
    Rejects any input containing decimal point to prevent float-to-int confusion.
    
    Signature:
        ```python
        def getInt(userin: str) -> int | None
        ```
    
    Parameters:
        ```python
        userin: str  # Raw user input string to validate
        ```
    
    Returns:
        ```python
        int | None  # Validated integer if successful, None if invalid
        ```
    
    Validation Rules:
        - Must not contain decimal point ('.')
        - Must be convertible to `int` type
        - Rejects float-format numbers (e.g., "42.0" rejected, "42" accepted)
    
    Examples:
        ```python
        getInt("42")  # -> 42
        getInt("42.0")  # -> None (Float data not support input for integer...)
        getInt("invalid")  # -> None (Value Not Acceptable for <class 'int'> type input...)
        ```
    
    Note:
        Pre-validates format before type conversion to provide clear error messages.

__________________________________________________________________________________
                                                                           2025@MO
    """
    # Check if input contains a decimal point before converting
    if '.' in userin:
        print('\tFloat data not support input for integer...')
        return None

    return tryLoop(int, userin)

def getStr(userin: str) -> str | None:
    """
    String input validation rejecting empty and pure numerical input.
    
    Validates string input with content requirements and numerical rejection.
    Ensures meaningful text input by blocking empty strings and numeric data.
    
    Signature:
        ```python
        def getStr(userin: str) -> str | None
        ```
    
    Parameters:
        ```python
        userin: str  # Raw user input string to validate
        ```
    
    Returns:
        ```python
        str | None  # Validated string if successful, None if invalid
        ```
    
    Validation Rules:
        - Must not be empty or whitespace-only
        - Must not be pure numerical data (`int` or `float` format)
        - Must contain at least one non-digit character
    
    Examples:
        ```python
        getStr("Alice")  # -> 'Alice'
        getStr("   ")  # -> None (Empty inputs not accepted...)
        getStr("42")  # -> None (String input cannot be numerical data...)
        getStr("42.5")  # -> None (String input cannot be numerical data...)
        getStr("Player1")  # -> 'Player1' (alphanumeric allowed)
        ```
    
    Note:
        Allows alphanumeric strings (e.g., "Player1") but rejects pure numbers.
        Handles negative numbers and decimals in numerical detection.

__________________________________________________________________________________
                                                                           2025@MO
    """
    result = tryLoop(str, userin)

    if not result.strip():
        print('\tEmpty inputs not accepted...')
    elif result.replace('.', '', 1).replace('-', '', 1).isdigit():
        print('\tString input cannot be numerical data (int or float)...')
    else:
        return result


def tryLoop(varType: type, userin: str):
    """
    Type conversion wrapper with exception handling.
    
    Attempts to convert user input string to target type with graceful error handling.
    Provides user-friendly error messages for conversion failures.
    
    Signature:
        ```python
        def tryLoop(varType: type, userin: str) -> varType | None
        ```
    
    Parameters:
        ```python
        varType: type  # Target type for conversion (int, float, str, etc.)
        userin: str  # Input string to convert
        ```
    
    Returns:
        ```python
        varType | None  # Converted value if successful, None if conversion fails
        ```
    
    Error Handling:
        ```python
        ValueError  # Input format incompatible with target type
        TypeError  # Type operation not supported for input
        ```
    
    Examples:
        ```python
        tryLoop(int, "42")  # -> 42
        tryLoop(float, "3.14")  # -> 3.14
        tryLoop(int, "invalid")  # -> None (Value Not Acceptable for <class 'int'> type input...)
        ```
    
    Note:
        Helper function for validation methods. Not intended for direct external use.
        Returns `None` on any exception, allowing caller to handle retry logic.

__________________________________________________________________________________
                                                                           2025@MO
    """
    try:
        return varType(userin)
    except ValueError:
        print(f"\tValue Not Acceptable for {varType} type input...")
    except TypeError:
        print(f"\tDataType Not Acceptable for {varType} type input...")




        

