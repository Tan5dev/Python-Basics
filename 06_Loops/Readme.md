# 🔁 Loops in Python

Loops are used to execute a block of code repeatedly.

Instead of writing the same code multiple times, loops help automate repetitive tasks.

---

# 📖 What is a Loop?

A loop allows a program to repeat a set of instructions until a condition is met.

### Example

```python
for i in range(5):
    print("Hello")
```

### Output

```text
Hello
Hello
Hello
Hello
Hello
```

---

# 📚 Types of Loops in Python

Python provides two main loops:

1. for Loop
2. while Loop

---

# 🔄 for Loop

A `for` loop is used to iterate over a sequence.

### Syntax

```python
for variable in sequence:
    # code block
```

### Example

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

---

# 🎯 range() Function

The `range()` function generates a sequence of numbers.

### Syntax

```python
range(start, stop, step)
```

### Examples

```python
range(5)
```

Output:

```text
0 1 2 3 4
```

```python
range(1, 6)
```

Output:

```text
1 2 3 4 5
```

```python
range(1, 10, 2)
```

Output:

```text
1 3 5 7 9
```

---

# 📝 Looping Through a String

```python
name = "Tanmay"

for letter in name:
    print(letter)
```

### Output

```text
T
a
n
m
a
y
```

---

# 📋 Looping Through a List

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

# 🔁 while Loop

A `while` loop runs as long as a condition remains True.

### Syntax

```python
while condition:
    # code block
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Output

```text
1
2
3
4
5
```

---

# ⛔ break Statement

Used to immediately stop a loop.

### Example

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### Output

```text
0
1
2
3
4
```

---

# ⏭ continue Statement

Skips the current iteration and moves to the next one.

### Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### Output

```text
0
1
3
4
```

---

# 🚧 pass Statement

Used as a placeholder when no code is needed.

### Example

```python
for i in range(5):
    pass
```

---

# 🪆 Nested Loops

A loop inside another loop.

### Example

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

### Output

```text
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

---

# ⭐ Pattern Example

```python
for i in range(5):
    print("*" * i)
```

### Output

```text

*
**
***
****
```

---

# 🌍 Real-World Example

### Multiplication Table

```python
number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

### Output

```text
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

# ⚠ Common Mistakes

## Infinite Loop

Wrong:

```python
count = 1

while count <= 5:
    print(count)
```

This never stops because `count` is not updated.

Correct:

```python
count += 1
```

---

## Wrong Indentation

Wrong:

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

# 🧠 Practice Questions

## Beginner

1. Print numbers from 1 to 10.
2. Print your name 5 times.
3. Print all even numbers from 1 to 20.

## Intermediate

1. Create a multiplication table.
2. Find the sum of numbers from 1 to 100.
3. Print a star pattern.

## Advanced

1. Reverse a string using a loop.
2. Count vowels in a string.
3. Create a number guessing game loop.

---

# 🎯 Summary

- for loops iterate over sequences.
- while loops run while a condition is True.
- range() generates number sequences.
- break exits a loop.
- continue skips an iteration.
- pass acts as a placeholder.
- Nested loops allow complex repetition.

---

Happy Coding! 🚀