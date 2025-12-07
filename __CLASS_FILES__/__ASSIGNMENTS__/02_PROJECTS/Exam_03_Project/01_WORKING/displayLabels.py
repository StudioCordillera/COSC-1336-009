"""
Display Labels Module

Provides formatting constants and boilerplate display functions for program headers
and footers. Simplifies consistent visual styling across project outputs.

Public API (__all__):
    ```python
    ['START', 'END', 'nL', 'tab', 'tab1', 'longBar', 'medBar', 'shortBar', 'dashGraph', 'lineGraph']
    ```

Function Signatures:
    ```python
    START() -> None
    END() -> None
    ```

Constant Variables:
    ```python
    nL: str = '\\n'
    tab: str = '    '  # 4 spaces
    tab1: str = '     '  # 5 spaces
    longBar: str = '--------------------------------------------------------------------------------'  # 80 dashes
    medBar: str = '--------------------------------------------------'  # 50 dashes
    shortBar: str = '------------'  # 12 dashes
    dashGraph: str = '------------------------------------------------------------'  # 60 dashes
    lineGraph: str = '____________________________________________________________'  # 60 underscores
    ```

Module Metadata:
    ```python
    __version__ = '1.0'
    __author__ = 'Matthew Ochoa'
    __date__ = 'December 6, 2025'
    ```

Usage:
    from displayLabels import START, END, longBar, nL
    
    START()  # Display program header
    print("Program content")
    END()    # Display program footer

Author: Matthew Ochoa
Date: December 6, 2025
Version: 1.0
"""

__all__ = ['START', 'END', 'nL', 'tab', 'tab1', 'longBar', 'medBar', 'shortBar', 'dashGraph', 'lineGraph']
__version__ = '1.0'
__author__ = 'Matthew Ochoa'
__date__ = 'December 6, 2025'

nL = '\n'
"""NewLine"""
tab= f"{' '*4}"
"""Tab = 4 spaces"""
tab1 = f"{' '*5}"
"""Tab + 1 space"""
longBar = f"{'-'*80}"
"""x80 count of - symbols for a line"""
medBar = f"{'-'*50}"
"""50 count of - symbols for a line"""
shortBar = f"{'-'*12}"
"""12 count of - symbols for a line"""
dashGraph = f"{'-'*60}"
"""60 count of _ symbols for a line"""
lineGraph = f"{'_'*60}"
"""60 count of - symbols for a line"""



# Display Start of Program Boiler SOPB
#  ------------------------------------------------------------------------
def START() -> None:
    """
    Display Start of Program Boiler (SOPB).
    
    Prints formatted program header with project title, author, and date information.
    Uses module formatting constants for consistent visual styling.
    
    Signature:
        ``def START() -> None``
    
    :return: None (outputs directly to console)
    :rtype: None
    
    Output Format:
        -------------------------------------------------------------------------
         Start of Project 4
         Written by: Matthew Ochoa
         Date: 11/25/2025
        -------------------------------------------------------------------------
        
          PROGRAM NAME | PURPOSE
        -------------------------------------------------------------------------

__________________________________________________________________________________
                                                                           2025@MO
    """
    print(tab1+longBar+nL+tab+'Start of Project 4')
    print(tab1+'Written by: Matthew Ochoa')
    print(tab1+'Date: 11/25/2025 ')
    print(tab,longBar)
    print(nL+'  PROGRAM NAME | PURPOSE')
    print(tab+longBar+nL)

# Display End of Program Boiler EOPB
#  ------------------------------------------------------------------------
def END() -> None:
    """
    Display End of Program Boiler (EOPB).
    
    Prints formatted program footer signaling program completion.
    Uses module formatting constants for consistent visual styling.
    
    Signature:
        ``def END() -> None``
    
    :return: None (outputs directly to console)
    :rtype: None
    
    Output Format:
        -------------------------------------------------------------------------
        
         End of Project
        -------------------------------------------------------------------------

__________________________________________________________________________________
                                                                           2025@MO
    """
    print(tab+longBar+nL)
    print(tab1+'End of Project')
    print(tab+longBar)    



'''
 △▽△▽△▽△▽△▽△▽△▽△▽
◢◤◢◤◢◤◢◤◢◤◢◤◢◤
◤◢◣◥◤◢◣◥◤◢◣◥◤◢◣◥
# ========== Section Name ==========

'''