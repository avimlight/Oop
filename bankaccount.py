class BalanceException(Exception):
    pass


class BankAccount:
    # its likes creeating an acount and initaializing with some amount
    def __init__(self, initialAmount, aactName):
        self.balance = initialAmount
        self.Name = aactName
        print(f"\n Account {self.Name} created\n Balance equals {self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount {self.Name} and the balance is {self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete....")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry account {self.Name} only has a balance of {self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw succesfull")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interuupted {error}")

    def transfer(self, amount, account):
        try:
            print("\n*********\n\nBegining Transfer")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n transfer completed......")
        except BalanceException as error:
            print(f"\nTransfer interrupted*** {error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit completed man")
        self.getBalance()


class SavingsAcct(InterestRewardsAccount):
    def __init__(self, initialAmount, aactName):
        super().__init__(initialAmount, aactName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n withdraw completed")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted :{error}")
