# 🔢 Sets in Python

Sets are used to store multiple unique values in a single variable.

Unlike lists and tuples, sets do not allow duplicate values.

---

# 📖 What is a Set?

A set is an unordered, mutable collection of unique elements.

### Example

```python
fruits = {"Apple", "Banana", "Mango"}

print(fruits)
```

### Output

```text
{'Apple', 'Banana', 'Mango'}
```

---

# 📝 Creating a Set

### Syntax

```python
set_name = {value1, value2, value3}
```

### Example

```python
numbers = {1, 2, 3, 4, 5}
```

---

# 🎯 Duplicate Values

Sets automatically remove duplicates.

### Example

```python
numbers = {1, 2, 2, 3, 4, 4, 5}

print(numbers)
```

### Output

```text
{1, 2, 3, 4, 5}
```

---

# 📏 Set Length

Use `len()` to count items.

### Example

```python
numbers = {1, 2, 3}

print(len(numbers))
```

### Output

```text
3
```

---

# 🔍 Checking Items

### Example

```python
fruits = {"Apple", "Banana", "Mango"}

print("Apple" in fruits)
```

### Output

```text
True
```

---

# ➕ Adding Items

## add()

Adds a single item.

### Example

```python
fruits = {"Apple", "Banana"}

fruits.add("Mango")

print(fruits)
```

### Output

```text
{'Apple', 'Banana', 'Mango'}
```

---

# ➕ Adding Multiple Items

## update()

### Example

```python
fruits.update(["Orange", "Grapes"])
```

### Output

```text
{'Apple', 'Banana', 'Orange', 'Grapes'}
```

---

# ❌ Removing Items

## remove()

Removes a specific item.

```python
fruits.remove("Banana")
```

⚠ Raises an error if item does not exist.

---

## discard()

```python
fruits.discard("Banana")
```

Does not raise an error.

---

## pop()

Removes a random item.

```python
fruits.pop()
```

---

## clear()

Removes all items.

```python
fruits.clear()
```

---

# 🔄 Looping Through Sets

### Example

```python
fruits = {"Apple", "Banana", "Mango"}

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

# 🤝 Union

Combines all unique values from two sets.

### Example

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
```

### Output

```text
{1, 2, 3, 4, 5}
```

---

# 🎯 Intersection

Returns common values.

### Example

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2))
```

### Output

```text
{2, 3}
```

---

# ➖ Difference

Returns values present in the first set but not in the second.

### Example

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.difference(set2))
```

### Output

```text
{1}
```

---

# ⚡ Symmetric Difference

Returns values present in either set but not both.

### Example

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.symmetric_difference(set2))
```

### Output

```text
{1, 4}
```

---

# 🌍 Real-World Example

### Remove Duplicate Values

```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)
```

### Output

```text
{1, 2, 3, 4, 5}
```

---

# ⚠ Common Mistakes

## Empty Set Creation

Wrong:

```python
my_set = {}
```

Output:

```text
<class 'dict'>
```

This creates a dictionary.

Correct:

```python
my_set = set()
```

---

## Using Indexing

Wrong:

```python
fruits[0]
```

Error:

```text
TypeError
```

Sets do not support indexing because they are unordered.

---

# 🧠 Practice Questions

## Beginner

1. Create a set of 5 numbers.
2. Add a new item.
3. Remove an item.

## Intermediate

1. Find the union of two sets.
2. Find the intersection of two sets.
3. Remove duplicate values from a list.

## Advanced

1. Create a student attendance tracker.
2. Compare two sets of data.
3. Find unique visitors from two website logs.

---

# 🎯 Summary

- Sets store unique values.
- Sets are unordered and mutable.
- Duplicate values are automatically removed.
- Sets support powerful mathematical operations.
- Union combines values.
- Intersection finds common values.
- Difference finds unique values.
- Sets are excellent