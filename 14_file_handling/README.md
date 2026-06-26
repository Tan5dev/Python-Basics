# 📂 File Handling in Python

File handling allows programs to create, read, write, update, and delete files stored on your computer.

It is an essential skill for working with text files, logs, configuration files, reports, and many real-world applications.

---

# 📖 What is File Handling?

File handling is the process of performing operations on files such as:

- Creating files
- Reading files
- Writing files
- Appending data
- Closing files

---

# 📝 Opening a File

Python uses the `open()` function.

### Syntax

```python
open(file_name, mode)
```

### Example

```python
file = open("sample.txt", "r")
```

---

# 📚 File Modes

| Mode | Description |
|------|-------------|
| `r` | Read (Default) |
| `w` | Write (Creates or overwrites a file) |
| `a` | Append (Adds data to the end of a file) |
| `x` | Create a new file (Fails if the file already exists) |
| `rb` | Read Binary |
| `wb` | Write Binary |

---

# 📖 Reading a File

## read()

Reads the entire file.

```python
file = open("sample.txt", "r")

print(file.read())

file.close()
```

---

## readline()

Reads one line.

```python
print(file.readline())
```

---

## readlines()

Returns all lines as a list.

```python
print(file.readlines())
```

---

# ✍️ Writing to a File

```python
file = open("sample.txt", "w")

file.write("Hello Python!")

file.close()
```

If the file already exists, its contents will be overwritten.

---

# ➕ Appending to a File

```python
file = open("sample.txt", "a")

file.write("\nWelcome to File Handling.")

file.close()
```

This keeps the existing content and adds new data at the end.

---

# 📄 Creating a New File

```python
file = open("new_file.txt", "x")

file.close()
```

---

# 🔒 Closing a File

Always close a file after using it.

```python
file.close()
```

Closing a file frees system resources and ensures all changes are saved.

---

# ⭐ Using the `with` Statement (Recommended)

The `with` statement automatically closes the file, even if an error occurs.

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

No need to call `close()` manually.

---

# ⚠ Handling File Errors

Trying to open a file that does not exist raises an error.

```python
try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
```

### Output

```text
File not found!
```

---

# 🌍 Real-World Example

### Save Student Information

```python
with open("students.txt", "a") as file:
    file.write("Tanmay,18,BSc Computer Science\n")
```

---

# ⚠ Common Mistakes

## Forgetting to Close the File

Wrong

```python
file = open("sample.txt", "r")

print(file.read())
```

The file remains open.

Correct

```python
file.close()
```

Or better:

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

---

## Using the Wrong File Mode

```python
open("sample.txt", "r")
```

If the file doesn't exist:

```text
FileNotFoundError
```

Use `"w"` or `"x"` if you want to create a new file.

---

# 🧠 Practice Questions

## Beginner

1. Create a text file.
2. Write your name into a file.
3. Read and display the contents of a file.

## Intermediate

1. Append a new line to an existing file.
2. Count the number of lines in a file.
3. Read a file line by line.

## Advanced

1. Build a student record system using files.
2. Copy the contents of one file to another.
3. Create a simple notes application.

---

# 🎯 Summary

- Use `open()` to work with files.
- Choose the correct file mode (`r`, `w`, `a`, `x`).
- Use `read()`, `readline()`, and `readlines()` to read data.
- Use `write()` to save data.
- Always close files, or use the `with` statement.
- Handle file-related errors using `try-except`.

---

Happy Coding! 🚀