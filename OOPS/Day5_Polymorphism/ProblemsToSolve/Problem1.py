# 1: Payment Processing System
# Complete the  Payment, CreditCard, and UPI classes.

# Payment class:
# Add below methods:
# process_payment() : Prints generic payment message
# CreditCard class:
# Inherits from Payment.

# Features to be added
# Override:
# process_payment() : Prints "Processing credit card payment"
# UPI class:
# Inherits from Payment.

# Features to be added
# Override:
# process_payment() : Prints "Processing UPI payment"
# Additional Requirement
# Create a list of objects (CreditCard, UPI)
# Iterate and call process_payment()

class Payment:
    def process_payment(self):
        print("Generic payment message")
class CreditCard(Payment):
    def process_payment(self):
        print("Processing credit card payment")
class UPI(Payment):
    def process_payment(self):
        print("Processing UPI payment")
# Create a list of objects (CreditCard, UPI)
payments = [CreditCard(), UPI()]

# Iterate and call process_payment()
for payment in payments:
    payment.process_payment()

 