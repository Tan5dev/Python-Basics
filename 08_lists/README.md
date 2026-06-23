# 📋 Lists in Python

Lists are one of the most powerful and commonly used data structures in Python.

A list can store multiple items in a single variable.

---

# 📖 What is a List?

A list is an ordered, mutable (changeable) collection of items.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

### Output

```text
['Apple', 'Banana', 'Mango']
```

---

# 📝 Creating a List

### Syntax

```python
list_name = [item1, item2, item3]
```

### Example

```python
numbers = [10, 20, 30, 40]
```

---

# 🔢 Accessing List Items

Lists use indexing.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
```

### Output

```text
Apple
Banana
```

---

# 🔄 Negative Indexing

Negative indexing starts from the end.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[-1])
```

### Output

```text
Mango
```

---

# ✂️ List Slicing

Extract a portion of a list.

### Syntax

```python
list[start:end]
```

### Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

### Output

```text
[20, 30, 40]
```

---

# ➕ Adding Items

## append()

Adds an item at the end.

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

### Output

```text
['Apple', 'Banana', 'Mango']
```

---

## insert()

Adds an item at a specific position.

```python
fruits.insert(1, "Orange")
```

### Output

```text
['Apple', 'Orange', 'Banana']
```

---

# ❌ Removing Items

## remove()

Removes a specific value.

```python
fruits.remove("Banana")
```

---

## pop()

Removes an item by index.

```python
fruits.pop(1)
```

---

## clear()

Removes all items.

```python
fruits.clear()
```

---

# 🔄 Updating Items

```python
fruits = ["Apple", "Banana"]

fruits[1] = "Mango"

print(fruits)
```

### Output

```text
['Apple', 'Mango']
```

---

# 🔍 Checking Items

```python
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
```

### Output

```text
True
```

---

# 📏 List Length

Use `len()`.

```python
fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))
```

### Output

```text
3
```

---

# 🔄 Looping Through Lists

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

### Output

```text
Apple
Banana
Mango
```

---

# 📊 Sorting Lists

## sort()

```python
numbers = [50, 10, 30, 20]

numbers.sort()

print(numbers)
```

### Output

```text
[10, 20, 30, 50]
```

---

## Reverse Sorting

```python
numbers.sort(reverse=True)
```

### Output

```text
[50, 30, 20, 10]
```

---

# 📄 Copying Lists

```python
numbers = [1, 2, 3]

new_numbers = numbers.copy()

print(new_numbers)
```

### Output

```text
[1, 2, 3]
```

---

# 🪆 Nested Lists

Lists inside lists.

```python
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix)
```

### Output

```text
[[1, 2], [3, 4]]
```

---

# ⚡ List Comprehension

A concise way to create lists.

### Example

```python
squares = [x * x for x in range(5)]

print(squares)
```

### Output

```text
[0, 1, 4, 9, 16]
```

---

# 🌍 Real-World Example

### Student Names

```python
students = ["Tanmay", "Rahul", "Amit"]

for student in students:
    print(student)
```

### Output

```text
Tanmay
Rahul
Amit
```

---

# ⚠ Common Mistakes

## Index Out of Range

Wrong:

```python
fruits = ["Apple"]

print(fruits[5])
```

Error:

```text
IndexError
```

---

## Using Wrong Method Name

Wrong:

```python
fruits.add("Mango")
```

Correct:

```python
fruits.append("Mango")
```

---

# 🧠 Practice Questions

## Beginner

1. Create a list of 5 fruits.
2. Print the first and last item.
3. Add a new fruit using `append()`.

## Intermediate

1. Remove an item from a list.
2. Sort a list of numbers.
3. Create a nested list.

## Advanced

1. Create a student management system using lists.
2. Use list comprehension to generate squares.
3. Find the largest number in a list.

---

# 🎯 Summary

- Lists store multiple values.
- Lists are ordered and mutable.
- Use indexing and slicing to access items.
- Use append(), insert(), remove(), and pop() to modify lists.
- List comprehensions provide a powerful shortcut.
- Lists are one of the most important Python data structures.

---

Happy Coding! 🚀