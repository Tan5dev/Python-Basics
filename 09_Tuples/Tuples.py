"""
=========================================
Python Basics - Tuples
Author: Tanmay Pathe
=========================================
"""

# Creating a Tuple

fruits = ("Apple", "Banana", "Mango")

print("Tuple:", fruits)

# Accessing Items

print("First Item:", fruits[0])
print("Last Item:", fruits[-1])

# Tuple Length

print("Length:", len(fruits))

# Membership Check

print("Apple" in fruits)

# Looping Through Tuple

print("\nTuple Items:")

for fruit in fruits:
    print(fruit)

# Packing

student = ("Tanmay", 18, "Pune")

print("\nPacked Tuple:", student)

# Unpacking

name, age, city = student

print("Name:", name)
print("Age:", age)
print("City:", city)

# Tuple Methods

numbers = (1, 2, 2, 3, 2)

print("\nCount:", numbers.count(2))
print("Index:", numbers.index(3))

# Joining Tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("Joined Tuple:", tuple1 + tuple2)