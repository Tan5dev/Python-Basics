"""
=========================================
Python Basics - Lists
Author: Tanmay Pathe
=========================================
"""

# Creating a List

fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

# Accessing Items

print("First Item:", fruits[0])
print("Last Item:", fruits[-1])

# Adding Items

fruits.append("Orange")

print("After Append:", fruits)

# Inserting Items

fruits.insert(1, "Grapes")

print("After Insert:", fruits)

# Removing Items

fruits.remove("Banana")

print("After Remove:", fruits)

# Length

print("Length:", len(fruits))

# Looping

print("\nLooping Through List:")

for fruit in fruits:
    print(fruit)

# Sorting

numbers = [50, 10, 30, 20]

numbers.sort()

print("\nSorted Numbers:", numbers)

# List Comprehension

squares = [x * x for x in range(5)]

print("Squares:", squares)

# Nested List

matrix = [
    [1, 2],
    [3, 4]
]

print("Matrix:", matrix)