---

# 🧠 Python Functions, Scope, and Modules

## 📌 Defining Functions with `def`

### What Are Functions?

- Functions are reusable blocks of code that perform a specific task.
- They help reduce repetition, improve readability, and make code easier to maintain.
- Example use case: Instead of writing the same logic multiple times, define it once in a function and call it whenever needed.

### How to Define a Function

- Use the `def` keyword followed by the function name and parentheses:
  ```python
  def greet(name):
      print(f"Hello, {name}!")
  ```
- Functions can accept parameters and return values using the `return` statement.

---

## 🧭 Scope and Lifetime of Variables

### Scope

- **Local Scope**:
  - Variables declared inside a function are only accessible within that function.
  - Example:
    ```python
    def example():
        x = 10  # local variable
        print(x)
    ```
- **Global Scope**:
  - Variables declared outside any function are accessible throughout the program.
  - Example:
    ```python
    x = 5  # global variable
    def show():
        print(x)
    ```

### Lifetime

- The lifetime of a variable refers to how long it exists in memory.
- Local variables only exist during the execution of the function.
- Once the function ends, the local variables are destroyed.

---

## 📦 Importing and Using Modules

### What Are Modules?

- Modules are Python files containing functions, classes, and variables that can be reused.
- They help organize code into logical components.
- Example: The built-in `math` module provides mathematical functions like `sqrt()` and `pi`.

### Ways to Import Modules

- **Import the entire module**:
  ```python
  import math
  print(math.sqrt(16))
  ```
- **Import specific functions**:
  ```python
  from math import sqrt
  print(sqrt(16))
  ```
- **Use aliases**:
  ```python
  import math as m
  print(m.pi)
  ```
- **Create custom modules**:
  - Save your functions in a `.py` file (e.g., `my_utils.py`)
  - Import it in another script:
    ```python
    import my_utils
    my_utils.my_function()
    ```

---
