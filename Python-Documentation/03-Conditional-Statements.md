# Python Conditional Statements — Complete Reference

> Conditional statements allow a Python program to make decisions based on conditions. This includes `if`, `elif`, `else`, nested conditions, comparison operators, logical operators, and combining multiple conditions for DevOps automation decisions.

---

## What are Conditional Statements?

Conditional statements allow a program to execute different blocks of code depending on whether a condition is `True` or `False`.

### Basic Structure

```python
if condition:
    # code executed when condition is True
```

Example:

```python
cpu_usage = 65

if cpu_usage > 80:
    print("CPU usage is high")
```

If the condition is `False`, the code inside the `if` block is skipped.

---

## `if` Statement

The `if` statement executes a block of code only when its condition evaluates to `True`.

### Syntax

```python
if condition:
    statement
```

### Example

```python
status_code = 500

if status_code != 200:
    print("Application health check failed")
```

The condition:

```python
status_code != 200
```

evaluates to:

```text
True
```

Therefore the `print()` statement executes.

---

## `if-else` Statement

`else` provides an alternative block when the `if` condition is `False`.

### Syntax

```python
if condition:
    # True
else:
    # False
```

### Example

```python
cpu_usage = 60

if cpu_usage >= 80:
    print("High CPU utilization")
else:
    print("CPU utilization is normal")
```

### Flow

```text
             Condition
                 |
          +------+------+
          |             |
        True          False
          |             |
          v             v
        if block      else block
```

---

## `if-elif-else`

When multiple conditions need to be evaluated, Python provides `elif`.

### Syntax

```python
if condition_1:
    # block 1

elif condition_2:
    # block 2

else:
    # default block
```

Python evaluates the conditions from top to bottom.

The **first condition that evaluates to `True`** gets executed, and the remaining `elif` and `else` blocks are skipped.

### Example

```python
status = "WARNING"

if status == "FAILED":
    print("Deployment blocked")

elif status == "WARNING":
    print("Deployment requires attention")

else:
    print("Deployment allowed")
```

---

## Multiple `elif` Conditions

More than one `elif` can be used.

```python
score = 75

if score >= 90:
    print("Excellent")

elif score >= 75:
    print("Good")

elif score >= 50:
    print("Average")

else:
    print("Needs improvement")
```

### Execution Flow

```text
             score
               |
               v
        score >= 90 ?
          /       \
       True       False
        |           |
      Block       score >= 75 ?
                    /      \
                 True      False
                  |          |
                Block      score >= 50 ?
                              /      \
                           True      False
                            |          |
                          Block      else
```

---

## Comparison Operators

Conditional statements commonly use comparison operators.

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `status == 200` |
| `!=` | Not equal to | `status != 200` |
| `>` | Greater than | `errors > 10` |
| `<` | Less than | `instances < expected` |
| `>=` | Greater than or equal to | `cpu >= 85` |
| `<=` | Less than or equal to | `cpu <= 85` |

Comparison operations return a Boolean value:

```text
True
```

or:

```text
False
```

### Example

```python
cpu_usage = 90

print(cpu_usage >= 85)
```

Output:

```text
True
```

---

## `==` vs `=`

These operators have different purposes.

### Assignment — `=`

Used to assign a value to a variable.

```python
status = 200
```

### Comparison — `==`

Used to compare two values.

```python
status == 200
```

The result is:

```text
True
```

or:

```text
False
```

### Important

```python
status = 200
```

means:

> Store `200` in `status`.

```python
status == 200
```

means:

> Check whether `status` is equal to `200`.

---

## Logical Operators

Logical operators combine multiple conditions.

Python provides:

```text
and
or
not
```

---

## `and` Operator

`and` requires **all conditions** to be `True`.

### Example

```python
cpu_usage = 75
memory_usage = 70

if cpu_usage >= 70 and memory_usage >= 70:
    print("Both resources require attention")
```

Both conditions must be true.

### Truth Table

| Condition A | Condition B | `A and B` |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Concept

```text
Condition A ----+
                |
                +---- AND ----> Result
                |
Condition B ----+

Both must be True
```

---

## `or` Operator

`or` requires **at least one condition** to be `True`.

### Example

