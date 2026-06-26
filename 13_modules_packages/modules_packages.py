"""
=========================================
Python Basics - Modules & Packages
Author: Tanmay Pathe
=========================================
"""

# Importing Modules

import math
import random
from datetime import datetime

# math Module

print("Square Root of 81:", math.sqrt(81))
print("Factorial of 5:", math.factorial(5))
print("Value of Pi:", math.pi)

# random Module

print("\nRandom Number:", random.randint(1, 100))

# datetime Module

print("\nCurrent Date & Time:")
print(datetime.now())

# Creating Your Own Module Example
# (Suppose calculator.py exists)

# import calculator
# print(calculator.multiply(5, 4))