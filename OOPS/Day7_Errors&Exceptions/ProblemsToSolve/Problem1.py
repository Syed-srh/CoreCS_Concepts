# 1: Safe Division System
# Design a program to safely perform division.

# Features to be implemented
# Create function divide(a, b)
# Accept inputs from user
# Handle below exceptions:
# ValueError → invalid input
# ZeroDivisionError → division by zero
# Add functionality:
# Print result if valid
# Print appropriate error messages otherwise
# Additional Requirements
# Program should not terminate on error
# Allow multiple attempts

def divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Division operation completed.")

# Example usage:
if __name__ == "__main__":
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            divide(a, b)
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        finally:
            print("Division operation completed.")

# This program allows users to perform division while handling potential exceptions gracefully. It continues to prompt the user until valid input is provided or the program is interrupted.