```python
cpu_usage = 90
memory_usage = 50

if cpu_usage >= 85 or memory_usage >= 85:
    print("Resource threshold exceeded")
```

The first condition is `True`, so the complete condition is `True`.

### Truth Table

| Condition A | Condition B | `A or B` |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Concept

```text
Condition A ----+
                |
                +----- OR -----> Result
                |
Condition B ----+

At least one must be True
```

---

## `not` Operator

`not` reverses a Boolean value.

```python
is_healthy = True

if not is_healthy:
    print("Application is unhealthy")
```

Truth table:

| Value | `not value` |
|---|---|
| `True` | `False` |
| `False` | `True` |

---

## Combining Comparison and Logical Operators

Real automation conditions often combine multiple comparisons.

```python
if cpu_usage >= 85 or memory_usage >= 85:
    print("Deployment blocked")
```

Here:

```text
cpu_usage >= 85
        OR
memory_usage >= 85
```

If either condition is `True`, the deployment is blocked.

---

## Parentheses in Conditions

Parentheses can be used to group conditions and make the intended logic clear.

```python
if (cpu_usage >= 70 and cpu_usage < 85) or warning_count > 20:
    print("Warning condition detected")
```

This represents:

```text
       +-----------------------------+
       | CPU >= 70 AND CPU < 85      |
       +-----------------------------+
                    |
                    OR
                    |
             warnings > 20
                    |
                    v
             Warning condition
```

Parentheses are especially useful when mixing `and` and `or`.

---

## Range Checking

A common pattern is checking whether a value falls within a range.

```python
cpu_usage >= 70 and cpu_usage < 85
```

This means:

```text
70 <= CPU usage < 85
```

### Example

```python
usage = 75

if usage >= 70 and usage < 85:
    print("Usage is in warning range")
```

The condition is `True`.

### Python Alternative

Python also supports chained comparisons:

```python
if 70 <= usage < 85:
    print("Usage is in warning range")
```

Both represent the same range.

---

## Nested `if` Statements

An `if` statement can be placed inside another `if` statement.

This is called a **nested conditional**.

### Example

```python
environment = "PRODUCTION"
status_code = 500

if environment == "PRODUCTION":

    if status_code != 200:
        print("Production deployment blocked")
```

The inner condition is evaluated only when the outer condition is `True`.

### Flow

```text
              Environment
                  |
                  v
       Is environment production?
             /          \
          True          False
           |
           v
      Status Check
           |
           v
     Is status != 200?
        /        \
     True        False
      |            |
    Block        Continue
```

---

## Why Use Nested Conditions?

Nested conditions are useful when one decision depends on another decision.

For example:

```text
Environment
     |
     +---- Production ----> Strict checks
     |
     +---- Development ---> Different checks
     |
     +---- Other ----------> Unsupported environment
```

This allows different rules to be applied for different environments.

---

## Environment-Based Conditional Logic

A common automation pattern is to apply different rules depending on the environment.

```python
environment = "PRODUCTION"

if environment.upper() == "PRODUCTION":
    print("Apply production rules")

elif environment.upper() == "DEVELOPMENT":
    print("Apply development rules")

else:
    print("Unsupported environment")
```

This creates three possible paths:

```text
                 Environment
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
     PRODUCTION   DEVELOPMENT   Other
          |           |           |
          v           v           v
     Production   Development  Unsupported
       Rules         Rules      Environment
```

---

## `upper()` for Case-Insensitive Comparison

The `upper()` string method converts a string to uppercase.

```python
environment = "production"

print(environment.upper())
```

Output:

```text
PRODUCTION
```

This makes comparisons less dependent on how the user entered the value.

```python
if environment.upper() == "PRODUCTION":
    print("Production environment")
```

The following values can therefore be normalized:

```text
production
Production
PRODUCTION
```

into:

```text
PRODUCTION
```

### Important

`upper()` does not modify the original string in place. It returns a new uppercase string.

---

## Multiple Deployment Conditions

A deployment decision may depend on several independent health checks.

For example:

```python
if (
    status_code != 200
    or cpu_usage >= 85
    or memory_usage >= 85
    or disk_usage >= 90
    or running_instances < expected_instances
    or error_count > 10
):
    print("Deployment blocked")
```

This uses `or` because **any one failed condition is sufficient to block the deployment**.

