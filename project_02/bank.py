class BankAccount:
    number_of_accounts = 0 # # CLASS attribute: shared by ALL instances, like Java's `static`.

    def __init__(self, owner, password, balance=0.0):
        self.owner = owner
        self.password = password
        self.balance = balance
        self.history = []
        BankAccount.number_of_accounts += 1

    def __str__(self):
        return f'Name: {self.owner}, Balance: {self.balance}'

    def deposit(self, amount, memo=None):
        self.balance += amount
        if memo:
            self.history.append(memo)

    def withdraw(self, amount, memo=None):
        self.balance -= amount
        if memo:
            self.history.append(memo)

    def transfer(self, to, amount, memo=None):
        self.balance -= amount
        to.deposit(amount)
        if memo:
            self.history.append(memo)