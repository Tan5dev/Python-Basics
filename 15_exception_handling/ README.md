# ⚠️ Exception Handling in Python

Exception handling allows a program to deal with errors gracefully instead of crashing.

By handling exceptions, you can provide meaningful messages to users and keep your program running.

---

# 📖 What is an Exception?

An exception is an error that occurs while a program is running.

Without exception handling, the program stops immediately when an error occurs.

### Example

```python
number = 10 / 0
```

### Output

```text
ZeroDivisionError: division by zero
```

---

# 📝 The try-except Block

The `try` block contains code that may cause an exception.

The `except` block handles the exception.

### Syntax

```python
try:
    # Code that may cause an exception
except:
    # Code to handle the exception
```

### Example

```python
try:
    number = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

### Output

```text
You cannot divide by zero.
```

---

# 🎯 Handling Multiple Exceptions

A program may encounter different types of exceptions.

### Example

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

---

# 📚 Common Python Exceptions

| Exception | Description |
|-----------|-------------|
| `ZeroDivisionError` | Division by zero |
| `ValueError` | Invalid value |
| `TypeError` | Unsupported data type |
| `NameError` | Variable not defined |
| `IndexError` | Invalid list index |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | File does not exist |

---

# ✨ The else Block

The `else` block runs only if no exception occurs.

### Example

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", number)
```

---

# 🔒 The finally Block

The `finally` block always executes, whether an exception occurs or not.

### Example

```python
try:
    file = open("sample.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program finished.")
```

### Output

```text
Program finished.
```

---

# 🚨 Raising Exceptions

You can create your own exceptions using `raise`.

### Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

### Output

```text
ValueError: Age cannot be negative.
```

---

# 🏗 Creating Custom Exceptions

You can define your own exception classes.

### Example

```python
class InvalidAgeError(Exception):
    pass

age = -1

if age < 0:
    raise InvalidAgeError("Invalid age entered.")
```

---

# 🌍 Real-World Example

### ATM Withdrawal

```python
balance = 5000
amount = 7000

try:
    if amount > balance:
        raise ValueError("Insufficient balance.")
    balance -= amount
    print("Withdrawal successful.")
except ValueError as error:
    print(error)
```

### Output

```text
Insufficient balance.
```

---

# ⚠ Common Mistakes

## Using a Bare except

Wrong

```python
try:
    print(10 / 0)
except:
    print("Error")
```

This catches every exception, which can make debugging difficult.

Correct

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## Ignoring Exceptions

Wrong

```python
except:
    pass
```

Avoid silently ignoring errors unless there is a good reason.

---

# 🧠 Practice Questions

## Beginner

1. Handle division by zero.
2. Handle invalid user input.
3. Catch an `IndexError`.

## Intermediate

1. Use `else` with a `try-except` block.
2. Use `finally` to display a closing message.
3. Handle multiple exceptions in one program.

## Advanced

1. Create a custom exception.
2. Build an ATM withdrawal program using exceptions.
3. Create a file reader that handles missing files gracefully.

---

# 🎯 Summary

- Exceptions are runtime errors.
- Use `try` to write code that may fail.
- Use `except` to handle errors.
- Use `else` for code that runs when no exception occurs.
- Use `finally` for cleanup code that always executes.
- Use `raise` to generate exceptions manually.
- Create custom exceptions for specific situations.

---

Happy Coding! 🚀