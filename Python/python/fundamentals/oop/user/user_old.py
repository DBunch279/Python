# Python OOP Users
class User:
    name = ""
    amount = 0
    def __init__(self, account_amount, name):
        self.amount = account_amount
        self.name = name
    
    def display_user_balance(self):
        print(self.name + "'s Current Balance is : " + str(self.amount))
        return self

    def make_deposit(self, amount_added):
        self.amount += amount_added
        return self

    def make_withdrawal(self, amount_taken):
        self.amount -= amount_taken
        return self
    
    def transfer_money(self, other_user, amount):
        other_user.amount += amount
        self.make_withdrawal(amount)
        return self