# Python OOP Users
from user_old import User

def main():
    josh = User(5000, "Josh")
    will = User(9000, "Will")
    pam = User(7000, "Pam")
    
    josh.display_user_balance()
    will.display_user_balance()
    pam.display_user_balance()

    print("")
    print("Josh Desposits a Bunch of Money for stuff + 2000 (x3)")
    for i in range(0, 3):
        josh.make_deposit(2000)
    josh.display_user_balance()

    print("")
    print("Josh Buys Coke out of Coke Machine - $3000 [I know that is alot for coke right]")
    josh.make_withdrawal(3000).display_user_balance()
    josh.display_user_balance()

    print("")
    print("Will Makes two Deposits and two Widthdrawals + 1000(x2) - 250(x2)")
    for i in range(0, 2):
        will.make_deposit(1000)
    for i in range(0, 2):
        will.make_withdrawal(250)
    will.display_user_balance()

    print("")
    print("Pam makes one deposit for a bonus check and three widthdrawals + 6000 - 250(x3)")
    pam.make_deposit(6000)
    for i in range(0, 3):
        pam.make_withdrawal(250)
    pam.display_user_balance()

    print("")
    print("Josh Transfers Money into Pam's account for some reason? Josh 2750 -> Pam")
    josh.transfer_money(pam, 2750).display_user_balance()
    pam.display_user_balance()

    print("")
    print("Pam is now the Richest")

if __name__ == "__main__":
    main()