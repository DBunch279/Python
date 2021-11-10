class BankAccount:
    int_rate = 0.0
    balance = 0
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account_info(self):
        print("Balance: " + str(self.balance))

    def yield_interest(self):
        if(self.int_rate > 0):
            self.balance += self.balance * self.int_rate