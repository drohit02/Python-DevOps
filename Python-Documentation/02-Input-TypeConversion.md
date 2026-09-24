# Python User Input and Type Conversion — Complete Reference

> Accepting runtime input, understanding Python's default input type, converting values into required data types, and checking data types using `type()`.

---

## What is User Input?

Python allows a program to accept values from the user while the program is running.

The `input()` function is used to read input from the standard input, usually the terminal.

### Basic Syntax

```python
variable = input()
```

The program pauses and waits for the user to enter a value.

```text
Program starts
     |
     v
input()
     |
     v
Program waits
     |
     v
User enters value
     |
     v
Python receives value
     |
     v
Value is stored in variable
```

---

## `input()` Function

The `input()` function can display a prompt before waiting for user input.

### Syntax

```python
variable = input("Prompt message: ")
```

### Example

```python
username = input("Enter username: ")
```

Output:

```text
Enter username: rohit
```

The entered value is stored in `username`.

---

## Important: `input()` Always Returns a String

One of the most important concepts is:

> **The `input()` function always returns the entered value as a `str`.**

Even if the user enters a number, Python initially receives it as a string.

### Example

```python
port = input("Enter port: ")
```

If the user enters:

```text
8080
```

Python stores:

```text
"8080"
```

not:

```text
8080
```

Therefore:

```python
print(type(port))
```

produces:

```text
<class 'str'>
```

### Input Flow

```text
User enters:

8080
  |
  v
input()
  |
  v
"8080"
  |
  v
Stored as str
```

---

## Why Type Conversion is Required

A value received through `input()` is a string.

However, many operations require another data type.

For example, mathematical operations require numeric values.

```python
value = input("Enter a number: ")

print(value + 10)
```

This causes a type-related error because:

```text
value -> str
10    -> int
```

Python does not automatically convert the string into an integer.

The value must first be converted.

```python
value = int(input("Enter a number: "))

print(value + 10)
```

Now:

```text
input()
   |
   v
"20"       String
   |
   | int()
   v
20         Integer
   |
   v
20 + 10
```

---

## What is Type Conversion?

**Type conversion** means converting a value from one data type into another data type.

For example:

```text
String
  |
  | int()
  v
Integer
```

or:

```text
String
  |
  | float()
  v
Float
```

Python provides built-in functions for common type conversions.

| Function | Converts To |
|---|---|
| `str()` | String |
| `int()` | Integer |
| `float()` | Floating-point number |
| `bool()` | Boolean |

---

## `int()` — Convert to Integer

The `int()` function converts a compatible value into an integer.

### Syntax

```python
int(value)
```

### Example

```python
number = int("100")

print(number)
print(type(number))
```

Output:

```text
100
<class 'int'>
```

### With `input()`

Conversion can be performed immediately:

```python
number = int(input("Enter a number: "))
```

The process is:

```text
User Input
    |
    v
"100"
    |
    | int()
    v
100
    |
    v
int
```

### Common Use Cases

`int()` is commonly used when input represents:

- Counts
- Ports
- Numbers
- IDs
- Retry limits
- Instance counts
- Time values

---

## `float()` — Convert to Floating-Point Number

The `float()` function converts a compatible value into a floating-point number.

### Syntax

```python
float(value)
```

### Example

```python
temperature = float("25.5")

print(temperature)
print(type(temperature))
```

Output:

```text
25.5
<class 'float'>
```

### With `input()`

```python
threshold = float(input("Enter threshold: "))
```

If the user enters:

```text
75.5
```

Python stores:

```text
75.5
```

as:

```text
float
```

---

## `str()` — Convert to String

The `str()` function converts a value into a string.

### Syntax

```python
str(value)
```

### Example

```python
number = 100

message = str(number)

print(message)
print(type(message))
```

Output:

```text
100
<class 'str'>
```

### Why `str()` is Useful

It is useful when a non-string value needs to be combined with text.

For example:

```python
port = 8080

message = "Port: " + str(port)

print(message)
```

Without `str()`:

