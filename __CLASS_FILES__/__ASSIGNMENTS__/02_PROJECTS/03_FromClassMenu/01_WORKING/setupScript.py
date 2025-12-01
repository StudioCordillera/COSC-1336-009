# Configuration Script
import os
import json
import modules.Collections_Class, modules.Employee_Class, modules.UI_Class

class Setup:
    def __init__(self, state, directory):
        self.state = state
        self.directory = directory

    def set_state(self, state):
        self.state = state
    def get_state(self):
        return self.state


def setup():
    getLastState()


def generateCollectionState(foundItems):
    e1 = modules.Employee_Class.Employee()
    data = e1.__dict__

    path = (f"{foundItems['__Collection__']}/Collection.json")
    with open (path,'w') as f:
        json.dump(data,f,indent=2)


def getLastState():
    targets = ['__Collection__', 'Collection.json']  # Fixed: Capital C
    foundItems = {'__Collection__':None, 'Collection.json': None}
    foundAll=True

    while foundAll:
        foundItems, foundAll = locateCollectionDir(targets, foundItems)
        generateCollectionState(foundItems)

    stateDir = {
        'collection files':{
            foundItems[0]:foundItems['__Collection__'],
            foundItems[1]:foundItems['Collection.json']
        },
        ''
    }




def locateCollectionDir(targets, foundItems):
    with os.scandir('.') as entries:
        for entry in entries:    
            if entry.is_file():
                if entry.name == targets[1]:
                    foundItems[entry.name] = entry.path
            elif entry.is_dir():
                if entry.name == targets[0]:
                    foundItems[entry.name] = entry.path
                    with os.scandir(entry.path) as subentries:
                        for subentry in subentries:
                            if subentry.name == targets[1]:
                                foundItems['Collection.json'] = subentry.path
                                break       

        
        if foundItems['__Collection__'] != None and foundItems['Collection.json'] != None:
            print(f"\tCollection folder found at {foundItems['__Collection__']}, file was found at {foundItems['Collection.json']}.")
            return foundItems, False
        elif foundItems['__Collection__'] == None and foundItems['Collection.json'] != None:
            print(f"\tCollection Folder not found, file was found at {foundItems['Collection.json']}.")
            return foundItems, True
        elif foundItems['__Collection__'] != None and foundItems['Collection.json'] == None:
            print(f"\tCollection folder found at {foundItems['__Collection__']}, file was not.")
            return foundItems, True
        else:
            print('\tCollection folder and files not found')
            os.mkdir('./__Collection__')
            foundItems['__Collection__'] = os.path.abspath('./__Collection__')
            return foundItems, True



setup()