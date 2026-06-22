# 📦 Variables in Python

Variables are containers used to store data values in a program.

---

## 📖 What is a Variable?

A variable is a name that refers to a value stored in memory.

### Example

```python
name = "Tanmay"
age = 18

print(name)
print(age)
```

---

## 📝 Syntax

```python
variable_name = value
```

### Example

```python
city = "Pune"
temperature = 30
```

---

## 📜 Rules for Naming Variables

### ✅ Valid Rules

- Must start with a letter (a-z, A-Z) or underscore (_)
- Can contain letters, numbers, and underscores
- Variable names are case-sensitive
- Can be of any length

### ❌ Invalid Rules

- Cannot start with a number
- Cannot contain spaces
- Cannot use Python keywords

---

## ✔ Valid Examples

```python
name = "Tanmay"
_age = 18
age1 = 18
first_name = "Tanmay"
```

---

## ❌ Invalid Examples

```python
1name = "Tanmay"
first name = "Tanmay"
class = "Python"
```

---

## 🎯 Multiple Assignment

Assign multiple values in a single line.

```python
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)
```

### Output

```text
10
20
30
```

---

## 🎯 Assign Same Value to Multiple Variables

```python
a = b = c = 100

print(a)
print(b)
print(c)
```

### Output

```text
100
100
100
```

---

## 🖥 Complete Example

```python
name = "Tanmay"
age = 18
height = 5.9
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)
```

### Output

```text
Name: Tanmay
Age: 18
Height: 5.9
Student: True
```

---

## ⚠ Common Mistakes

### Starting with a Number

```python
2age = 18
```

Error:

```text
SyntaxError
```

### Using Spaces

```python
first name = "Tanmay"
```

Error:

```text
SyntaxError
```

---

## 🧠 Practice Questions

### Beginner

1. Create a variable named `country` and store your country name.
2. Create variables for your name, age, and city.
3. Print all variables using `print()`.

### Intermediate

1. Assign three values in a single line.
2. Assign the same value to three variables.
3. Create meaningful variable names for a student record.

---

## 🎯 Summary

- Variables store data values.
- Use `=` to assign values.
- Follow naming rules carefully.
- Variables can hold different types of data.
- Python allows multiple assignments.

---

Happy Coding! 🚀