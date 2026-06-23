# 🧩 Functions in Python

Functions are reusable blocks of code that perform a specific task.

Instead of writing the same code multiple times, you can write it once inside a function and call it whenever needed.

---

# 📖 What is a Function?

A function is a block of organized, reusable code designed to perform a specific task.

### Example

```python
def greet():
    print("Hello, World!")

greet()
```

### Output

```text
Hello, World!
```

---

# 📝 Defining a Function

Use the `def` keyword to create a function.

### Syntax

```python
def function_name():
    # code block
```

### Example

```python
def welcome():
    print("Welcome to Python!")

welcome()
```

### Output

```text
Welcome to Python!
```

---

# 📞 Calling a Function

A function only runs when it is called.

### Example

```python
def greet():
    print("Hello")

greet()
greet()
```

### Output

```text
Hello
Hello
```

---

# 📥 Function Parameters

Parameters allow functions to accept data.

### Syntax

```python
def function_name(parameter):
    # code block
```

### Example

```python
def greet(name):
    print(f"Hello, {name}")

greet("Tanmay")
```

### Output

```text
Hello, Tanmay
```

---

# 📤 Return Statement

The `return` statement sends a value back to the caller.

### Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

### Output

```text
30
```

---

# 🎯 Multiple Parameters

```python
def student(name, age):
    print(name, age)

student("Tanmay", 18)
```

### Output

```text
Tanmay 18
```

---

# ⚙️ Default Parameters

Default values are used if no argument is provided.

### Example

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Tanmay")
```

### Output

```text
Hello, Guest
Hello, Tanmay
```

---

# 🏷️ Keyword Arguments

Arguments can be passed using parameter names.

### Example

```python
def student(name, age):
    print(name, age)

student(age=18, name="Tanmay")
```

### Output

```text
Tanmay 18
```

---

# 📦 *args

Allows multiple positional arguments.

### Example

```python
def total(*numbers):
    print(numbers)

total(10, 20, 30)
```

### Output

```text
(10, 20, 30)
```

---

# 📚 **kwargs

Allows multiple keyword arguments.

### Example

```python
def student(**details):
    print(details)

student(name="Tanmay", age=18)
```

### Output

```text
{'name': 'Tanmay', 'age': 18}
```

---

# 🔁 Recursion

A function calling itself.

### Example

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)
```

### Output

```text
5
4
3
2
1
```

---

# 🌍 Variable Scope

Scope determines where a variable can be accessed.

## Local Variable

```python
def demo():
    x = 10
    print(x)

demo()
```

## Global Variable

```python
x = 100

def demo():
    print(x)

demo()
```

---

# 🌍 Real-World Example

### Calculator Function

```python
def add(a, b):
    return a + b

print(add(5, 3))
```

### Output

```text
8
```

---

# ⚠ Common Mistakes

## Forgetting Parentheses

Wrong:

```python
greet
```

Correct:

```python
greet()
```

---

## Missing Return

Wrong:

```python
def add(a, b):
    a + b
```

Correct:

```python
def add(a, b):
    return a + b
```

---

# 🧠 Practice Questions

## Beginner

1. Create a function that prints your name.
2. Create a function to add two numbers.
3. Create a function that prints a welcome message.

## Intermediate

1. Create a function that finds the square of a number.
2. Create a function with default parameters.
3. Create a function that accepts multiple arguments.

## Advanced

1. Create a factorial function using recursion.
2. Create a calculator using functions.
3. Create a student management system using functions.

---

# 🎯 Summary

- Functions make code reusable.
- Use `def` to create functions.
- Parameters allow data input.
- `return` sends values back.
- Default arguments provide fallback values.
- `*args` handles multiple positional arguments.
- `**kwargs` handles multiple keyword arguments.
- Recursion allows a function to call itself.

---

Happy Coding! 🚀