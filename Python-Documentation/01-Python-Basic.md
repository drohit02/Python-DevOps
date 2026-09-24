# Python Basics — Variables, Data Types and `print()` Function

> Fundamental Python concepts covered in the first Python script: variables, assignment, data types, type conversion, string concatenation, f-strings, and console output.

---

## Variables

A **variable** is a name used to store or reference a value in Python.

```python
variable_name = value
```

### Important Points

- Python does not require explicit variable declaration.
- A variable is created when a value is assigned to it.
- The `=` operator is used for assignment.
- Variable names are case-sensitive.
- Variables can be reassigned.
- Python determines the data type from the assigned value.
- A variable can contain different types of values during program execution.

---

## Variable Naming Rules

Python variable names must follow specific rules.

| Rule | Example |
|---|---|
| Can contain letters | `name` |
| Can contain numbers | `name1` |
| Can contain underscores | `user_name` |
| Cannot start with a number | `1name` ❌ |
| Cannot contain spaces | `user name` ❌ |
| Case-sensitive | `name` ≠ `Name` |
| Cannot use Python keywords | `class` ❌ |

### Naming Convention

Python commonly follows the **snake_case** naming convention.

```python
application_name
server_port
environment_name
user_status
```

Using meaningful variable names improves readability and makes automation scripts easier to maintain.

---

## Variable Assignment

Assignment means storing a value in a variable.

```python
name = "Python"
count = 10
enabled = True
```

The value on the right side of `=` is assigned to the variable on the left side.

```text
variable = value
   ↑        ↑
 name     data
```

### Reassignment

A variable can be assigned a new value.

```python
value = 100
value = 200
```

After the second assignment, `value` contains `200`.

---

## Dynamic Typing

Python is a **dynamically typed language**.

The data type is determined at runtime based on the value assigned to a variable.

```python
value = 100
value = "Python"
```

The same variable can therefore refer to values of different data types at different points during execution.

### Important Point

Python does not require the programmer to specify the variable type during assignment.

---

## Data Types

A **data type** defines the kind of value stored in a variable.

### Common Python Data Types

| Data Type | Python Type | Example | Purpose |
|---|---|---|---|
| String | `str` | `"Python"` | Text |
| Integer | `int` | `100` | Whole numbers |
| Float | `float` | `10.5` | Decimal numbers |
| Boolean | `bool` | `True` | Logical state |
| List | `list` | `[1, 2, 3]` | Ordered collection |
| Tuple | `tuple` | `(1, 2, 3)` | Immutable collection |
| Set | `set` | `{1, 2, 3}` | Unique values |
| Dictionary | `dict` | `{"key": "value"}` | Key-value data |
| None | `NoneType` | `None` | Represents no value |

The fundamental data types introduced here are:

- `str`
- `int`
- `float`
- `bool`

---

## String — `str`

A **String** represents textual data.

```python
"Hello"
'Python'
```

Strings are normally enclosed in single or double quotes.

### Important Points

- Strings represent text.
- Strings can contain letters, numbers, spaces, and special characters.
- A value enclosed in quotes is treated as a string.
- A numeric-looking value can still be a string if it is enclosed in quotes.

### String vs Number

| Value | Data Type |
|---|---|
| `100` | `int` |
| `"100"` | `str` |
| `10.5` | `float` |
| `"10.5"` | `str` |

Therefore, quotes affect the data type.

---

## Integer — `int`

An **Integer** represents a whole number without a decimal portion.

```python
10
100
8080
-50
0
```

Integers are commonly used for:

- Counts
- Port numbers
- IDs
- Numeric configuration values
- Mathematical operations

---

## Float — `float`

A **Float** represents a number containing a decimal portion.

```python
3.14
10.5
99.99
```

### Float vs String

```python
3.12
```

is a `float`.

```python
"3.12"
```

is a `str`.

This distinction is important when working with software versions and configuration values.

A software version is commonly represented as a string because it is an identifier rather than a number intended for mathematical calculations.

---

## Boolean — `bool`

A **Boolean** represents a logical state.

Python has two Boolean values:

```python
True
False
```

### Common Use Cases

| State | Boolean Value |
|---|---|
| Service running | `True` |
| Service stopped | `False` |
| Feature enabled | `True` |
| Feature disabled | `False` |
| Deployment successful | `True` |
| Deployment unsuccessful | `False` |

### Boolean vs String

| Value | Data Type |
|---|---|
| `True` | `bool` |
| `False` | `bool` |
| `"True"` | `str` |
| `"False"` | `str` |

Quotes convert the value into a String representation.

---

## Checking Data Types — `type()`

Python provides the built-in `type()` function to determine the data type of a value.

```python
type(value)
```

Examples:

```python
type("Python")    # str
type(100)         # int
type(10.5)        # float
type(True)        # bool
```

### Why `type()` is Useful

- Verify the data type of a variable.
- Debug unexpected values.
- Understand how Python interpreted a value.
- Identify type-related problems.

---

## `print()` Function

The `print()` function is used to display information on the standard output.

```python
print(value)
```

It is commonly used for:

- Displaying messages.
- Displaying variable values.
- Debugging.
- Showing application information.
- Displaying script execution results.

---

## Printing Multiple Values

The `print()` function can accept multiple values.

```python
print(value1, value2, value3)
```

By default, Python separates the values with a space.

```text
value1 value2 value3
```

The separator can be customized using `sep`.

```python
print(value1, value2, sep=" | ")
```

Output:

```text
value1 | value2
```

---

## New Line — `\n`

