class BankAccount:

    def __init__(self, owner, balance):
        if balance <= 0:
            raise ValueError("Balance must be greater than 0.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Amount cannot exceed current balance.")
        self.balance -= amount

    def transfer(self, amount, target_account):
        self.withdraw(amount)
        target_account.deposit(amount)

    def __str__(self):
        return f"{self.owner}'s account | Balance: ${self.balance:.2f}"


acc1 = BankAccount("John", 500)
acc2 = BankAccount("Jane", 300)

acc1.deposit(200)
print(acc1)                      # John's account | Balance: $700.00

acc1.withdraw(100)
print(acc1)                      # John's account | Balance: $600.00

acc1.transfer(150, acc2)
print(acc1)                      # John's account | Balance: $450.00
print(acc2)                      # Jane's account | Balance: $450.00

# acc3 = BankAccount("Bob", -100)  # raises ValueError