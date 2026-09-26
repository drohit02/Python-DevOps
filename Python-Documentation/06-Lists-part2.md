# Python Tutorial - 1
## Question 6 - Lists: `len()`, Conditional List Processing and Counters

> This note focuses only on the new or important List concepts introduced in this script. Basic List creation, indexing, `append()`, iteration, searching, and `break` are covered in the previous List notes.

---

## 1. `len()` with a List

`len()` returns the number of elements currently present in a list.

```python
services = ["api", "web", "worker"]

print(len(services))
```

Output:

```text
3
```

### Remember

```text
len(list) = Number of elements
```

It does **not** return the last index.

For:

```python
services = ["api", "web", "worker"]
```

```text
Number of elements = 3
Last index         = 2
```

---

## 2. `len()` Changes as the List Changes

A list can grow during program execution.

```python
services = []

print(len(services))
```

Output:

```text
0
```

After adding items:

```python
services.append("api")
services.append("web")
```

Now:

```python
len(services)
```

returns:

```text
2
```

### Important Concept

`len()` does not permanently store the list size.

It calculates the current number of elements.

```text
List changes
     │
     ▼
len(list)
     │
     ▼
Current number of elements
```

---

# 3. `len()` vs Counter

There are two different concepts.

### List Length

```python
len(services)
```

Answers:

> How many elements are currently stored in the list?

### Counter

```python
ready_services += 1
```

Answers:

> How many items satisfied this particular condition?

Example:

```text
All Services List
        │
        ├── Ready
        ├── Failed
        └── Ready
```

Therefore:

```text
len(services)       → Total services
ready_services      → Ready services
failed_services     → Failed services
```

These values may be different.

---

# 4. Multiple Lists for Different Purposes

A program can maintain multiple lists.

For example:

```python
all_services = []

failed_services = []
```

The first list stores all valid services.

The second list stores only services that failed validation.

Conceptually:

```text
                 All Services
                      │
             ┌────────┴────────┐
             │                 │
          Ready             Failed
             │                 │
             │                 ▼
             │          failed_services
             │
             ▼
        ready count
```

A list can therefore represent a collection while a separate counter can represent a numeric summary.

---

# 5. Conditional `append()`

A list does not have to receive every value.

An item can be added only when a condition is satisfied.

```python
if service_name:
    services.append(service_name)
```

Conceptually:

```text
Input
  │
  ▼
Valid?
 /   \
No    Yes
│      │
│      ▼
│    append()
│      │
└──────┘
```

This is useful when building a list containing only valid data.

---

# 6. Truthiness of Strings

Python allows a string to be directly used in a condition.

```python
if service_name:
    ...
```

An empty string:

```python
""
```

is considered **False**.

A non-empty string is considered **True**.

```python
if "api":
    print("True")
```

The condition is true because the string contains characters.

But:

```python
if "":
    print("True")
```

does not execute because the string is empty.

### Remember

```text
""       → False
"api"    → True
"hello"  → True
```

---

# 7. Empty List Truthiness

Lists also have Boolean truthiness.

An empty list:

```python
services = []
```

is considered:

```text
False
```

A non-empty list:

```python
services = ["api"]
```

is considered:

```text
True
```

Therefore:

```python
if services:
    print("List contains services")
```

is a valid way to check whether a list contains at least one element.

---

# 8. `None` vs Empty List

These are different concepts.

```python
service_name = None
```

means:

> No value has been assigned.

Whereas:

```python
services = []
```

means:

> A list exists, but currently contains zero elements.

Conceptually:

```text
None
 │
 └── No value

[]
 │
 └── List exists but contains no elements
```

Do not confuse:

```python
None
```

with:

```python
[]
```

---

# 9. Initializing a List Before a Loop

If a list needs to collect values during a loop, create it before the loop.

```python
services = []

for item in source:
    services.append(item)
```

Why?

Because the list must already exist when `append()` is executed.

Typical pattern:

```text
Create List
     │
     ▼
Start Loop
     │
     ▼
Receive Item
     │
     ▼
Validate Item
     │
     ▼
append()
     │
     ▼
Next Item
```

---

# 10. Conditional Classification

