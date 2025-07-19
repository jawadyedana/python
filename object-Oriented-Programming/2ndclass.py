# banking system ACP
class Account:
    # constructor
    def _init_(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs {amount} from account no {self.account_number} was debited")
        print(f"Total Balance: {self.get_balance()}")

    def credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} to account no {self.account_number} was credited")
        print(f"Total Balance: {self.get_balance()}")

    def get_balance(self):
        return self.balance

# Example usage
acc1_obj = Account(10000, 2345) # object cretion
acc1_obj.debit(3000)

acc2_obj = Account(40000, 3413) # object creation
acc2_obj.credit(3000)
