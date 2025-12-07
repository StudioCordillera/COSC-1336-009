# BANK CLASS
import os
from collections import ChainMap


class Account:


    def __init__(self, internalID:int = 0, AccountID:str = 'aID', AccountHolder:str = 'Name', Checkings:float = 0.00, Fees:float = 0.00, Balance:float = 0.00):
        self.AccountID = AccountID
        self.AccountHolder = AccountHolder
        self.Checkings = Checkings
        self.Fees = Fees
        self.Balance = Balance
        self.ledger:list = []

    if __name__ == "__Bank__":
        def changeAccount(self):
            """
            docstring
            """
            pass





class Bank:
    def __init__(self):
        self.Registry = {}
    
    def registerAccount(self, Account:object):
        self.Registry=ChainMap(Account)

    def __name__(self):
        return "__Bank__"

    


    



'''
def firstRun():
    timeCode:time = time.asctime()
    tCat = [['w', 'Withdraw'],['P', 'Purchase'], ['D', 'Deposit'], ['E', 'End']]
    tType = [['C', 'Credit', '+'],['D', 'Debit', '-']]
    amount:float = 0.00
    LedgerEntry:list = [timeCode, tCat, amount, tType]

    


    new_account = {
        internalID:{
            'InternalID': internalID,
            'AccountID': AccountID,
            'Account Holder': AccountHolder,
            'Checkings': Checkings,
            'Fees': Fees,
            'Balance': Balance,
            'Ledger': Ledger
        }
    }



    print(accounts)
'''

def main():

    
    acct1 = Account(1,'powers1', 'Powers, Roger', 10000, 0, 1000)
    BankReg=Bank()

    BankReg.__dict__

    print(acct1.__dict__)
    print(BankReg.__dict__)


main()


