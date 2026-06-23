"""
=========================================
Python Basics - Functions
Author: Tanmay Pathe
=========================================
"""

# Simple Function

def greet():
    print("Hello, World!")

greet()

# Function with Parameters

def welcome(name):
    print(f"Welcome, {name}")

welcome("Tanmay")

# Return Statement

def add(a, b):
    return a + b

print("Sum:", add(10, 20))

# Default Parameter

def greet_user(name="Guest"):
    print(f"Hello, {name}")

greet_user()
greet_user("Tanmay")

# *args

def total(*numbers):
    print("Numbers:", numbers)

total(10, 20, 30)

# **kwargs

def student(**details):
    print(details)

student(name="Tanmay", age=18)

# Recursion

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)