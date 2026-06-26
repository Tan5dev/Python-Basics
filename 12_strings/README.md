# 📝 Strings in Python

Strings are one of the most commonly used data types in Python.

A string is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`).

---

# 📖 What is a String?

A string is used to store text data.

### Example

```python
name = "Tanmay"

print(name)
```

### Output

```text
Tanmay
```

---

# 📝 Creating Strings

### Syntax

```python
string_name = "Text"
```

### Examples

```python
name = "Tanmay"
city = 'Pune'

message = """Welcome
to
Python"""
```

---

# 📏 String Length

Use the `len()` function to find the number of characters.

### Example

```python
text = "Python"

print(len(text))
```

### Output

```text
6
```

---

# 🔢 String Indexing

Each character has an index.

```text
P  y  t  h  o  n
0  1  2  3  4  5
```

### Example

```python
text = "Python"

print(text[0])
print(text[5])
```

### Output

```text
P
n
```

---

# 🔄 Negative Indexing

Negative indexing starts from the end.

```text
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

### Example

```python
text = "Python"

print(text[-1])
```

### Output

```text
n
```

---

# ✂️ String Slicing

Extract part of a string.

### Syntax

```python
string[start:end]
```

### Example

```python
text = "Programming"

print(text[0:7])
```

### Output

```text
Program
```

---

# 🔄 String Concatenation

Join strings using `+`.

### Example

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

### Output

```text
Hello World
```

---

# 🔁 String Repetition

Repeat strings using `*`.

### Example

```python
print("Hi! " * 3)
```

### Output

```text
Hi! Hi! Hi!
```

---

# 🔍 Membership Operators

Check if a substring exists.

### Example

```python
text = "Python Programming"

print("Python" in text)
print("Java" in text)
```

### Output

```text
True
False
```

---

# 🔤 Common String Methods

## upper()

```python
text = "python"

print(text.upper())
```

Output

```text
PYTHON
```

---

## lower()

```python
text = "PYTHON"

print(text.lower())
```

Output

```text
python
```

---

## title()

```python
text = "python programming"

print(text.title())
```

Output

```text
Python Programming
```

---

## strip()

Removes leading and trailing spaces.

```python
text = "  Python  "

print(text.strip())
```

Output

```text
Python
```

---

## replace()

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output

```text
I like Python
```

---

## split()

Splits a string into a list.

```python
text = "Python Java C"

print(text.split())
```

Output

```text
['Python', 'Java', 'C']
```

---

## join()

Joins a list into a string.

```python
languages = ["Python", "Java", "C"]

print(", ".join(languages))
```

Output

```text
Python, Java, C
```

---

## find()

Returns the index of the first occurrence.

```python
text = "Python"

print(text.find("t"))
```

Output

```text
2
```

---

## count()

Counts occurrences.

```python
text = "banana"

print(text.count("a"))
```

Output

```text
3
```

---

# ✨ String Formatting

## f-Strings

```python
name = "Tanmay"
age = 18

print(f"My name is {name}. I am {age} years old.")
```

Output

```text
My name is Tanmay. I am 18 years old.
```

---

# 🌍 Real-World Example

```python
name = input("Enter your name: ")

print(f"Welcome, {name}!")
```

---

# ⚠ Common Mistakes

## Index Out of Range

Wrong

```python
text = "Python"

print(text[10])
```

Error

```text
IndexError
```

---

## Strings are Immutable

Wrong

```python
text = "Python"

text[0] = "J"
```

Error

```text
TypeError
```

Correct

```python
text = "Python"

text = "J" + text[1:]
```

Output

```text
Jython
```

---

# 🧠 Practice Questions

## Beginner

1. Print the first and last character of a string.
2. Convert a string to uppercase.
3. Count the number of characters.

## Intermediate

1. Reverse a string using slicing.
2. Replace a word in a sentence.
3. Split a sentence into words.

## Advanced

1. Check if a string is a palindrome.
2. Count vowels in a string.
3. Count the frequency of each character.

---

# 🎯 Summary

- Strings store text data.
- Strings are immutable.
- Use indexing and slicing to access characters.
- String methods simplify text manipulation.
- f-Strings provide clean and readable formatting.
- Strings are essential for almost every Python application.

---

Happy Coding! 🚀