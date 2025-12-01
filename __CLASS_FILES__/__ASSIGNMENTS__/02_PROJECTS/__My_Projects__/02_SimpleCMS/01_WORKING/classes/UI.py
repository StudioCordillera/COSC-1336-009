## UI Menu Class
import os
from dataclasses import dataclass
from collection import Collection
from element import Employee


# clearTerminal()
def clearTerminal():
    os.system('cls')


@dataclass
class UI:

    Collection = Collection()

    def simpleInput(self, prompt):
        userInput = input(prompt)
        return userInput

    def optionsMenu(self, prompt, options):
        while True:
            print(prompt)
            for key in options:
                print(f"{key}. {options[key]}")
            userInput = int(input())
            if userInput not in options.keys():
                print('\nNOT AN OPTION!!')
            else:
                return userInput
            

    def registrationFlow(self, stages, stage):

        option = stages[stage]['fields']['type'](self, prompt=(stages[stage]['fields']['prompt']),options=(stages[stage]['inputs']))
        option = stages[stage]['routes'][option]
        option = stages[option]['fields']['type'](self, prompt=stages[option]['fields']['prompt'])

        return option










            

def main():
    index = 1
    stage = 1
    stages = {

        1:{
            'operation':{
                'Register':'Employee'
            },

            'fields':{
                'type': UI.optionsMenu,
                'prompt': 'Choose an Option'
            },

            'inputs':{
                1: 'Register Employee',
                2: 'Confirm Employee'
            },

            'routes':{
                1:2,
                2:None
            }
        },

        2:{
            'operation':{
                'edit':'name'
            },
            'fields':{
                'type':UI.simpleInput,
                'prompt':'Insert name: '
            }}}
    ui1 = UI()


    option = ui1.registrationFlow(stages, stage)

    ui1.Collection.set_employee_name(option)
    ui1.Collection.saveState()


main()