```python
"Port: " + port
```

causes a `TypeError` because Python cannot directly concatenate:

```text
str + int
```

---

## `bool()` — Convert to Boolean

The `bool()` function converts a value into either:

```text
True
False
```

### Syntax

```python
bool(value)
```

Examples:

```python
print(bool(1))
print(bool(0))
```

Output:

```text
True
False
```

### Important String Behavior

A non-empty string is considered `True`.

Therefore:

```python
print(bool("True"))
print(bool("False"))
```

produces:

```text
True
True
```

This is because `"False"` is still a **non-empty string**.

An empty string is considered `False`:

```python
print(bool(""))
```

Output:

```text
False
```

### Important Point

`bool()` does **not** interpret the text `"True"` or `"False"` as Boolean values.

For textual Boolean input, explicit logic is required.

---

## `type()` Function

The `type()` function is used to determine the data type of a value.

### Syntax

```python
type(value)
```

### Example

```python
value = 100

print(type(value))
```

Output:

```text
<class 'int'>
```

Another example:

```python
value = "100"

print(type(value))
```

Output:

```text
<class 'str'>
```

### Checking Input Type

```python
value = input("Enter a value: ")

print(type(value))
```

Regardless of whether the user enters:

```text
100
```

the result is:

```text
<class 'str'>
```

---

## Checking Type Before and After Conversion

`type()` is particularly useful for understanding what happens during type conversion.

```python
value = input("Enter a number: ")

print(type(value))

value = int(value)

print(type(value))
```

Conceptually:

```text
Before Conversion
-----------------
Input
  |
  v
"100"
  |
  v
str


After Conversion
----------------
"100"
  |
  | int()
  v
100
  |
  v
int
```

---

## Direct Type Conversion with `input()`

Python allows conversion to be performed directly while receiving input.

### Integer

```python
age = int(input("Enter age: "))
```

### Float

```python
price = float(input("Enter price: "))
```

### String

```python
name = str(input("Enter name: "))
```

The `str()` conversion is generally unnecessary here because `input()` already returns a string.

Therefore:

```python
name = input("Enter name: ")
```

is normally sufficient.

---

## `input()` vs Type Conversion

| Operation | Result |
|---|---|
| `input()` | Always returns `str` |
| `int(input())` | Returns `int` |
| `float(input())` | Returns `float` |
| `str(input())` | Returns `str` |
| `bool(input())` | Returns `bool`, but based on whether the string is empty |

Example:

```python
text = input("Enter value: ")
number = int(input("Enter number: "))
decimal = float(input("Enter decimal: "))
```

The resulting types are:

```text
text    -> str
number  -> int
decimal -> float
```

---

## String Concatenation and Type Conversion

String concatenation uses the `+` operator.

Two strings can be concatenated:

```python
first_name = "Rohit"
last_name = "Deshmukh"

full_name = first_name + " " + last_name

print(full_name)
```

Result:

```text
Rohit Deshmukh
```

But a string and integer cannot be directly concatenated:

```python
port = 8080

print("Port: " + port)
```

This produces a `TypeError`.

The integer can be converted to a string:

```python
print("Port: " + str(port))
```

---

## Type Conversion vs Concatenation

These are two different operations.

### Type Conversion

Changes the data type:

```python
number = int("100")
```

```text
"100"  ->  100
 str       int
```

### String Concatenation

Combines strings:

```python
message = "Value: " + "100"
```

```text
"Value: " + "100"
          |
          v
     "Value: 100"
```

If one value is an integer:

```python
message = "Value: " + str(100)
```

The integer must first be converted to a string.

---

## F-Strings with User Input

An f-string allows variables to be embedded directly inside a string.

### Syntax

```python
f"Text {variable}"
```

### Example

```python
environment = input("Enter environment: ")

print(f"Selected environment: {environment}")
```

F-strings are useful when displaying multiple values.

```python
name = input("Enter name: ")
version = input("Enter version: ")

print(f"Application: {name}, Version: {version}")
```

### F-String vs `str()` Concatenation