A common automation pattern is to classify each item.

For example:

```text
Service
   │
   ▼
Validation
   │
   ├── Passed → Ready
   │
   └── Failed → Failed
```

The program can then maintain:

```python
ready_count = 0
failed_count = 0
failed_services = []
```

This gives three different types of information:

```text
ready_count
    → Number

failed_count
    → Number

failed_services
    → Collection of names
```

---

# 11. Counter Pattern

A counter normally starts from zero.

```python
ready_count = 0
```

When an item satisfies the condition:

```python
ready_count += 1
```

Equivalent to:

```python
ready_count = ready_count + 1
```

### Pattern

```text
Start
  │
  ▼
count = 0
  │
  ▼
Process item
  │
  ├── Condition True  → count += 1
  │
  └── Condition False → no increment
  │
  ▼
Next item
```

---

# 12. Counter vs List

A counter and a list solve different problems.

### Counter

```python
failed_count = 0
```

Stores:

```text
Number
```

### List

```python
failed_services = []
```

Stores:

```text
Actual values
```

For example:

```text
failed_count = 2

failed_services = [
    "payment",
    "notification"
]
```

The counter tells you **how many**.

The list tells you **which ones**.

---

# 13. `len()` Can Also Count a Subset

If a list contains only failed services:

```python
failed_services = [
    "payment",
    "notification"
]
```

then:

```python
len(failed_services)
```

returns:

```text
2
```

Therefore, sometimes a separate counter is not necessary.

For example:

```python
failed_services.append(service_name)
```

and later:

```python
print(len(failed_services))
```

can provide the failed count.

### Important

Use a separate counter when the count represents logic that is different from simply counting list elements.

---

# 14. `len()` as a Validation Check

A list can be checked using its length.

```python
if len(services) == 0:
    print("No services available")
```

Or more simply:

```python
if not services:
    print("No services available")
```

Both express the idea that the list is empty.

---

# 15. `len()` with `range()`

A very common pattern is:

```python
for index in range(len(services)):
    print(services[index])
```

If:

```python
len(services) == 4
```

then:

```python
range(len(services))
```

becomes:

```python
range(4)
```

which generates:

```text
0
1
2
3
```

These are the valid indexes.

---

# 16. `len()` Is Dynamic

Suppose:

```python
services = ["api", "web"]
```

Then:

```python
len(services)
```

is:

```text
2
```

After:

```python
services.append("worker")
```

the same expression:

```python
len(services)
```

now returns:

```text
3
```

Therefore:

> `len()` always reflects the current size of the collection.

---

# 17. Important List Rules to Remember

### Rule 1 — Index starts from zero

```text
First item  → 0
Second item → 1
Third item  → 2
```

---

### Rule 2 — `len()` counts elements

```python
len(services)
```

returns:

```text
Number of elements
```

not the last index.

---

### Rule 3 — Last index

```python
len(services) - 1
```

is the last valid index for a non-empty list.

---

### Rule 4 — Empty list

```python
[]
```

has:

```text
len([]) == 0
```

---

### Rule 5 — `append()` adds one item

```python
services.append(value)
```

---

### Rule 6 — `append()` returns `None`

Do not write:

```python
services = services.append(value)
```

Use:

```python
services.append(value)
```

---

### Rule 7 — Lists are mutable

```python
services[0] = "new-value"
```

can change an existing element.

---

### Rule 8 — Lists preserve order

Items remain in insertion order.

---

### Rule 9 — Lists allow duplicates

```python
["api", "api", "web"]
```

is valid.

---

### Rule 10 — List can grow dynamically

```python
services = []

services.append("api")
services.append("web")
```

No fixed size is required.

---

# 18. Most Important List Methods

| Operation | Syntax | Meaning |
|---|---|---|
| Create | `[]` | Empty list |
| Create | `list()` | Empty list |
| Add | `append(value)` | Add at end |
| Count | `len(list)` | Number of elements |
| Access | `list[index]` | Get element |
| Modify | `list[index] = value` | Change element |
| Search | `value in list` | Membership |
| Remove value | `remove(value)` | Remove matching value |
| Remove index | `pop(index)` | Remove by index |
| Delete | `del list[index]` | Delete element |
| Iterate | `for item in list` | Process elements |
| Index + value | `enumerate(list)` | Get both |

