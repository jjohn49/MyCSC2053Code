class Bank:

    def __init__(self,account_number,account_balance):
        self.account_number = account_number
        self.account_balance = account_balance

    def __str__(self):
        return str(self.account_number) + " " + str(self.account_balance)

    def deposit(self,amount):
        self.account_balance += amount

    def withdraw(self,amount):
        self.account_balance -= amount

    def get_balance(self):
        return self.account_balance
