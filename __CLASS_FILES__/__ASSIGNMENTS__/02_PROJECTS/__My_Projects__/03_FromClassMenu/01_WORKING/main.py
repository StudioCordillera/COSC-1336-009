########################################
## Matthew Ochoa                   #####
## MONTH ##, #yr#                  #####
## Project: ##                     #####
## Status: In - Progress           #####
## Class: COSC 1336                #####
########################################\
import os
import modules.Collections_Class, modules.Employee_Class, modules.UI_Class
import setupScript

#  Item Management System | With Setup
# --------------------------------------------

''' Objectives 
    
    setup.py:
        1) load element config from .txt file
        2) generate collections_class config from new elements class
        3) generate UI_Class config from collections and elements class
        
'''

def main():

    setupScript.setup()

    e1 = modules.Employee_Class.Employee()

    # print(e1.__module__)
    # print(e1.__dict__)

    for keys, values in enumerate(e1.__dict__):
        print(f"{keys}: { values}: {e1.__dict__[values]}")






main()