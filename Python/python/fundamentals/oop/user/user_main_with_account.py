#Python OOP User With Account
from bankaccount.bankaccount import BankAccount
from user_account import User

def main():
    dave = User("Dave", BankAccount(0.00, 5000), BankAccount(0.05, 10000))
    dave.checking.deposit(4000)
    dave.checking.display_account_info()
    dave.savings.yield_interest()
    dave.savings.display_account_info()

if(__name__ == "__main__"):
    main()