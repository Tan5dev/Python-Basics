"""
=========================================
Python Basics - Sets
Author: Tanmay Pathe
=========================================
"""

# Creating Sets

fruits = {"Apple", "Banana", "Mango"}

print("Set:", fruits)

# Adding Items

fruits.add("Orange")

print("\nAfter Add:")
print(fruits)

# Removing Items

fruits.remove("Banana")

print("\nAfter Remove:")
print(fruits)

# Membership Check

print("\nApple in Set:")
print("Apple" in fruits)

# Looping

print("\nLooping Through Set:")

for fruit in fruits:
    print(fruit)

# Set Operations

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("\nUnion:")
print(set1.union(set2))

print("\nIntersection:")
print(set1.intersection(set2))

print("\nDifference:")
print(set1.difference(set2))

print("\nSymmetric Difference:")
print(set1.symmetric_difference(set2))

# Removing Duplicates

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print("\nUnique Numbers:")
print(unique_numbers)