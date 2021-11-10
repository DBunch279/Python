from bankaccount.bankaccount import BankAccount
# Python OOP Users
class User:
    name = ""
    checking = None
    savings = None
    def __init__(self, name, checking, savings):
        self.name = name
        self.checking = checking
        self.savings = savings