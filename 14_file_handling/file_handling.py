"""
=========================================
Python Basics - File Handling
Author: Tanmay Pathe
=========================================
"""

# Writing to a File

with open("sample.txt", "w") as file:
    file.write("Welcome to Python File Handling!\n")
    file.write("This is the second line.\n")

print("Data written successfully.")

# Reading the File

with open("sample.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)

# Appending to the File

with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")

print("Data appended successfully.")

# Reading Line by Line

print("\nReading Line by Line:")

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

# Error Handling

try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("\nError: File not found.")