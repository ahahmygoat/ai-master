---
# 🔁 Python Control Flow: Conditional Statements

Control flow allows your program to make decisions and execute code based on conditions. Python uses `if`, `elif`, and `else` statements to control the flow of execution.
---

## 🧠 Syntax Overview

- **`if`**: Executes a block of code if the condition is `True`.
- **`elif`**: (short for "else if") Adds additional conditions after the initial `if`.
- **`else`**: Executes a block of code if none of the previous conditions are `True`.

---

## ✅ Example: Checking a Condition

```python
num = 15

if num > 10:
    print("Positive Number")
elif num == 0:
    print("Number = 0")
else:
    print("Negative Number")
```

### 🔍 Output:

```
Positive Number
```

---

## 🧪 Additional Tips

- Conditions use comparison operators like `>`, `<`, `==`, `!=`, `>=`, `<=`.
- You can combine conditions using logical operators: `and`, `or`, `not`.
- Indentation is critical in Python—blocks under `if`, `elif`, and `else` must be indented consistently.

---

## 🧩 Example: Multiple Conditions

```python
temperature = 75

if temperature > 85:
    print("It's hot outside.")
elif temperature > 65:
    print("It's warm outside.")
else:
    print("It's cool outside.")
```

---
