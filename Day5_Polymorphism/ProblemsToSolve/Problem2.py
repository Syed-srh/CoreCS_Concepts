# 2: Notification System
# Complete the Notification, EmailNotification, and SMSNotification classes.

# Notification class:
# Add method:
# send() : Prints generic notification
# EmailNotification class:
# Inherits from Notification.

# Override:
# send() : Prints email-specific message
# SMSNotification class:
# Inherits from Notification.

# Override:
# send() : Prints SMS-specific message
# Additional Requirement
# Store objects in a list
# Call send() using loop

class Notification:
    def send(self):
        print("Sending a generic notification")
class EmailNotification(Notification):
    def send(self):
        print("Sending an email notification")
class SMSNotification(Notification):
    def send(self):
        print("Sending an SMS notification")
# Create a list of objects (EmailNotification, SMSNotification)
notifications = [EmailNotification(), SMSNotification()]

# Call send() using a loop
for notification in notifications:
    notification.send()
    