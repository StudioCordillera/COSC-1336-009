## UI Menu Class
import classes.collection
import classes.element

class UI:
    def __init__(self, running):
        self.running = running
        self.uiProvider(running)

    def uiProvider(self, running:bool):
        while running:
            flow = self.mainMenu()
            print(flow)


    def mainMenu(self):

        choices = ['New Registration', 'Modify Existing Item', 'Settings', 'Exit']
        prompt = '\tChoose your option:'

        flow = self.choicesMenu(choices,prompt)
        return flow
    
    def validateChoices(self, choices:list[str], userInput:str):

        if str(userInput).lower().strip() in choices:
            return True, userInput
        else:
            print('\tNOT A PROVIDED OPTION...')
            return False, None



    def choicesMenu(self, choices:list[str], prompt:str):
        inputs = []
        while not isValid:
            print(prompt)
            for count in range(0,len(choices)):
                inputs.append(count+1)
                print(f"\t{inputs[count]}. {choices[count]}")
            userInput = input()
            isValid, choice = self.validateChoices(choices, userInput)
        return choice
            





