class BankAccount:
    def _init_(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successful.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful.")
        else:
            print("Insufficient funds for withdrawal.")

    def get_balance(self):
        return self.balance

    def _str_(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: {self.balance}"



account1 = BankAccount("123456", "Rafik shah")
print(account1)
account1.deposit(1000)
account1.withdraw(500)
print("Current balance:", account1.get_balance())