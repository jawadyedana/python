class BankAccount:
    def _init_(self, owner, balance):
        # Public attribute
        self.owner = owner
        # Private attribute
        self._balance = balance

    # Getter method to access private balance
    def get_balance(self):
        return self._balance

    # Setter method to update private balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}. New Balance: {self._balance}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}. Remaining Balance: {self._balance}")
        else:
            print("Insufficient balance or invalid amount!")

# Creating an account object
account = BankAccount("Gauraav", 5000)

# Accessing Public attribute
print("Account Owner:", account.owner)

# Accessing Private attribute using method
print("Initial balance:", account.get_balance())

# Depositing and withdrawing money
account.deposit(2000)
account.withdraw(1000)
