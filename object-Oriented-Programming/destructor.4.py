class BankAccount:
    def _init_(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        print(f"Account created for {self.name} with Account Number: {self.account_number}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully. Current Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully. Current Balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def _del_(self):
        print(f"Account for {self.name} is being deleted.")

# Create an instance of BankAccount
account1 = BankAccount("Izyan", "1234567890", 500)  # Constructor called

# Perform deposit and withdrawal operations
account1.deposit(200)
account1.withdraw(100)

# Manually delete the account instance
del account1  # Destructor called manually
