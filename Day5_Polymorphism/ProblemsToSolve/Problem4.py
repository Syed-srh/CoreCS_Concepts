# 4: Logger System (Singleton)
# Complete the  Logger class.

# Features to be added
# Add class variable:
# _instance = None
# Override __new__():
# Ensure only one instance is created
# Add method:
# log(message) : Prints message
# Additional Requirement
# Create multiple objects
# Verify both refer to same instance

class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def log(self, message):
        print(message)
# Create multiple objects
logger1 = Logger()
logger2 = Logger()
# Verify both refer to same instance
print(logger1 is logger2)  # Output: True