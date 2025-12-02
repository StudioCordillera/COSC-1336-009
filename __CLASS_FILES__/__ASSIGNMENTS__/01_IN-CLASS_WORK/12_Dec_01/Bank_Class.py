# BANK CLASS
import os
from dataclasses import dataclass


@dataclass
class Bank:
    def __init__(self, balance):

        self.name = str
        self.balance = balance

    # Getters
    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance
    
    # Setters
    def set_name(self, name):
        self.name = name

    def set_balance(self, balance):
        self.balance = balance    

def displayBalance(b1 = Bank):
    return b1.get_balance()