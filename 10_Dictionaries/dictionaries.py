"""
=========================================
Python Basics - Dictionaries
Author: Tanmay Pathe
=========================================
"""

# Creating Dictionary

student = {
    "name": "Tanmay",
    "age": 18,
    "city": "Pune"
}

print("Dictionary:", student)

# Accessing Values

print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding Items

student["course"] = "Python"

print("\nAfter Adding:", student)

# Updating Items

student["age"] = 19

print("After Updating:", student)

# Length

print("Length:", len(student))

# Looping

print("\nKeys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

# Nested Dictionary

students = {
    "student1": {
        "name": "Tanmay",
        "age": 18
    }
}

print("\nNested Dictionary:")
print(students)

# Removing Item

student.pop("city")

print("\nAfter Removing City:")
print(student)