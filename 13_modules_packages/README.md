# 📦 Modules & Packages in Python

Modules and packages help organize Python code into reusable and manageable files.

Instead of writing all your code in one file, you can split it into multiple modules and group related modules into packages.

---

# 📖 What is a Module?

A module is simply a Python file (`.py`) containing variables, functions, or classes that can be imported into another Python program.

### Example

Suppose we have a file named `calculator.py`.

```python
def add(a, b):
    return a + b
```

Now we can use it in another file.

```python
import calculator

print(calculator.add(10, 20))
```

### Output

```text
30
```

---

# 📝 Importing Modules

Python provides different ways to import modules.

## import

```python
import math

print(math.sqrt(25))
```

### Output

```text
5.0
```

---

## from ... import ...

```python
from math import sqrt

print(sqrt(49))
```

### Output

```text
7.0
```

---

## import ... as

```python
import math as m

print(m.pi)
```

### Output

```text
3.141592653589793
```

---

# 📚 Built-in Modules

Python includes many built-in modules.

| Module | Purpose |
|----------|----------|
| math | Mathematical operations |
| random | Generate random values |
| datetime | Work with dates and time |
| os | Operating system operations |
| sys | Python interpreter information |
| statistics | Statistical calculations |

---

# 🎲 random Module

```python
import random

print(random.randint(1, 10))
```

Example Output

```text
7
```

---

# ➗ math Module

```python
import math

print(math.sqrt(64))
print(math.factorial(5))
```

### Output

```text
8.0
120
```

---

# 📅 datetime Module

```python
from