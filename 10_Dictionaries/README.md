# 📖 Dictionaries in Python

Dictionaries are one of the most powerful and widely used data structures in Python.

They store data in **key-value pairs**, making data retrieval fast and efficient.

---

# 📚 What is a Dictionary?

A dictionary is an unordered, mutable collection of key-value pairs.

### Example

```python
student = {
    "name": "Tanmay",
    "age": 18,
    "city": "Pune"
}

print(student)
```

### Output

```text
{'name': 'Tanmay', 'age': 18, 'city': 'Pune'}
```

---

# 📝 Creating a Dictionary

### Syntax

```python
dictionary_name = {
    "key": value
}
```

### Example

```python
person = {
    "name": "John",
    "age": 25
}
```

---

# 🔍 Accessing Values

Use the key name.

### Example

```python
student = {
    "name": "Tanmay",
    "age": 18
}

print(student["name"])
```

### Output

```text
Tanmay
```

---

# ✅ Using get()

Safely retrieves values.

### Example

```python
print(student.get("age"))
```

### Output

```text
18
```

---

# ➕ Adding Items

### Example

```python
student["course"] = "Python"

print(student)
```

### Output

```text
{
'name': 'Tanmay',
'age': 18,
'course': 'Python'
}
```

---

# ✏️ Updating Items

### Example

```python
student["age"] = 19

print(student)
```

### Output

```text
{'name': 'Tanmay', 'age': 19}
```

---

# ❌ Removing Items

## pop()

```python
student.pop("age")
```

---

## popitem()

Removes the last inserted item.

```python
student.popitem()
```

---

## del

```python
del student["name"]
```

---

## clear()

```python
student.clear()
```

Removes all items.

---

# 📏 Dictionary Length

### Example

```python
student = {
    "name": "Tanmay",
    "age": 18
}

print(len(student))
```

### Output

```text
2
```

---

# 🔄 Looping Through Dictionaries

## Keys

```python
for key in student:
    print(key)
```

### Output

```text
name
age
```

---

## Values

```python
for value in student.values():
    print(value)
```

### Output

```text
Tanmay
18
```

---

## Key-Value Pairs

```python
for key, value in student.items():
    print(key, value)
```

### Output

```text
name Tanmay
age 18
```

---

# 📋 Dictionary Methods

| Method | Description |
|----------|-------------|
| keys() | Returns all keys |
| values() | Returns all values |
| items() | Returns key-value pairs |
| get() | Returns value by key |
| update() | Updates dictionary |
| pop() | Removes item |
| clear() | Removes all items |

---

# 🪆 Nested Dictionaries

Dictionaries inside dictionaries.

### Example

```python
students = {
    "student1": {
        "name": "Tanmay",
        "age": 18
    },
    "student2": {
        "name": "Rahul",
        "age": 19
    }
}

print(students)
```

### Output

```text
{
 'student1': {'name': 'Tanmay', 'age': 18},
 'student2': {'name': 'Rahul', 'age': 19}
}
```

---

# 🌍 Real-World Example

### Student Information System

```python
student = {
    "name": "Tanmay",
    "course": "BSc Computer Science",
    "city": "Pune"
}

print(student["course"])
```

### Output

```text
BSc Computer Science
```

---

# ⚠ Common Mistakes

## Accessing a Non-Existing Key

Wrong:

```python
print(student["phone"])
```

Error:

```text
KeyError
```

Use:

```python
print(student.get("phone"))
```

Output:

```text
None
```

---

## Duplicate Keys

Wrong:

```python
data = {
    "name": "Tanmay",
    "name": "Rahul"
}
```

Output:

```text
{'name': 'Rahul'}
```

The last value overwrites previous ones.

---

# 🧠 Practice Questions

## Beginner

1. Create a dictionary storing your name and age.
2. Print a specific value using its key.
3. Add a new key-value pair.

## Intermediate

1. Update an existing value.
2. Remove a key-value pair.
3. Loop through all keys and values.

## Advanced

1. Create a student management system.
2. Create a nested dictionary.
3. Build a contact book using dictionaries.

---

# 🎯 Summary

- Dictionaries store data as key-value pairs.
- Keys must be unique.
- Dictionaries are mutable.
- Use `get()` for safe access.
- Use `items()` to iterate through key-value pairs.
- Nested dictionaries help organize complex data.

---

Happy Coding! 🚀