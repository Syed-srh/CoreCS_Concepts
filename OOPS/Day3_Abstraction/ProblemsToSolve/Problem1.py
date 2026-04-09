#Abstraction

#Problem -- 1
  #Practice Scenario 1: Payment System
# Complete the Payment and UPIPayment / CardPayment classes by adding new features by following the instructions.

# Payment class:
# The Payment class should contain the necessary attributes and methods.

# Features to be added to Payment class:
# Add below attributes:

# amount
# transaction_id
# status (initialized as "Pending")
# Add below methods:

# process_payment() : Abstract method to process payment
# show_status() : Prints the payment status
# Subclasses:
# The UPIPayment and CardPayment classes inherit from Payment.

# Features to be added to subclasses:
# Add below methods:

# process_payment() : Implement payment logic specific to each payment type

class Payment:
    def __init__(self, amount, transaction_id, status="Pending"):
        self.amount = amount
        self.transaction_id = transaction_id
        self.status = status
    
    def process_payment(self):
        pass

    def show_status(self):
        print(f"Payment Status: {self.status}")


class UPIPayment(Payment):
    def process_payment(self):
        # Simulate UPI payment processing logic
        print(f"Processing UPI payment of {self.amount} with transaction ID {self.transaction_id}")
        self.status = "Completed"
        print("UPI payment successful")


class CardPayment(Payment):
    def process_payment(self):
        # Simulate card payment processing logic
        print(f"Processing card payment of {self.amount} with transaction ID {self.transaction_id}")
        self.status = "Completed"
        print("Card payment successful")

# Example usage
upi_payment = UPIPayment(1000, "TXN12345")
card_payment = CardPayment(2000, "TXN67890")

upi_payment.process_payment()
upi_payment.show_status()

card_payment.process_payment()
card_payment.show_status()
