# 🔀 Conditional Statements in Python

Conditional statements allow a program to make decisions based on conditions.

---

## 📖 What are Conditional Statements?

Conditional statements execute different blocks of code depending on whether a condition is True or False.

### Example

```python
age = 18

if age >= 18:
    print("You can vote.")
```

### Output

```text
You can vote.
```

---

# 📝 The if Statement

The `if` statement executes a block of code only if the condition is True.

### Syntax

```python
if condition:
    # code block
```

### Example

```python
marks = 80

if marks >= 40:
    print("Pass")
```

### Output

```text
Pass
```

---

# 🔄 if-else Statement

Used when there are two possible outcomes.

### Syntax

```python
if condition:
    # code
else:
    # code
```

### Example

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### Output

```text
Minor
```

---

# 🔀 if-elif-else Statement

Used when multiple conditions need to be checked.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

### Output

```text
Grade B
```

---

# 🪆 Nested if Statements

An `if` statement inside another `if` statement.

### Example

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
```

### Output

```text
Can drive
```

---

# ⚡ Short-Hand if

### Example

```python
age = 18

if age >= 18: print("Adult")
```

### Output

```text
Adult
```

---

# 🎯 Match-Case Statement (Python 3.10+)

Used as an alternative to multiple if-elif statements.

### Syntax

```python
match variable:
    case value:
        # code
```

### Example

```python
day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid Day")
```

### Output

```text
Monday
```

---

# 🔍 Comparison Operators in Conditions

| Operator | Meaning |
|-----------|----------|
| == | Equal To |
| != | Not Equal To |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal To |
| <= | Less Than or Equal To |

### Example

```python
x = 10

if x > 5:
    print("Greater")
```

---

# 🔗 Logical Operators in Conditions

| Operator | Meaning |
|----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses the result |

### Example

```python
age = 25

if age >= 18 and age <= 60:
    print("Eligible")
```

### Output

```text
Eligible
```

---

# 🌍 Real-World Example

### Voting Eligibility Checker

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

---

# 🎯 Complete Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

### Output

```text
Grade B
```

---

# ⚠ Common Mistakes

## Forgetting Colon (:)

Wrong:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

## Incorrect Indentation

Wrong:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

# 🧠 Practice Questions

## Beginner

1. Check whether a number is positive or negative.
2. Check whether a student passed or failed.
3. Check if a person is eligible to vote.

## Intermediate

1. Create a grade calculator.
2. Check if a number is even or odd.
3. Create a simple login system.

## Advanced

1. Build a menu-driven program using match-case.
2. Create a ticket booking eligibility checker.
3. Create a bank withdrawal validation system.

---

# 🎯 Summary

- `if` executes code when a condition is True.
- `if-else` handles two outcomes.
- `if-elif-else` handles multiple conditions.
- Nested if statements allow complex decision-making.
- Match-case provides a cleaner alternative to multiple conditions.
- Proper indentation is essential in Python.

---

Happy Coding! 🚀