### Logic

```text
Status check -----------+
CPU check --------------+
Memory check -----------+
Disk check -------------+
Instance check ---------+---- OR ----> BLOCK
Error check ------------+
```

---

## Deployment Decision States

Conditional logic can be used to produce different decision states.

A common structure is:

```text
                Health Checks
                     |
          +----------+----------+
          |          |          |
          v          v          v
        Failed     Warning    Normal
          |          |          |
          v          v          v
       BLOCKED    WARNING     ALLOWED
```

Example:

```python
if critical_condition:
    decision = "BLOCKED"

elif warning_condition:
    decision = "WARNING"

else:
    decision = "ALLOWED"
```

---

## Why `elif` is Important for Decision States

Consider:

```python
if critical_condition:
    decision = "BLOCKED"

elif warning_condition:
    decision = "WARNING"

else:
    decision = "ALLOWED"
```

The order is important.

Python checks:

```text
1. Critical condition
       |
       | False
       v
2. Warning condition
       |
       | False
       v
3. Else
```

If the critical condition is `True`, Python does not continue to the `elif`.

Therefore, `if-elif-else` is useful when the program should select **one decision path** from multiple alternatives.

---

## Independent `if` Statements

Inside a selected decision block, multiple independent `if` statements can be used to display all failed checks.

```python
if cpu_usage >= 85:
    print("CPU threshold exceeded")

if memory_usage >= 85:
    print("Memory threshold exceeded")

if disk_usage >= 90:
    print("Disk threshold exceeded")
```

Unlike `if-elif-else`, each `if` is evaluated independently.

### Difference

```text
if
if
if
```

allows multiple blocks to execute.

Whereas:

```text
if
elif
elif
else
```

selects only the first matching branch.

---

## `if` vs `if-elif` for Multiple Checks

| Structure | Behavior |
|---|---|
| Multiple `if` | Every condition is evaluated |
| `if-elif-else` | Stops after first matching branch |
| Nested `if` | Condition evaluated inside another condition |
| `if` without `else` | No action when condition is false |
| `if-else` | Two possible paths |

### Example

```python
if cpu_usage >= 85:
    print("High CPU")

if memory_usage >= 85:
    print("High memory")
```

Both messages can appear.

But:

```python
if cpu_usage >= 85:
    print("High CPU")

elif memory_usage >= 85:
    print("High memory")
```

only the first matching branch executes.

---

## `None` as an Initial Decision Value

Python provides `None` to represent the absence of a value.

Example:

```python
decision = None
```

This can be useful when a variable will receive its actual value later.

For example:

```python
decision = None

if failed:
    decision = "BLOCKED"

elif warning:
    decision = "WARNING"

else:
    decision = "ALLOWED"
```

Before the conditional logic runs:

```text
decision -> None
```

After execution:

```text
decision -> BLOCKED
```

or:

```text
decision -> WARNING
```

or:

```text
decision -> ALLOWED
```

---

## Indentation in Conditional Statements

Python uses indentation to determine which statements belong to a conditional block.

Correct:

```python
if cpu_usage >= 85:
    print("High CPU")
```

The `print()` statement is indented.

Nested conditions require another indentation level:

```python
if environment == "PRODUCTION":

    if cpu_usage >= 85:
        print("High CPU")
```

### Structure

```text
if
|
+--- indented block
     |
     +--- nested if
          |
          +--- further indented block
```

Incorrect indentation can cause:

```text
IndentationError
```

---

## Complete Conditional Decision Flow

A typical environment-based deployment gate can follow this structure:

```text
                 User Input
                     |
                     v
              Environment Check
                     |
          +----------+----------+
          |                     |
     Production              Development
          |                     |
          v                     v
    Strict Health          Different Health
       Checks                  Checks
          |                     |
          +----------+----------+
                     |
                     v
              Critical Checks
                     |
              +------+------+
              |             |
             Yes            No
              |             |
              v             v
           BLOCKED      Warning Checks
                            |
                     +------+------+
                     |             |
                    Yes            No
                     |             |
                     v             v
                  WARNING       ALLOWED
```

---

## Generic Deployment Gate Example

