# ⌨️ Input and Output in Python

Input and Output (I/O) are used to interact with users.

- **Input** → Taking data from the user.
- **Output** → Displaying data to the user.

---

## 📖 What is Output?

Output is information displayed on the screen.

Python uses the `print()` function to display output.

### Syntax

```python
print(value)
```

### Example

```python
print("Hello, World!")
```

### Output

```text
Hello, World!
```

---

## 🖥 Multiple Outputs

```python
name = "Tanmay"
age = 18

print(name)
print(age)
```

### Output

```text
Tanmay
18
```

---

## ⌨️ What is Input?

Input allows users to enter data during program execution.

Python uses the `input()` function.

### Syntax

```python
input("Message")
```

### Example

```python
name = input("Enter your name: ")

print(name)
```

### Input

```text
Tanmay
```

### Output

```text
Tanmay
```

---

## 🔄 Input Always Returns a String

```python
age = input("Enter your age: ")

print(type(age))
```

### Output

```text
<class 'str'>
```

---

## 🔢 Converting Input to Integer

```python
age = int(input("Enter your age: "))

print(age)
print(type(age))
```

### Output

```text
18
<class 'int'>
```

---

## 📏 Converting Input to Float

```python
height = float(input("Enter your height: "))

print(height)
```

### Example Output

```text
5.9
```

---

## 🏷️ Formatted Output using f-Strings

f-Strings make output cleaner and more readable.

### Syntax

```python
f"text {variable}"
```

### Example

```python
name = "Tanmay"
age = 18

print(f"My name is {name} and I am {age} years old.")
```

### Output

```text
My name is Tanmay and I am 18 years old.
```

---

## ✨ Escape Characters

Escape characters add special formatting.

| Escape Character | Meaning |
|-----------------|---------|
| \n | New Line |
| \t | Tab Space |
| \' | Single Quote |
| \" | Double Quote |
| \\ | Backslash |

### Example

```python
print("Hello\nWorld")
```

### Output

```text
Hello
World
```

---

## 🎯 Complete Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}")
print(f"You are {age} years old.")
```

### Sample Input

```text
Tanmay
18
```

### Output

```text
Hello Tanmay
You are 18 years old.
```

---

## ⚠ Common Mistakes

### Forgetting Type Conversion

```python
age = input("Enter age: ")

print(age + 5)
```

Error:

```text
TypeError
```

Correct:

```python
age = int(input("Enter age: "))

print(age + 5)
```

---

## 🧠 Practice Questions

### Beginner

1. Take a user's name as input and print it.
2. Take a user's age and print it.
3. Print a welcome message.

### Intermediate

1. Take two numbers and print their sum.
2. Take a user's city and display it using an f-string.
3. Print text using escape characters.

### Advanced

1. Create a simple student information program.
2. Take name, age, and city as input and display them neatly.
3. Build a mini calculator using user input.

---

## 🎯 Summary

- Use `print()` to display output.
- Use `input()` to take input from users.
- `input()` returns a string by default.
- Use `int()` and `float()` for conversion.
- f-Strings provide clean formatting.
- Escape characters help format text.

---

Happy Coding! 🚀