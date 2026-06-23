"""
=========================================
Python Basics - Loops
Author: Tanmay Pathe
=========================================
"""

# For Loop

print("For Loop:")

for i in range(5):
    print(i)

# While Loop

print("\nWhile Loop:")

count = 1

while count <= 5:
    print(count)
    count += 1

# Break Statement

print("\nBreak Example:")

for i in range(10):
    if i == 5:
        break
    print(i)

# Continue Statement

print("\nContinue Example:")

for i in range(5):
    if i == 2:
        continue
    print(i)

# Nested Loop

print("\nNested Loop:")

for i in range(3):
    for j in range(3):
        print(i, j)

# Multiplication Table

print("\nMultiplication Table of 5:")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")