"""
=========================================
Python Basics - Exception Handling
Author: Tanmay Pathe
=========================================
"""

# ZeroDivisionError

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Multiple Exceptions

try:
    number = int(input("\nEnter a number: "))
    print(100 / number)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Operation completed successfully.")
finally:
    print("Execution finished.")

# Raising an Exception

try:
    age = -5

    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as error:
    print(error)

# Custom Exception

class InvalidAgeError(Exception):
    """Raised when an invalid age is provided."""
    pass

try:
    age = -1

    if age < 0:
        raise InvalidAgeError("Invalid age entered.")
except InvalidAgeError as error:
    print(error)