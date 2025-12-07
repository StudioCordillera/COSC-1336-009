from collections import ChainMap
import enum
import json
import os
from typing import Iterable
from data_exploration import global_settings, user_preferences, project_config, workspace_settings, session_data, temporary_overrides, feature_flags, api_config, database_settings, cache_config, monitoring_config, notification_settings, billing_config, experimental_features


def getFile(path):

    with open(path, 'r') as file:
        for lines in file:
            print(lines)
    
def getUnison(listDicts):
    """
    Takes a list of dictionaries and categorizes all values by type into lists.
    Preserves all data including duplicates.
    
    Algorithm:
    1. Create empty lists for each type category
    2. Loop through each dictionary in the list
    3. Loop through each key-value pair in current dictionary
    4. Check value type (order matters: bool before int!)
    5. Append value to appropriate list
    """
    
    # Step 1: Initialize empty lists for each type category
    all_keys = []           # All keys across all dicts (preserves duplicates)
    strings = []            # String values
    booleans = []           # Boolean values
    numbers = []            # int and float values
    collections = []        # list, tuple, set values
    dict_items = []         # dict values
    none_values = []        # None values
    
    for d in enum(listDicts):
        dNames:



    # Step 2: Loop through each dictionary
    for dictionary in listDicts:
        
        # Step 3: Loop through each key-value pair
        for key, value in dictionary.items():
            
            # Collect all keys
            all_keys.append(key)
            
            # Step 4 & 5: Check type and append to appropriate list
            # ORDER MATTERS: bool must come before int (bool is subclass of int)
            
            if isinstance(value, bool):
                booleans.append(value)
            
            elif value is None:
                none_values.append(None)
            
            elif isinstance(value, str):
                strings.append(value)
            
            elif isinstance(value, (int, float)):
                numbers.append(value)
            
            elif isinstance(value, (list, tuple, set)):
                collections.append(value)
            
            elif isinstance(value, dict):
                dict_items.append(value)
        
        



    #print(f"Booleans: {booleans}")
    #print(f"Strings: {strings}")
    #print(f"Numbers: {numbers}")
    #print(f"Collections: {collections}")
    #print(f"Dicts: {dict_items}")




def main():

    listDicts = [global_settings, user_preferences, project_config, workspace_settings, session_data, temporary_overrides, feature_flags, api_config, database_settings, cache_config, monitoring_config, notification_settings, billing_config, experimental_features]

    #global_settings
    
    # global_settings
    # user_preferences
    # project_config
    # workspace_settings
    # session_data
    # temporary_overrides
    # feature_flags
    # api_config
    # database_settings
    # cache_config
    # monitoring_config
    # notification_settings
    # billing_config
    # experimental_features


    getUnison(listDicts)



main()

ChainMap()

