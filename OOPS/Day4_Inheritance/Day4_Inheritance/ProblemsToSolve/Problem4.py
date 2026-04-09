#4: Banking System (Multilevel Inheritance)
# Complete the  Account, SavingsAccount, and PremiumSavings classes.

# Account class:
# The Account class is the base class.

# Features to be added to Account class
# Add below attributes:
# account_number
# balance
# Add below methods:
# display_balance() : Prints account balance
# SavingsAccount class:
# The SavingsAccount class inherits from Account.

# Features to be added to SavingsAccount class
# Add below attributes:
# interest_rate
# Add below methods:
# calculate_interest() : Prints calculated interest
# PremiumSavings class:
# The PremiumSavings class inherits from SavingsAccount.

# Features to be added to PremiumSavings class
# Add below attributes:
# cashback_percentage
# Add below methods:
# display_features() : Prints interest_rate and cashback_percentage

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print(f"Interest: {interest}")

class PremiumSavingAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance, interest_rate)
        self.cash_back_percentage = 5

    def display_features(self):
        print(f"Interest Rate: {self.interest_rate}%, Cash Back: {self.cash_back_percentage}%")
        
# Example usage:
savings_account = SavingsAccount(567890, 0, 3) 
#here the 567890 is the account number, 0 is the initial balance and 3 is the interest rate
savings_account.balance = 1000
savings_account.display_balance()
savings_account.calculate_interest()

premium_savings_account = PremiumSavingAccount(567890, 0, 3)
premium_savings_account.balance = 2000
premium_savings_account.display_balance()
premium_savings_account.display_features()
premium_savings_account.calculate_interest()
