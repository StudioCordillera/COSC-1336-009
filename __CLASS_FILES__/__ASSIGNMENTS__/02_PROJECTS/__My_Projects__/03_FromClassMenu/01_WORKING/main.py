########################################
## Matthew Ochoa                   #####
## MONTH ##, #yr#                  #####
## Project: ##                     #####
## Status: In - Progress           #####
## Class: COSC 1336                #####
########################################
import os
from modules.UI_LIBRARY.typeValidation import ValidateUI
V = ValidateUI.validateInput


#  Item Management System | With Setup
# --------------------------------------------

''' Objectives 

    - Menu UI class
    - Repository Class
    - Elements functionality
    
    setup.py:
        1) load element config from .txt file
        2) generate collections_class config from new elements class
        3) generate UI_Class config from collections and elements class


        
'''

def main():

    # Testing Input Validation
    print(V(bool, '\tProvide a Boolean: '))
    print(V(int, '\tProvide a integer: '))
    print(V(float, '\tProvide a float: '))
    print(V(str, '\tProvide a string: '))






main()