```python
environment = input("Enter environment: ")
status_code = int(input("Enter status code: "))
cpu_usage = float(input("Enter CPU usage: "))
error_count = int(input("Enter error count: "))

decision = None

if environment.upper() == "PRODUCTION":

    if status_code != 200 or cpu_usage >= 85 or error_count > 10:
        decision = "BLOCKED"

    elif cpu_usage >= 70 or error_count > 5:
        decision = "WARNING"

    else:
        decision = "ALLOWED"

elif environment.upper() == "DEVELOPMENT":

    if status_code != 200 or cpu_usage >= 95 or error_count > 50:
        decision = "BLOCKED"

    elif cpu_usage >= 90 or error_count > 20:
        decision = "WARNING"

    else:
        decision = "ALLOWED"

else:
    print("Unsupported environment")
```

This example demonstrates:

- `if`
- `elif`
- `else`
- Nested `if`
- Comparison operators
- `and`
- `or`
- `upper()`
- `None`
- Multiple conditions
- Environment-specific rules
- Deployment decision logic

---

## Common Errors

### Missing Colon

Incorrect:

```python
if cpu_usage >= 85
    print("High CPU")
```

Correct:

```python
if cpu_usage >= 85:
    print("High CPU")
```

---

### Incorrect Indentation

Incorrect:

```python
if cpu_usage >= 85:
print("High CPU")
```

Correct:

```python
if cpu_usage >= 85:
    print("High CPU")
```

---

### Using `=` Instead of `==`

Incorrect:

```python
if environment = "PRODUCTION":
```

Correct:

```python
if environment == "PRODUCTION":
```

---

### Incorrect `and` / `or` Logic

Be careful when combining conditions.

```python
if cpu_usage >= 70 and cpu_usage < 85:
```

means both conditions must be true.

Whereas:

```python
if cpu_usage >= 85 or memory_usage >= 85:
```

means either condition can trigger the block.

---

### Comparing Different Data Types

If input is received using `input()`:

```python
port = input("Enter port: ")
```

then:

```python
port == 8080
```

compares:

```text
str
```

with:

```text
int
```

For numeric input, convert it:

```python
port = int(input("Enter port: "))
```

---

## Best Practices

- Use meaningful variable names for conditions.
- Keep complex conditions readable.
- Use parentheses when mixing `and` and `or`.
- Use `elif` when only one decision branch should be selected.
- Use separate `if` statements when multiple independent checks must be reported.
- Normalize user-provided text with methods such as `upper()` when appropriate.
- Convert input into the required data type before comparisons.
- Keep environment-specific rules clearly separated.
- Use `None` when a decision variable needs an initial empty state.
- Avoid unnecessarily deep nesting when the same logic can be simplified.
- Keep critical deployment checks explicit and easy to understand.

---

## Quick Reference

| Concept | Syntax | Purpose |
|---|---|---|
| `if` | `if condition:` | Execute when condition is true |
| `else` | `else:` | Execute when previous condition is false |
| `elif` | `elif condition:` | Test another condition |
| Nested `if` | `if` inside `if` | Dependent decision logic |
| Equal | `==` | Compare equality |
| Not equal | `!=` | Compare inequality |
| Greater | `>` | Greater-than comparison |
| Less | `<` | Less-than comparison |
| Greater/equal | `>=` | Threshold comparison |
| Less/equal | `<=` | Threshold comparison |
| `and` | `A and B` | Both conditions must be true |
| `or` | `A or B` | At least one condition must be true |
| `not` | `not A` | Reverse Boolean result |
| `upper()` | `value.upper()` | Convert string to uppercase |
| `None` | `variable = None` | Represent no value |

---

## Key Takeaways

```text
if
 |
 +---- True ----> Execute block
 |
 +---- False ---> Check elif
                    |
                    +---- True ----> Execute block
                    |
                    +---- False ---> else
```

The main concepts covered are:

1. `if` conditional statements
2. `if-else`
3. `if-elif-else`
4. Nested `if` statements
5. Comparison operators
6. Logical operators — `and`, `or`, `not`
7. Combining multiple conditions
8. Range checking
9. Case normalization with `upper()`
10. Independent `if` checks
11. Decision variables using `None`
12. Environment-specific conditional logic
13. Conditional deployment gates
14. Python indentation rules
15. Using conditions for DevOps automation decisions