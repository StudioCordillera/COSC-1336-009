
###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 10, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   MODULE: Display Labels                                    |
|_____________________________________________________________|
|                                                             |
|   - Provides static methods for UI banners and labels       |
|                                                             |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class Labels:

    # Display Start of Program Boiler SOPB
    #  ------------------------------------------------------------------------
    @staticmethod
    def projectStart():
        print(' ' * 4, '-'* 80, '\n',' ' * 4, 'Start of Project 4')
        print(' ' * 5, 'Written by: Matthew Ochoa')
        print(' ' * 5,'Date: 11/25/2025 ')
        print(' ' * 4,'-' * 80)
        Labels.bannersTitle()


    # Display End of Program Boiler EOPB
    #  ------------------------------------------------------------------------
    @staticmethod
    def projectEnd():
        print('\n',' ' * 4,'-' * 80)
        print( ' ' * 5, 'End of Project')
        print(' ' * 4,'-' * 80)    


    @staticmethod
    def bannersTitle():
        print('\tSearch Student Information')
        print(' ' * 4,'-' * 80)

    @staticmethod
    def bannersQuery():
        print('\n',' ' * 4,'-' * 80)
        print('\tQuery Sumary: Student Information')
        print(' ' * 4,'-' * 80)


    '''
    
    
    △▽△▽△▽△▽△▽△▽△▽△▽
    ◢◤◢◤◢◤◢◤◢◤◢◤◢◤
    ◤◢◣◥◤◢◣◥◤◢◣◥◤◢◣◥
    # ========== Section Name ==========
    
    '''


    
'''

Project #8 
Written by: Ally Baba 
----------------------------------------------- 
    Search Student Information 
    -------------------------------------------------------------------------------- 
        Are you ready to search? (Y/N) Y 
        Please enter a student ID: A007 
    
    -------------------------------------------------------------------------------- 
    Query Summary: Student Information  
    -------------------------------------------------------------------------------- 
        Student Found 
        Name: Ally Baba 
        ID: A007 
    
        Are you ready to search? (Y/N) Y 
        Please enter a student ID: X007 
    
    -------------------------------------------------------------------------------- 
    Query Summary: Student Information  
    -------------------------------------------------------------------------------- 
        Student Not Found 
        Are you ready to search? (Y/N) N 
        You have searched 2 times 
 
-------------------------------------------------------------------------------- 
End of Project 8 
 


'''