`\n` represents a **newline character** inside a string.

```python
"First Line\nSecond Line"
```

Output:

```text
First Line
Second Line
```

### Common Escape Characters

| Escape Sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote |
| `\'` | Single quote |

Escape sequences are useful when formatting console output.

---

## String Concatenation

**Concatenation** means joining strings together.

Python uses the `+` operator to concatenate strings.

```python
"Hello " + "Python"
```

Result:

```text
Hello Python
```

### Concatenating Variables

String variables can also be combined.

```python
"Name: " + name
```

The values being joined using `+` must be compatible with string concatenation.

---

## String + Integer

Python does not automatically concatenate a String and an Integer using `+`.

```python
"Port: " + 8080
```

This results in a `TypeError`.

### Using `str()`

The `str()` function converts a value into a String.

```python
"Port: " + str(8080)
```

The conversion flow is:

```text
Integer
   │
   ▼
 str()
   │
   ▼
String
```

Now both values are strings and can be concatenated.

---

## Type Conversion

**Type conversion** means converting a value from one data type to another.

Common conversion functions include:

| Function | Converts To |
|---|---|
| `str()` | String |
| `int()` | Integer |
| `float()` | Float |
| `bool()` | Boolean |

### Examples

```python
str(100)
int("100")
float("10.5")
bool(1)
```

Type conversion is especially important when working with:

- User input
- Environment variables
- Configuration files
- Command-line arguments
- API responses
- Automation scripts

---

## `str()` vs `f-string`

Both can be used to include variable values in text, but they work differently.

### `str()`

`str()` explicitly converts a value into a string.

```python
str(value)
```

It is useful when a value needs to be converted before performing string operations such as concatenation.

### F-String

An **f-string** allows variables and expressions to be inserted directly inside a string.

```python
f"Value: {value}"
```

The `f` before the opening quote tells Python that expressions inside `{}` should be evaluated.

---

## F-Strings

F-strings provide a clean way to create formatted strings.

```python
f"Hello {name}"
```

The expression inside `{}` is evaluated and its result is inserted into the string.

### Multiple Variables

```python
f"{name} is running on port {port}"
```

Multiple variables can be included in the same f-string.

### Expressions

F-strings can also evaluate expressions.

```python
f"Total: {price * quantity}"
```

### Important Points

- Prefix the string with `f`.
- Variables or expressions are placed inside `{}`.
- Python automatically converts the inserted value into its string representation.
- F-strings are generally easier to read than long concatenation expressions.
- F-strings are especially useful for logging and status messages in automation scripts.

---

## String Concatenation vs F-String

| Feature | Concatenation | F-String |
|---|---|---|
| Operator | `+` | `f"..."` |
| Explicit conversion often needed | Yes | Usually no |
| Readability | Can become difficult with many values | Generally easier |
| Variables | Added using `+` | Placed inside `{}` |
| Expressions | Less convenient | Supported directly |
| Useful for formatted output | Yes | Yes |

### Example Comparison

Concatenation:

```python
"User: " + name + ", Age: " + str(age)
```

F-string:

```python
f"User: {name}, Age: {age}"
```

For output containing multiple variables, f-strings are generally cleaner and easier to maintain.

---

## `str()` vs F-String — When to Use

| Situation | Recommended |
|---|---|
| Need to convert a value into a String | `str()` |
| Need to concatenate a non-string value | `str()` |
| Need formatted output with variables | F-string |
| Need multiple variables in one message | F-string |
| Need expressions inside output | F-string |

The two concepts are related but serve different purposes:

```text
str()
  ↓
Type Conversion

f"..."
  ↓
String Formatting
```

---

## `print()` and Formatted Output

`print()` and f-strings are often used together.

```text
f-string → creates formatted text
     ↓
print() → displays the text
```

This makes it easy to create readable console messages containing dynamic values.

---

## `print()` Return Value

The `print()` function displays data but does not return the displayed value for normal program use.

Its return value is:

```python
None
```

This is different from the text that appears on the console.

---

## Practical DevOps Relevance

These basic Python concepts are frequently used in DevOps automation.

| Python Concept | DevOps Usage |
|---|---|
| Variables | Store configuration and runtime values |
| Strings | Handle service names, paths, environments and commands |
| Integers | Handle ports, counts and numeric configuration |
| Booleans | Represent enabled/disabled or success/failure states |
| Type conversion | Convert environment variables and command-line input |
| `print()` | Display execution information and debugging output |
| Concatenation | Build simple messages and strings |
| F-strings | Create readable logs and dynamic messages |
| `type()` | Debug unexpected configuration values |

---

## Key Takeaways

```text
Variable
   │
   ├── stores/references a value
   │
   ▼
Data Type
   │
   ├── str
   ├── int
   ├── float
   └── bool
   │
   ▼
Type Conversion
   │
   └── str(), int(), float(), bool()
   │
   ▼
String Formatting
   │
   ├── Concatenation (+)
   └── F-string
   │
   ▼
print()
   │
   └── displays the final output
```

### Quick Reference

| Concept | Key Point |
|---|---|
| Variable | Stores or references a value |
| Assignment | Uses `=` |
| Dynamic Typing | Type is determined at runtime |
| `str` | Text |
| `int` | Whole number |
| `float` | Decimal number |
| `bool` | `True` or `False` |
| `type()` | Checks the data type |
| `str()` | Converts a value to String |
| Concatenation | Joins strings using `+` |
| `\n` | Creates a new line |
| F-string | Formats strings using `{}` |
| `print()` | Displays output |