Without f-string:

```python
print("Port: " + str(port))
```

With f-string:

```python
print(f"Port: {port}")
```

The f-string is generally easier to read when constructing messages containing multiple variables.

---

## Type Conversion Errors

Type conversion only works when the value is compatible with the target type.

For example:

```python
number = int("100")
```

works because `"100"` represents a valid integer.

But:

```python
number = int("hello")
```

causes:

```text
ValueError
```

Similarly:

```python
value = float("abc")
```

causes a `ValueError`.

### Conversion Flow

```text
User Input
    |
    v
String
    |
    v
Conversion Function
    |
    +------ Valid ------> Converted Value
    |
    +------ Invalid ----> ValueError
```

---

## Common Type Conversion Errors

| Situation | Result |
|---|---|
| `int("100")` | Valid |
| `int("10.5")` | `ValueError` |
| `int("abc")` | `ValueError` |
| `float("10.5")` | Valid |
| `float("abc")` | `ValueError` |
| `"Port: " + 8080` | `TypeError` |
| `"Port: " + str(8080)` | Valid |

---

## Runtime Configuration Flow

User input and type conversion are useful when creating scripts that accept configuration values at runtime.

```text
             Python Script
                  |
                  v
          Ask for Input
                  |
        +---------+---------+
        |         |         |
        v         v         v
      Text      Number    Decimal
        |         |         |
        |         |         |
       str       int      float
        |         |         |
        +---------+---------+
                  |
                  v
        Application Logic
                  |
                  v
             Output
```

This pattern is commonly used in automation scripts.

---

## DevOps Relevance

User input and type conversion are useful when building scripts for:

- Deployment configuration
- Environment selection
- Port configuration
- Version selection
- Retry configuration
- Resource counts
- Threshold values
- Automation utilities
- Local testing scripts
- Operational command-line tools

A DevOps script may accept a value as text, convert it into the required type, and then use that value in automation logic.

Example flow:

```text
Operator
   |
   | enters configuration
   v
Python Script
   |
   | input()
   v
String Values
   |
   | type conversion
   v
Correct Data Types
   |
   v
Validation / Logic
   |
   v
Automation
```

---

## Important Points

- `input()` is used to accept runtime input.
- `input()` always returns a `str`.
- Numeric input must be converted before performing numeric operations.
- `int()` converts compatible values to integers.
- `float()` converts compatible values to floating-point numbers.
- `str()` converts values to strings.
- `bool()` converts values according to Python's truth-value rules.
- `bool("False")` is `True` because `"False"` is a non-empty string.
- `type()` is used to inspect the data type of a value.
- Invalid numeric conversion can raise `ValueError`.
- Concatenating a string directly with an integer causes `TypeError`.
- `str()` can be used before string concatenation.
- F-strings provide a convenient way to include variables inside strings.
- Type conversion is especially important when processing configuration values received as user input.

---

## Quick Reference

| Concept | Syntax | Purpose |
|---|---|---|
| User input | `input()` | Accept runtime input |
| Input with prompt | `input("Message")` | Display prompt and receive input |
| Integer conversion | `int(value)` | Convert to integer |
| Float conversion | `float(value)` | Convert to float |
| String conversion | `str(value)` | Convert to string |
| Boolean conversion | `bool(value)` | Convert according to truth-value rules |
| Type checking | `type(value)` | Identify data type |
| F-string | `f"{value}"` | Insert values into strings |
| String concatenation | `"A" + "B"` | Combine strings |

---

## Complete Concept Flow

```text
                 User Input
                     |
                     v
                 input()
                     |
                     v
                  str
                     |
          +----------+----------+
          |          |          |
          v          v          v
        int()     float()     bool()
          |          |          |
          v          v          v
        int        float       bool
          |          |          |
          +----------+----------+
                     |
                     v
                Program Logic
                     |
                     v
                   Output
```

---

## One-Line Summary

> `input()` receives data as a string, type conversion changes that value into the required data type, and `type()` can be used to verify the resulting type.