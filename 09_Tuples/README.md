# 📦 Tuples in Python

Tuples are used to store multiple items in a single variable.

They are similar to lists, but unlike lists, tuples are **immutable**, meaning their values cannot be changed after creation.

---

# 📖 What is a Tuple?

A tuple is an ordered, immutable collection of items.

### Example

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits)
```

### Output

```text
('Apple', 'Banana', 'Mango')
```

---

# 📝 Creating a Tuple

### Syntax

```python
tuple_name = (item1, item2, item3)
```

### Example

```python
colors = ("Red", "Green", "Blue")
```

---

# 🔢 Accessing Tuple Items

Tuples use indexing just like lists.

### Example

```python
colors = ("Red", "Green", "Blue")

print(colors[0])
print(colors[1])
```

### Output

```text
Red
Green
```

---

# 🔄 Negative Indexing

```python
colors = ("Red", "Green", "Blue")

print(colors[-1])
```

### Output

```text
Blue
```

---

# ✂️ Tuple Slicing

### Syntax

```python
tuple[start:end]
```

### Example

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

### Output

```text
(20, 30, 40)
```

---

# 🔒 Immutability

Tuples cannot be modified after creation.

### Example

```python
colors = ("Red", "Green", "Blue")

colors[0] = "Yellow"
```

### Output

```text
TypeError
```

---

# 📏 Tuple Length

Use `len()` to count items.

### Example

```python
colors = ("Red", "Green", "Blue")

print(len(colors))
```

### Output

```text
3
```

---

# 🔍 Checking Items

```python
colors = ("Red", "Green", "Blue")

print("Red" in colors)
```

### Output

```text
True
```

---

# 🔄 Looping Through Tuples

```python
colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)
```

### Output

```text
Red
Green
Blue
```

---

# 📦 Tuple Packing

Packing means storing multiple values into a tuple.

### Example

```python
student = ("Tanmay", 18, "Pune")

print(student)
```

### Output

```text
('Tanmay', 18, 'Pune')
```

---

# 📤 Tuple Unpacking

Unpacking extracts values from a tuple.

### Example

```python
student = ("Tanmay", 18, "Pune")

name, age, city = student

print(name)
print(age)
print(city)
```

### Output

```text
Tanmay
18
Pune
```

---

# ⚙️ Tuple Methods

Python tuples have only two built-in methods.

## count()

Returns how many times a value appears.

```python
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
```

### Output

```text
3
```

---

## index()

Returns the first occurrence index.

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

### Output

```text
1
```

---

# 🔗 Joining Tuples

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)
```

### Output

```text
(1, 2, 3, 4, 5, 6)
```

---

# 🌍 Real-World Example

### Student Record

```python
student = ("Tanmay", 18, "Computer Science")

print(student)
```

### Output

```text
('Tanmay', 18, 'Computer Science')
```

Tuples are useful when data should not be modified accidentally.

---

# ⚠ Common Mistakes

## Forgetting the Comma in Single-Item Tuple

Wrong:

```python
fruit = ("Apple")
```

This becomes a string.

Correct:

```python
fruit = ("Apple",)
```

### Output

```text
<class 'tuple'>
```

---

## Trying to Modify a Tuple

Wrong:

```python
colors[0] = "Yellow"
```

Error:

```text
TypeError
```

---

# 🧠 Practice Questions

## Beginner

1. Create a tuple of 5 fruits.
2. Print the first and last item.
3. Find the length of a tuple.

## Intermediate

1. Use tuple slicing.
2. Use `count()` and `index()`.
3. Check whether an item exists in a tuple.

## Advanced

1. Create a student record using tuples.
2. Practice tuple packing and unpacking.
3. Join two tuples together.

---

# 🎯 Summary

- Tuples store multiple values.
- Tuples are ordered and immutable.
- Tuples use indexing and slicing.
- Tuples support packing and unpacking.
- Only `count()` and `index()` methods are available.
- Tuples are useful for fixed data that should not change.

---

Happy Coding! 🚀