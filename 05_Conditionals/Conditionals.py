"""
=========================================
Python Basics - Conditional Statements
Author: Tanmay Pathe
=========================================
"""

# Simple if

age = 18

if age >= 18:
    print("You are an adult.")

# if-else

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# if-elif-else

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Nested if

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can Drive")

# Match-Case

day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid Day")