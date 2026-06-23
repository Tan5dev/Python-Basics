"""
=========================================
Python Basics - Operators
Author: Tanmay Pathe
=========================================
"""

a = 10
b = 3

# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Comparison Operators
print("\nGreater Than:", a > b)
print("Equal To:", a == b)

# Logical Operators
print("\nLogical AND:", a > 0 and b > 0)

# Membership Operators
numbers = [10, 20, 30]
print("\nMembership:", 10 in numbers)

# Identity Operators
x = [1, 2]
y = x

print("Identity:", x is y)

# Bitwise Operators
print("\nBitwise AND:", a & b)