# Name      Ally Baba
# Date      February 7 2020
# Program   dictionary
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# Delete

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name']; # remove entry with key 'Name'
print("Dictionary after deleting Key:Name is : ", dict.keys())

dict.clear();     # remove all entries in dict
print("Dictionary after clearing the dictionary is : ", dict.keys())

del dict ;        # delete entire dictionary

#print ("dict['Age']: ", dict['Age'])   Error message
#print ("dict['School']: ", dict['School']) Error message