---

# 19. List + Loop + Condition

One of the most important Python patterns for DevOps scripting is:

```python
items = []

for item in source:

    if condition:
        items.append(item)
```

This means:

```text
Source
  │
  ▼
Loop through items
  │
  ▼
Check condition
  │
  ├── False → Ignore
  │
  └── True → Add to list
```

This pattern is the foundation for filtering data.

---

# 20. List + Counter + Condition

Another important pattern:

```python
ready_count = 0
failed_count = 0

for item in items:

    if condition:
        ready_count += 1
    else:
        failed_count += 1
```

This produces summary information.

```text
                 Items
                   │
                   ▼
               Condition
                /      \
               /        \
            True        False
             │            │
             ▼            ▼
        ready_count   failed_count
          += 1          += 1
```

---

# 21. List + Failed Items + Count

A useful validation pattern is:

```python
failed_items = []

for item in items:

    if condition_failed:
        failed_items.append(item)
```

Then:

```python
failed_count = len(failed_items)
```

This provides both:

```text
Failed Count
     +
Failed Item Names
```

Example:

```text
Failed Count:
3

Failed Items:
[
    "service-a",
    "service-c",
    "service-f"
]
```

---

# 22. Important Difference: `len()` vs `range()`

Do not confuse these:

```python
len(services)
```

and:

```python
range(len(services))
```

### `len()`

Produces a number:

```text
3
```

### `range()`

Produces an iterable sequence:

```text
0, 1, 2
```

Example:

```python
services = ["api", "web", "worker"]

print(len(services))
```

Output:

```text
3
```

But:

```python
for index in range(len(services)):
    print(index)
```

Output:

```text
0
1
2
```

---

# 23. One Important Production Pattern

When you only need the number of items:

```python
len(services)
```

When you need to process each value:

```python
for service in services:
```

When you need index + value:

```python
for index, service in enumerate(services):
```

When you need to check whether an item exists:

```python
if service in services:
```

Remember this decision:

```text
Need count?
   → len()

Need values?
   → for item in list

Need index + value?
   → enumerate()

Need existence?
   → in
```

---

# 24. DevOps Relevance

Lists are frequently used to maintain collections of:

```text
ECS Services
Kubernetes Pods
Docker Containers
EC2 Instances
AWS Resources
Deployment Targets
Application Names
Log Files
Environment Names
Repository Names
Failed Services
Healthy Services
```

A typical automation script can therefore follow:

```text
Collect Data
     │
     ▼
Store in List
     │
     ▼
Validate
     │
     ▼
Classify
   /     \
Ready   Failed
  │        │
  │        ▼
  │   Failed List
  │
  ▼
Ready Count

        +
        
Failed Count
```

---

# 25. Quick Revision

```text
LIST
 │
 ├── Ordered
 ├── Mutable
 ├── Allows duplicates
 ├── Zero-based index
 │
 ├── append()
 │      └── Adds item
 │
 ├── len()
 │      └── Number of items
 │
 ├── list[index]
 │      └── Access item
 │
 ├── in
 │      └── Check existence
 │
 ├── for
 │      └── Process items
 │
 └── enumerate()
        └── Index + value
```

### Most Important Things to Remember

```text
1. List index starts from 0.

2. len(list) gives the number of elements.

3. Last index = len(list) - 1.

4. append() modifies the list.

5. append() returns None.

6. [] means an empty list.

7. None means no value; [] means an empty list.

8. Lists are mutable.

9. Lists preserve insertion order.

10. Lists allow duplicate values.

11. A list can grow dynamically.

12. Use `for item in list` when index is not required.

13. Use `enumerate()` when index and value are both required.

14. Use `in` for a simple membership check.

15. Use `len()` when you need the current number of elements.

16. A counter stores a number; a list stores actual items.

17. A list can be used to store only items that pass a condition.

18. `if list:` means the list is not empty.

19. `if not list:` means the list is empty.

20. `len()` always reflects the list's current size.