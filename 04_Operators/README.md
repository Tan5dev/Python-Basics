# ➕ Operators in Python

Operators are special symbols used to perform operations on variables and values.

---

## 📖 What are Operators?

Operators allow us to perform calculations, comparisons, and logical operations.

### Example

```python
a = 10
b = 5

print(a + b)
```

### Output

```text
15
```

---

# 📚 Types of Operators in Python

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

---

# ➕ Arithmetic Operators

Used for mathematical calculations.

| Operator | Description | Example |
|----------|------------|----------|
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| // | Floor Division | a // b |
| % | Modulus | a % b |
| ** | Exponent | a ** b |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

### Output

```text
13
7
30
3.3333333333333335
3
1
1000
```

---

# 📝 Assignment Operators

Used to assign values.

| Operator | Example |
|----------|----------|
| = | x = 5 |
| += | x += 5 |
| -= | x -= 5 |
| *= | x *= 5 |
| /= | x /= 5 |

### Example

```python
x = 10

x += 5

print(x)
```

### Output

```text
15
```

---

# ⚖️ Comparison Operators

Used to compare values.

| Operator | Meaning |
|----------|---------|
| == | Equal To |
| != | Not Equal To |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal To |
| <= | Less Than or Equal To |

### Example

```python
a = 10
b = 5

print(a > b)
print(a == b)
```

### Output

```text
True
False
```

---

# 🔍 Logical Operators

Used to combine conditions.

| Operator | Meaning |
|----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses the result |

### Example

```python
age = 18

print(age >= 18 and age < 60)
```

### Output

```text
True
```

---

# 🆔 Identity Operators

Used to compare object identities.

| Operator | Meaning |
|----------|---------|
| is | Same Object |
| is not | Different Object |

### Example

```python
x = [1, 2]
y = x

print(x is y)
```

### Output

```text
True
```

---

# 📋 Membership Operators

Used to check if a value exists in a sequence.

| Operator | Meaning |
|----------|---------|
| in | Present |
| not in | Not Present |

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
```

### Output

```text
True
```

---

# ⚡ Bitwise Operators

Operate on binary values.

| Operator | Description |
|----------|-------------|
| & | AND |
| \| | OR |
| ^ | XOR |
| ~ | NOT |
| << | Left Shift |
| >> | Right Shift |

### Example

```python
a = 5
b = 3

print(a & b)
```

### Output

```text
1
```

---

# 🎯 Complete Example

```python
a = 10
b = 5

print("Addition:", a + b)
print("Greater:", a > b)
print("Logical:", a > 0 and b > 0)
print("Membership:", 10 in [10, 20, 30])
```

### Output

```text
Addition: 15
Greater: True
Logical: True
Membership: True
```

---

# ⚠ Common Mistakes

### Using = Instead of ==

Wrong:

```python
if a = 5:
```

Correct:

```python
if a == 5:
```

---

### Division Result Confusion

```python
10 / 3
```

Returns:

```text
3.3333333333333335
```

Use floor division if you need an integer:

```python
10 // 3
```

Returns:

```text
3
```

---

# 🧠 Practice Questions

## Beginner

1. Add two numbers.
2. Find the remainder of 15 divided by 4.
3. Calculate 2 raised to the power 5.

## Intermediate

1. Compare two numbers using comparison operators.
2. Check if a user is eligible to vote.
3. Use logical operators with multiple conditions.

## Advanced

1. Build a simple calculator.
2. Check membership in a list.
3. Experiment with bitwise operators.

---

# 🎯 Summary

- Operators perform actions on values and variables.
- Arithmetic operators handle calculations.
- Comparison operators compare values.
- Logical operators combine conditions.
- Membership operators check existence.
- Identity operators compare objects.
- Bitwise operators work with binary numbers.

---

Happy Coding! 🚀