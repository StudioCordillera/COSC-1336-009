# Type Validation tools for UI class

class ValidateUI:
    

    @staticmethod
    def validateInput(varType, prompt):

        dataTypes = {float:ValidateUI.getFloat,int:ValidateUI.getInt,str:ValidateUI.getStr}

        while True:
            if varType is bool:
                return ValidateUI.getBool()
            else:
                result = dataTypes[varType](input(prompt))
                if result is not None:
                    return result

    @staticmethod
    def getBool() -> bool:

        while True:
            userin=input('\tEnter \'T\' for true or \'F\' for false... ')

            if userin.upper() == 'T':
                return True
            elif userin.upper() == 'F':
                return False
            else:
                print('\tINVALID OPTION...')

    @staticmethod
    def getFloat(userin):

        result=ValidateUI.tryLoop(float, userin)

        if '.' not in userin and isinstance(result, float):
            print('\tInteger data is not a supported Float input...')
        elif isinstance(result, float):
            return result

    @staticmethod
    def getInt(userin):

        # Check if input contains a decimal point before converting
        if '.' in userin:
            print('\tFloat data not support input for integer...')
            return None

        return ValidateUI.tryLoop(int, userin)


    @staticmethod
    def getStr(userin):

        result=ValidateUI.tryLoop(str, userin)

        if not result.strip():
            print('\tEmpty inputs not accepted...')
        elif result.replace('.', '', 1).replace('-', '', 1).isdigit():
            print('\tString input cannot be numerical data (int or float)...')
        else:
            return result


    @staticmethod
    def tryLoop(varType:type, userin):

        try:
            return varType(userin)
        except ValueError:
            print(f"\tValue Not Acceptable for {varType} type input...")
        except TypeError:
            print(f"\tDataType Not Acceptable for {varType} type input...")




        

