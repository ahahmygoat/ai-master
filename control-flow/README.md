---
# 🔁 Python Control Flow: Conditional Statements & Loops

Control flow allows your program to make decisions and repeat actions based on conditions. Python provides powerful tools like `if`, `elif`, `else`, `for`, and `while` to manage how your code executes.
---

## 🧠 Conditional Statements

### Syntax Overview

- **`if`**: Executes a block of code if the condition is `True`.
- **`elif`**: (short for "else if") Adds additional conditions after the initial `if`.
- **`else`**: Executes a block of code if none of the previous conditions are `True`.

### ✅ Example: Checking a Condition

```python
num = 15

if num > 10:
    print("Positive Number")
elif num == 0:
    print("Number = 0")
else:
    print("Negative Number")
```

#### 🔍 Output:

```
Positive Number
```

### 🧪 Additional Tips

- Use comparison operators: `>`, `<`, `==`, `!=`, `>=`, `<=`
- Combine conditions with logical operators: `and`, `or`, `not`
- Indentation matters! Python uses indentation to define code blocks.

---

## 🔄 Loops in Python

Loops allow you to repeat actions efficiently.

### 🔁 Types of Loops

#### **`for` Loop**

- Iterates over a sequence (like a list, tuple, string, or range).
- Example:
  ```python
  for fruit in ["apple", "banana", "cherry"]:
      print(fruit)
  ```

#### **`while` Loop**

- Repeats as long as a condition is `True`.
- Example:
  ```python
  count = 0
  while count < 3:
      print("Counting:", count)
      count += 1
  ```

---

## 🧩 Looping Over Different Objects

- **Strings**:
  ```python
  for char in "hello":
      print(char)
  ```
- **Lists**:
  ```python
  for item in [1, 2, 3]:
      print(item)
  ```
- **Tuples**:
  ```python
  for pair in [(1, 2), (3, 4)]:
      print(pair)
  ```
- **Range**:
  ```python
  for i in range(5):
      print(i)
  ```

---

## 🛑 Controlling Loop Execution

### `break`

- Terminates the loop when a condition is met.
- Example:
  ```python
  for i in range(10):
      if i == 5:
          break
      print(i)
  ```

### `continue`

- Skips the current iteration and moves to the next.
- Example:
  ```python
  for i in range(5):
      if i == 2:
          continue
      print(i)
  ```
