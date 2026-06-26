"""
=========================================
Python Basics - Strings
Author: Tanmay Pathe
=========================================
"""

# Creating Strings

text = "Python Programming"

print("Original String:", text)

# Length

print("Length:", len(text))

# Indexing

print("First Character:", text[0])
print("Last Character:", text[-1])

# Slicing

print("First 6 Characters:", text[:6])

# Upper & Lower

print("Upper:", text.upper())
print("Lower:", text.lower())

# Replace

print("Replace:", text.replace("Python", "Java"))

# Split

words = text.split()
print("Split:", words)

# Join

languages = ["Python", "Java", "C++"]
print("Join:", " | ".join(languages))

# Find

print("Find 'Pro':", text.find("Pro"))

# Count

print("Count of 'm':", text.count("m"))

# f-String

name = "Tanmay"
print(f"Welcome, {name}!")