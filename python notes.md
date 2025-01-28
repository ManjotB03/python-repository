# Python Fundamentals

## 1. Introduction to Python
Python is a popular, high-level, and general-purpose programming language known for its simplicity and readability. It is widely used for web development, data analysis, machine learning, automation, and more.

---

## 2. How to Download and Install Python

### Step 1: Download Python
1. Visit the official Python website: [https://www.python.org/](https://www.python.org/).
2. Navigate to the **Downloads** section.
3. Select the appropriate version for your operating system (e.g., Windows, macOS, Linux).
   - Recommended: Download the latest **Python 3.x** version.

### Step 2: Install Python
#### Windows:
1. Run the downloaded `.exe` file.
2. Check the box **"Add Python to PATH"** (important for running Python from the command line).
3. Click **Install Now** and follow the prompts.

#### macOS:
1. Run the downloaded `.pkg` file.
2. Follow the installation prompts.
3. Verify the installation by running `python3 --version` in Terminal.

#### Linux:
1. Open the terminal and use your package manager:
   ```bash
   sudo apt update
   sudo apt install python3


# Commenting Code in Python

## Why Comment Your Code?

Comments are essential for writing clean, understandable, and maintainable code. They help:
1. **Explain Complex Logic**: Describe non-obvious parts of the code to make them easier to understand.
2. **Improve Collaboration**: Allow team members (or your future self) to understand the purpose of the code quickly.
3. **Debugging and Testing**: Temporarily disable parts of code for debugging or testing without deleting it.
4. **Document Code**: Provide context, assumptions, or warnings directly in the codebase.

---

## How to Write Comments in Python

Python supports single-line and multi-line comments:

### 1. **Single-Line Comments**
Single-line comments start with the `#` symbol and are used to comment on one line of code.

### 2. **Multi-Line Comments**
You can use triple quotes (""" or ''') to simulate them. These are generally treated as docstrings but can also serve as comments.


# Python Data Types

Python is a dynamically typed language, which means you don’t need to declare the type of a variable. However, understanding data types is essential for writing efficient and bug-free code.

---

## 1. **Numeric Data Types**

### **a. Integer (`int`)**
- Represents whole numbers (positive or negative).
- Example:
  ```python
  x = 10
  y = -5
  ```
### **b. Float (float)**
- Represents real numbers (with decimals)
-  Example:
 ```python
  pi = 3.14
  e = -2.71
```
### **c. String (str)**
- Represents text data enclosed in single or double quotes.
- Example:
```python
name = "Manjot"
greeting = 'Hello, World!'

print(name.upper())      # Output: MANJOT
print(greeting.split())  # Output: ['Hello,', 'World!']
```

### **d. Boolean (bool)**
- Represents True or False.

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equals | `2 + 2 = 4` |
| `!=` or `<>` | Not equals | `5 != 3` |
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `3 < 7` |
| `>=` | Greater than or equal to | `8 >= 8` |
| `<=` | Less than or equal to | `2 <= 3` |

## Variables

* **Definition:** A variable is a named storage location used to hold a value (like a number, text, or a more complex data structure). 
* **Purpose:**
    * Store data for later use in calculations or operations.
    * Make code more readable and maintainable by giving meaningful names to values.
    * Allow you to easily change the value of a piece of data in multiple places within your code.

**Example (in Python):**

```python
age = 21  # Assigns the value 21 to the variable 'age'
name = "Manjot"  # Assigns the string "Alice" to the variable 'name'

print("My name is", name, "and I am", age, "years old.") 
```

## Types of string methods
| Method        | Description                                                                 | Example                                  | Output                    |
|---------------|-----------------------------------------------------------------------------|------------------------------------------|---------------------------|
| `len()`       | Returns the length (number of characters) of a string.                       | `len("Hello")`                          | `5`                       |
| `lower()`     | Converts all characters in a string to lowercase.                           | `"HELLO".lower()`                        | `hello`                   |
| `upper()`     | Converts all characters in a string to uppercase.                           | `"hello".upper()`                        | `HELLO`                   |
| `capitalize()`| Capitalizes the first letter of the string.                                 | `"hello".capitalize()`                   | `Hello`                   |
| `title()`     | Capitalizes the first letter of each word in the string.                    | `"hello world".title()`                  | `Hello World`             |
| `strip()`     | Removes leading and trailing whitespace (spaces, tabs, newlines).           | `"   hello   ".strip()`                  | `hello`                   |
| `replace()`   | Replaces all occurrences of a substring with another substring.             | `"hello".replace("e", "a")`              | `hallo`                   |
| `find()`      | Returns the index of the first occurrence of a substring.                   | `"hello".find("e")`                      | `1`                       |
| `split()`     | Splits a string into a list of substrings based on a delimiter.             | `"apple,banana,orange".split(",")`       | `['apple', 'banana', 'orange']` |
| `join()`      | Concatenates elements of a list into a single string, using the string as a delimiter. | `"-".join(["apple", "banana", "orange"])` | `apple-banana-orange`     |

## Collections in Python

In Python, **collections** refer to a set of data structures that are used to store and manage groups of data. These structures are built into the Python language and allow you to organize, manipulate, and access data in a variety of ways.

### 1. **List**

A **list** is an ordered, mutable collection of items. You can modify the elements in a list, and lists can hold elements of different data types.

#### 2. **Dictionary**

A **dictionary** (also called a dict) is a collection of key-value pairs. Each key is unique and maps to a corresponding value. 

## Loops in Python

Loops are fundamental programming structures that allow you to execute a block of code multiple times. Python provides two main types of loops: **for loops** and **while loops**. Loops help to automate repetitive tasks and make your code more efficient.

### Python Loops Summary

| Loop Type    | Description                                      | Syntax                                             | Example                                                    | Notes                                          |
|--------------|--------------------------------------------------|---------------------------------------------------|------------------------------------------------------------|------------------------------------------------|
| **`for` loop**| Used to iterate over a sequence or iterable.    | `for variable in iterable:`                       | `for i in range(5):`<br>`    print(i)`                       | Ideal for iterating over lists, ranges, or any iterable. |
| **`while` loop**| Repeats as long as a condition is true.        | `while condition:`                                | `count = 0`<br>`while count < 3:`<br>`    print(count)`       | Useful when the number of iterations is not known beforehand. |
| **`break`**   | Exits the loop prematurely.                      | `break`                                           | `for i in range(5):`<br>`    if i == 3:`<br>`        break`   | Used to stop the loop at a specific condition. |
| **`continue`**| Skips the current iteration and proceeds to the next one. | `continue`                                        | `for i in range(5):`<br>`    if i == 3:`<br>`        continue`| Skips the current iteration without exiting the loop. |
| **Nested loops**| Loops inside other loops.                      | `for variable1 in iterable1:`<br>`    for variable2 in iterable2:` | `for i in range(2):`<br>`    for j in range(3):`<br>`        print(i, j)` | Useful for working with multi-dimensional data or performing complex operations. |

## Functions in Python

A **function** in Python is a block of code that only runs when it is called. Functions allow you to organize and reuse code, making your programs more efficient and modular. You can define functions to perform specific tasks, and they can accept inputs, process them, and return outputs.

### 1. **Defining a Function**

In Python, you define a function using the `def` keyword, followed by the function name and parameters (optional).

#### Example
```python
def greet():
    print('Hello, World!')

greet()




