---
# 🧺 Python Data Structures

Python offers several built-in data structures that help organize and manage data efficiently. These include **lists**, **tuples**, **dictionaries**, and **sets**—each with unique properties and use cases.
---

## 📋 Lists

### What Are Lists?

- Ordered, **mutable** collections that can hold elements of **any data type**.
- Lists are ideal for storing sequences of items that may change over time.

### Creating Lists

```python
fruits = ["apple", "banana", "cherry"]
```

### Accessing Elements

- **By index**:
  ```python
  print(fruits[0])  # Output: apple
  ```
- **Negative indexing** (starts from the end):
  ```python
  print(fruits[-1])  # Output: cherry
  ```

### Modifying Lists

```python
fruits[1] = "blueberry"
fruits.append("date")
fruits.remove("apple")
```

### Slicing Lists

```python
print(fruits[1:3])  # Output: ['blueberry', 'cherry']
```

---

## 📦 Tuples

### What Are Tuples?

- Ordered, **immutable** collections.
- Once created, their elements **cannot be changed**.

### Creating Tuples

```python
coordinates = (10, 20)
```

### Accessing Elements

```python
print(coordinates[0])  # Output: 10
```

### Immutability

- You **cannot** modify or append to a tuple:
  ```python
  coordinates[0] = 15  # ❌ Error
  ```

---

## 🗂️ Dictionaries

### What Are Dictionaries?

- Unordered collections of **key-value pairs**.
- Keys must be unique and immutable; values can be any type.

### Creating Dictionaries

```python
person = {"name": "Alice", "age": 30}
```

### Accessing and Modifying Data

```python
print(person["name"])  # Output: Alice
person["age"] = 31
person["city"] = "Seattle"
```

---

## 🧮 Sets

### What Are Sets?

- Unordered collections of **unique** items.
- Useful for removing duplicates and performing set operations.

### Creating Sets

```python
colors = {"red", "green", "blue"}
```

### Adding and Removing Elements

```python
colors.add("yellow")
colors.remove("green")
```

### Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # Output: {1, 2, 3, 4, 5}
```

---
