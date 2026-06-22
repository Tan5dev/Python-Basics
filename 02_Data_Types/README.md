# 🏷️ Data Types in Python

Data types specify the type of value a variable can store.

Python automatically determines the data type of a value when it is assigned to a variable.

---

## 📖 What is a Data Type?

A data type defines the kind of value stored in a variable.

### Example

```python
name = "Tanmay"
age = 18
height = 5.9
is_student = True
```

Here:

- `name` → String (`str`)
- `age` → Integer (`int`)
- `height` → Float (`float`)
- `is_student` → Boolean (`bool`)

---

## 📚 Common Python Data Types

| Data Type | Description | Example |
|------------|------------|---------|
| str | Text/String | "Hello" |
| int | Whole Numbers | 10 |
| float | Decimal Numbers | 3.14 |
| bool | True or False | True |
| list | Ordered Collection | [1,2,3] |
| tuple | Immutable Collection | (1,2,3) |
| set | Unordered Unique Values | {1,2,3} |
| dict | Key-Value Pairs | {"name":"Tanmay"} |

---

## 📝 Checking Data Types

Use the `type()` function.

### Example

```python
name = "Tanmay"
age = 18

print(type(name))
print(type(age))
```

### Output

```text
<class 'str'>
<class 'int'>
```

---

## 🔤 String (str)

Strings store text values.

### Example

```python
name = "Tanmay"

print(name)
print(type(name))
```

### Output

```text
Tanmay
<class 'str'>
```

---

## 🔢 Integer (int)

Integers store whole numbers.

### Example

```python
age = 18

print(age)
print(type(age))
```

### Output

```text
18
<class 'int'>
```

---

## 📏 Float (float)

Floats store decimal numbers.

### Example

```python
height = 5.9

print(height)
print(type(height))
```

### Output

```text
5.9
<class 'float'>
```

---

## ✅ Boolean (bool)

Booleans store either True or False.

### Example

```python
is_student = True

print(is_student)
print(type(is_student))
```

### Output

```text
True
<class 'bool'>
```

---

## 📋 List

Lists store multiple values and can be modified.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(type(fruits))
```

### Output

```text
['Apple', 'Banana', 'Mango']
<class 'list'>
```

---

## 📦 Tuple

Tuples store multiple values but cannot be modified.

### Example

```python
colors = ("Red", "Green", "Blue")

print(colors)
print(type(colors))
```

### Output

```text
('Red', 'Green', 'Blue')
<class 'tuple'>
```

---

## 🎯 Set

Sets store unique values.

### Example

```python
numbers = {1, 2, 3, 4}

print(numbers)
print(type(numbers))
```

### Output

```text
{1, 2, 3, 4}
<class 'set'>
```

---

## 📖 Dictionary

Dictionaries store data as key-value pairs.

### Example

```python
student = {
    "name": "Tanmay",
    "age": 18
}

print(student)
print(type(student))
```

### Output

```text
{'name': 'Tanmay', 'age': 18}
<class 'dict'>
```

---

## ⚠ Common Mistakes

### Forgetting Quotes for Strings

```python
name = Tanmay
```

Error:

```text
NameError
```

Correct:

```python
name = "Tanmay"
```

---

## 🧠 Practice Questions

### Beginner

1. Create a string variable for your name.
2. Create an integer variable for your age.
3. Create a float variable for your height.

### Intermediate

1. Create a list of 5 fruits.
2. Create a tuple of 3 colors.
3. Create a dictionary containing your name and age.

### Advanced

1. Use `type()` to display the type of each variable.
2. Create one variable for each major Python data type.

---

## 🎯 Summary

- Python has multiple built-in data types.
- Use `type()` to check a variable's type.
- Strings store text.
- Integers store whole numbers.
- Floats store decimal numbers.
- Booleans store True/False values.
- Lists, Tuples, Sets, and Dictionaries store collections of data.

---

Happy Coding! 🚀