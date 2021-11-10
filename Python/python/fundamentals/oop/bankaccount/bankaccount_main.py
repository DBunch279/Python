from bankaccount import BankAccount
accounts = []
bankAccount1 = BankAccount(0.00, 400.0)
accounts.append(bankAccount1)
bankAccount2 = BankAccount(0.02, 553.21)
accounts.append(bankAccount2)
bankAccount3 = BankAccount(0.05, 125.12)
accounts.append(bankAccount3)
bankAccount4 = BankAccount(0.06, 58.51)
accounts.append(bankAccount4)
def main():
    for i in range(0, 3):
        bankAccount1.deposit(200.0)
    bankAccount1.withdraw(50.0)

    for j in range(0, 2):
        bankAccount2.deposit(50.0)
    for k in range(0, 4):
        bankAccount2.withdraw(30.2)
    for o in range(0, len(accounts)):
        accounts[o].display_account_info()
    
if(__name__ == "__main__"):
    main()