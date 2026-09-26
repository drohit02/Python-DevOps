# Python Tutorial - 1
## Question 5 - Lists and List Processing

> Python Lists are ordered, mutable collections used to store multiple values in a single variable. Lists are commonly used in DevOps scripting to maintain inventories, process service names, collect configuration values, search for resources, and perform repeated operations on a group of items.

---

## 1. What is a List?

A **List** is a collection that can store multiple values in a single variable.

```python
services = ["api", "web", "worker"]
```

A list:

- Maintains insertion order
- Allows duplicate values
- Allows different data types
- Can be modified after creation
- Uses indexing
- Supports iteration
- Supports searching and filtering

### Basic Structure

```text
List
 │
 ├── Item 1
 ├── Item 2
 ├── Item 3
 └── Item 4
```

Example:

```python
services = ["api", "web", "worker", "database"]
```

---

# 2. Creating an Empty List

An empty list contains no elements.

```python
services = []
```

The `list()` constructor can also be used:

```python
services = list()
```

Both create an empty list.

```python
services = []

print(services)
```

Output:

```text
[]
```

### Why Create an Empty List?

An empty list is commonly used when values will be collected later.

```python
services = []

services.append("api")
services.append("web")
services.append("worker")
```

The list now contains:

```text
["api", "web", "worker"]
```

This is a common pattern in automation scripts.

---

# 3. Adding Items to a List

The `append()` method adds one item to the end of a list.

```python
services = []

services.append("api")
services.append("web")
services.append("worker")
```

Result:

```text
["api", "web", "worker"]
```

### Important

`append()` modifies the existing list.

Do **not** assign the result of `append()` back to the list.

Correct:

```python
services.append("api")
```

Incorrect:

```python
services = services.append("api")
```

Why?

Because `append()` returns `None`.

```python
services = []

result = services.append("api")

print(services)
print(result)
```

Output:

```text
["api"]
None
```

Therefore:

```python
services = services.append("api")
```

would make `services` become:

```text
None
```

---

# 4. List Indexing

Every element in a list has an index.

Python uses **zero-based indexing**.

```python
services = ["api", "web", "worker"]
```

The structure is:

```text
Value       api       web       worker
Index        0         1          2
             │         │          │
             └─────────┴──────────┘
                  List
```

Accessing an item:

```python
print(services[0])
```

Output:

```text
api
```

```python
print(services[1])
```

Output:

```text
web
```

```python
print(services[2])
```

Output:

```text
worker
```

---

# 5. Index vs Location

An important distinction:

### Index

The actual position number used internally by Python.

```text
0
1
2
```

### Human-readable Location

You may choose to display the position starting from `1`.

```text
1st
2nd
3rd
```

For example:

```text
List:

Index       Value
  0         api
  1         web
  2         worker
```

Human-readable locations:

```text
Location 1 → api
Location 2 → web
Location 3 → worker
```

Python's index is still:

```text
0, 1, 2
```

The location displayed to a user does not change the actual list index.

---

# 6. Accessing List Elements

A list element can be accessed using:

```python
list_name[index]
```

Example:

```python
services = ["api", "web", "worker"]

service = services[1]

print(service)
```

Output:

```text
web
```

The expression:

```python
services[1]
```

means:

> Get the element stored at index `1`.

---

# 7. Negative Indexing

Python also supports negative indexes.

```python
services = ["api", "web", "worker"]
```

The index structure becomes:

```text
Positive Index:    0        1         2
                   │        │         │
                   api      web       worker
                   │        │         │
Negative Index:   -3       -2        -1
```

Therefore:

```python
services[-1]
```

returns:

```text
worker
```

And:

```python
services[-2]
```

returns:

```text
web
```

Negative indexing is useful when accessing elements from the end of a list.

---

# 8. Finding the Number of Elements

The `len()` function returns the number of elements in a list.

```python
services = ["api", "web", "worker"]

print(len(services))
```

Output:

```text
3
```

### Important

`len()` returns the **number of elements**, not the last index.

For:

```python
services = ["api", "web", "worker"]
```

there are:

```text
3 elements
```

but the last index is:

```text
2
```

Because indexing starts from `0`.

```text
Number of elements = 3
Last index         = 2
```

---

# 9. `len()` and Indexing

This is an important relationship:

```python
services = ["api", "web", "worker"]
```

```text
len(services) = 3

Valid indexes:

0
1
2
```

Therefore, when accessing indexes using a loop:

```python
for index in range(0, len(services)):
    print(services[index])
```

The generated indexes are:

```text
0
1
2
```

---

# 10. Using `range()` with a List

`range()` can be used to generate indexes.

```python
services = ["api", "web", "worker"]

for index in range(0, len(services)):
    print(services[index])
```

Execution:

```text
range(0, 3)

0
1
2
```

Then:

```text
services[0]
services[1]
services[2]
```

The loop therefore accesses every list element.

---

# 11. Direct List Iteration

Python does not always require indexes to process a list.

You can directly iterate over the values.

```python
services = ["api", "web", "worker"]

for service in services:
    print(service)
```

Output:

```text
api
web
worker
```

This is generally simpler when the index is not required.

---

# 12. Index-Based Iteration vs Direct Iteration

### Index-Based Iteration

```python
for index in range(len(services)):
    print(services[index])
```

Use this when you need the index.

```text
Index + Value
```

### Direct Iteration

```python
for service in services:
    print(service)
```

Use this when you only need the value.

```text
Value
```

### Conceptual Difference

```text
Index-Based:

index
  │
  ▼
services[index]
  │
  ▼
value


Direct:

service
  │
  ▼
value
```

---

# 13. Reading Multiple Values from User Input

Lists are commonly used to collect multiple values from users.

General pattern:

```python
items = []

count = int(input("Enter number of items: "))

for number in range(1, count + 1):
    item = input(f"Enter item {number}: ")
    items.append(item)
```

If the user enters:

```text
3
api
web
worker
```

the resulting list becomes:

```python
["api", "web", "worker"]
```

This pattern is useful for dynamically building collections.

---

# 14. Dynamic List Creation

A list does not need to have a fixed size.

For example:

```python
services = []
```

Initially:

```text
[]
```

After one item:

```text
["api"]
```

After two items:

```text
["api", "web"]
```

After three items:

```text
["api", "web", "worker"]
```

Python lists can grow dynamically.

---

# 15. Searching for an Item in a List

Python provides the `in` operator for checking whether an item exists.

```python
services = ["api", "web", "worker"]

if "web" in services:
    print("Service found")
```

Output:

```text
Service found
```

If the item does not exist:

```python
if "database" in services:
    print("Service found")
```

The condition evaluates to:

```text
False
```

---

# 16. Using `in` for Membership Checking

The `in` operator performs a membership test.

```python
item in collection
```

It produces a Boolean result:

```text
True
```

or:

```text
False
```

Example:

```python
services = ["api", "web", "worker"]

print("api" in services)
```

Output:

```text
True
```

```python
print("database" in services)
```

Output:

```text
False
```

---

# 17. Case Sensitivity During Searching

String comparison is case-sensitive.

```python
services = ["API", "Web", "Worker"]

print("api" in services)
```

Output:

```text
False
```

Even though:

```text
API
```

and:

```text
api
```

represent the same letters, Python treats them as different strings.

---

# 18. Case-Insensitive Comparison

The `lower()` method can normalize strings before comparison.

```python
service_name = "API"

if service_name.lower() == "api":
    print("Service found")
```

Both values become lowercase:

```text
api
```

Another option is:

```python
service_name.upper()
```

Example:

```python
if service_name.upper() == "API":
    print("Service found")
```

### Concept

```text
User Input
    │
    ▼
Normalize Case
    │
    ▼
Compare Values
    │
    ▼
True / False
```

---

# 19. Manual Search Using a Loop

Instead of using `in`, a list can be searched manually.

```python
services = ["api", "web", "worker"]

search_name = "web"

for index in range(len(services)):

    if services[index] == search_name:
        print("Service found")
        break
```

The loop checks:

```text
services[0] == search_name
services[1] == search_name
services[2] == search_name
```

Once a match is found, `break` terminates the loop.

---

# 20. Using a Boolean Flag During Search

A Boolean variable can store whether a search was successful.

```python
services = ["api", "web", "worker"]

found = False

for service in services:

    if service == "web":
        found = True
        break

if found:
    print("Service found")
else:
    print("Service not found")
```

Initial state:

```text
found = False
```

After finding the item:

```text
found = True
```

The Boolean variable represents the final search state.

---

# 21. Why Initialize a Boolean Variable?

Before the search begins, the result is unknown.

Therefore, a Boolean flag can be initialized with:

```python
found = False
```

Then the search can update it:

```python
if service == search_name:
    found = True
```

Conceptually:

```text
Search Starts
     │
     ▼
found = False
     │
     ▼
Check each item
     │
     ├── Match → found = True
     │
     └── No Match → continue
     │
     ▼
Check final result
```

---

# 22. `break` in a Search Loop

`break` immediately terminates the current loop.

```python
for service in services:

    if service == search_name:
        found = True
        break
```

Once the condition becomes true:

```text
Match Found
     │
     ▼
found = True
     │
     ▼
break
     │
     ▼
Loop Terminates
```

There is no reason to continue searching if only the existence of the item is required.

---

# 23. Finding the Index of an Item

If the index is required, the loop can retain the current index.

```python
services = ["api", "web", "worker"]

search_name = "web"

for index in range(len(services)):

    if services[index] == search_name:
        print(f"Found at index {index}")
        break
```

Output:

```text
Found at index 1
```

Remember:

```text
Human Position = Index + 1
```

Therefore:

```python
print(index + 1)
```

would display:

```text
2
```

---

# 24. Index vs Human Position

For this list:

```python
services = ["api", "web", "worker"]
```

| Python Index | Human Position | Value |
|---:|---:|---|
| 0 | 1 | api |
| 1 | 2 | web |
| 2 | 3 | worker |

Python internally uses:

```text
0, 1, 2
```

A user-facing message may use:

```text
1, 2, 3
```

The two concepts should not be confused.

---

# 25. Modifying List Elements

Lists are **mutable**.

This means their elements can be changed after the list is created.

```python
services = ["api", "web", "worker"]

services[1] = "frontend"
```

The list becomes:

```text
["api", "frontend", "worker"]
```

The list itself remains the same object, but one element has been changed.

---

# 26. Removing List Elements

Python provides multiple methods for removing elements.

### `remove()`

Removes the first matching value.

```python
services = ["api", "web", "worker"]

services.remove("web")
```

Result:

```text
["api", "worker"]
```

### `pop()`

Removes an item using its index.

```python
services.pop(1)
```

### `del`

Can delete an element using its index.

```python
del services[1]
```

---

# 27. `append()` vs `remove()` vs `pop()`

| Operation | Purpose |
|---|---|
| `append()` | Add item at the end |
| `remove()` | Remove matching value |
| `pop()` | Remove item using index |
| `del` | Delete item or range |

Example:

```python
services.append("cache")
services.remove("web")
services.pop(0)
```

---

# 28. List Ordering

Lists preserve the order in which items are inserted.

```python
services = []

services.append("api")
services.append("web")
services.append("worker")
```

The order remains:

```text
api
web
worker
```

Python does not automatically rearrange the list.

---

# 29. Duplicate Values

Lists allow duplicate values.

```python
services = ["api", "web", "api"]
```

The list contains:

```text
Index 0 → api
Index 1 → web
Index 2 → api
```

Therefore, the same value can appear multiple times.

---

# 30. Searching When Duplicate Values Exist

Suppose:

```python
services = ["api", "web", "api"]
```

A search for:

```text
api
```

can have multiple matches.

If using:

```python
break
```

the loop stops at the first match.

```text
api → first match → break
```

Therefore:

> `break` is appropriate when only the first matching item is required.

If all matching items are required, the loop should continue.

---

# 31. Counting Matching Items

A counter can be used to count matching values.

```python
services = ["api", "web", "api", "worker"]

count = 0

for service in services:

    if service == "api":
        count += 1

print(count)
```

Output:

```text
2
```

This is a common pattern in automation scripts.

---

# 32. Counter Pattern

A counter usually starts at zero.

```python
count = 0
```

When the required condition is satisfied:

```python
count += 1
```

Conceptually:

```text
Start
  │
  ▼
count = 0
  │
  ▼
Process item
  │
  ├── Match → count + 1
  │
  └── No Match → continue
  │
  ▼
Next item
  │
  ▼
Final count
```

---

# 33. List Processing Pattern

A very common Python automation pattern is:

```text
Create Collection
      │
      ▼
Collect Data
      │
      ▼
Store in List
      │
      ▼
Process List
      │
      ├── Display
      ├── Search
      ├── Filter
      ├── Count
      └── Modify
```

This pattern is highly useful in DevOps scripting.

---

# 34. Lists and DevOps Service Inventory

Lists are useful for representing collections such as:

```text
Application Services
EC2 Instances
ECS Services
Docker Images
Kubernetes Pods
Namespaces
AWS Regions
S3 Objects
File Names
Deployment Targets
```

Example:

```python
services = [
    "frontend",
    "backend",
    "payment",
    "notification"
]
```

The list can then be processed using loops.

---

# 35. Processing a Service Inventory

A typical automation flow may look like:

```text
User Input
    │
    ▼
Number of Services
    │
    ▼
Collect Service Names
    │
    ▼
Store in List
    │
    ▼
Display Inventory
    │
    ▼
Search Requested Service
    │
    ▼
Found?
  /     \
Yes      No
 │        │
 ▼        ▼
Index   Not Found
```

This pattern can be adapted to many DevOps automation tasks.

---

# 36. List and `for` Loop Together

Lists and `for` loops are commonly used together.

```python
services = ["api", "web", "worker"]

for service in services:
    print(service)
```

The loop automatically processes each element.

```text
services
   │
   ├── api
   ├── web
   └── worker
        │
        ▼
      for loop
        │
        ▼
   Process each item
```

---

# 37. List + `range()` + Index

Another common pattern is:

```python
services = ["api", "web", "worker"]

for index in range(len(services)):
    print(index, services[index])
```

Output:

```text
0 api
1 web
2 worker
```

Here:

```text
range(len(services))
```

generates indexes.

And:

```python
services[index]
```

retrieves the corresponding value.

---

# 38. `enumerate()` for Index + Value

Python provides `enumerate()` when both the index and value are required.

```python
services = ["api", "web", "worker"]

for index, service in enumerate(services):
    print(index, service)
```

Output:

```text
0 api
1 web
2 worker
```

If a human-readable position is required:

```python
for index, service in enumerate(services, start=1):
    print(index, service)
```

Output:

```text
1 api
2 web
3 worker
```

This can be cleaner than manually using:

```python
range(len(services))
```

---

# 39. `enumerate()` Concept

```text
List
 │
 ├── api
 ├── web
 └── worker
      │
      ▼
 enumerate()
      │
      ├── (0, api)
      ├── (1, web)
      └── (2, worker)
```

When both position and value are required, `enumerate()` is often useful.

---

# 40. String Methods with List Values

If list elements are strings, string methods can be used while processing them.

```python
services = ["API", "Web", "Worker"]

for service in services:
    print(service.lower())
```

Output:

```text
api
web
worker
```

The original list is not automatically modified.

```python
services = ["API", "Web"]
```

After:

```python
for service in services:
    print(service.lower())
```

the list remains:

```python
["API", "Web"]
```

unless the values are explicitly reassigned.

---

# 41. Normalizing User Input

When comparing user input with stored values, normalization can make comparisons more predictable.

Example:

```python
search_name = input("Enter service: ")

normalized_name = search_name.strip().lower()
```

The `strip()` method removes leading and trailing whitespace.

For example:

```text
"  API  "
```

becomes:

```text
"API"
```

Then:

```python
.lower()
```

produces:

```text
"api"
```

---

# 42. `strip()` + `lower()`

A common input-normalization pattern is:

```python
value = input("Enter value: ").strip().lower()
```

Conceptually:

```text
Raw Input
   │
   ▼
strip()
   │
   ▼
Remove extra spaces
   │
   ▼
lower()
   │
   ▼
Normalize case
   │
   ▼
Comparable value
```

This is useful when user input is used for searching.

---

# 43. Searching with `in` vs Manual Loop

There are two common approaches.

### Membership Test

```python
if service_name in services:
    print("Found")
```

Use this when you only need to know whether the value exists.

### Manual Loop

```python
for index, service in enumerate(services):

    if service == service_name:
        print(index)
        break
```

Use this when you need additional information such as:

- Index
- Matching value
- Custom processing
- Multiple conditions
- Additional actions

---

# 44. Common Error: `IndexError`

Accessing an index that does not exist produces an `IndexError`.

```python
services = ["api", "web"]

print(services[2])
```

Valid indexes are:

```text
0
1
```

Index `2` does not exist.

Therefore Python raises:

```text
IndexError
```

---

# 45. Common Error: Empty List Indexing

This is also invalid:

```python
services = []

print(services[0])
```

There is no element at index `0`.

The list contains:

```text
0 elements
```

Therefore an `IndexError` occurs.

---

# 46. Common Error: Using `len()` as the Last Index

This is incorrect:

```python
services = ["api", "web", "worker"]

print(services[len(services)])
```

Because:

```text
len(services) = 3
```

but valid indexes are:

```text
0
1
2
```

The correct last index is:

```python
len(services) - 1
```

Therefore:

```python
services[len(services) - 1]
```

returns:

```text
worker
```

---

# 47. Common Error: Incorrect `append()` Assignment

Incorrect:

```python
services = services.append("api")
```

After this operation:

```python
services
```

becomes:

```text
None
```

Correct:

```python
services.append("api")
```

The list itself is modified.

---

# 48. Common Error: Confusing Index and Value

Consider:

```python
services = ["api", "web", "worker"]
```

This:

```python
services[1]
```

returns:

```text
web
```

The value:

```text
1
```

is the index.

The value:

```text
web
```

is the element.

They are different concepts.

---

# 49. Common Error: Case-Sensitive Search

This comparison:

```python
"API" == "api"
```

returns:

```text
False
```

If case-insensitive comparison is required:

```python
"API".lower() == "api".lower()
```

returns:

```text
True
```

---

# 50. Common Error: Modifying a List While Iterating

Care should be taken when changing a list while iterating over it.

For example:

```python
for service in services:
    services.remove(service)
```

This can produce unexpected behavior because the collection is being changed while the loop is processing it.

Prefer creating a separate result list or using appropriate filtering techniques when removing multiple elements.

---

# 51. List Mutability

Lists are mutable.

This means:

```python
services[0] = "frontend"
```

can change the existing list.

Example:

```python
services = ["api", "web"]

services[0] = "frontend"
```

Result:

```text
["frontend", "web"]
```

This is different from immutable data types such as strings.

---

# 52. List Slicing

A portion of a list can be extracted using slicing.

```python
services = ["api", "web", "worker", "database"]
```

```python
services[1:3]
```

returns:

```text
["web", "worker"]
```

The general syntax is:

```python
list[start:stop]
```

The `stop` index is excluded.

---

# 53. List Slicing Diagram

For:

```python
services = ["api", "web", "worker", "database"]
```

```text
Index       0       1        2          3
            │       │        │          │
Value      api     web     worker    database
                    │         │
                    └─────────┘
                     [1:3]
```

Result:

```text
["web", "worker"]
```

---

# 54. Useful List Operations

| Operation | Example | Purpose |
|---|---|---|
| Create | `[]` | Create empty list |
| Add | `append()` | Add one item |
| Count | `len()` | Number of items |
| Access | `list[index]` | Get item |
| Modify | `list[index] = value` | Change item |
| Search | `value in list` | Membership test |
| Remove | `remove()` | Remove matching value |
| Remove by index | `pop()` | Remove indexed item |
| Delete | `del` | Delete item |
| Iterate | `for item in list` | Process items |
| Index + value | `enumerate()` | Get both |
| Slice | `list[start:stop]` | Get part of list |

---

# 55. List Processing Patterns

### Collect

```python
items = []

for value in source:
    items.append(value)
```

### Display

```python
for item in items:
    print(item)
```

### Search

```python
if target in items:
    print("Found")
```

### Count

```python
count = 0

for item in items:
    if condition:
        count += 1
```

### Process with Index

```python
for index, item in enumerate(items):
    print(index, item)
```

---

# 56. DevOps Use Case: Service Inventory

A DevOps script may maintain an inventory:

```python
services = [
    "frontend",
    "backend",
    "payment",
    "notification"
]
```

Possible operations:

```text
               Service Inventory
                       │
        ┌──────────────┼──────────────┐
        │              │              │
      Count          Search         Display
        │              │              │
     len()            in          for loop
        │              │              │
        └──────────────┼──────────────┘
                       │
                  Process Data
```

---

# 57. DevOps Use Case: ECS Services

A list can represent ECS service names:

```python
ecs_services = [
    "frontend-service",
    "user-service",
    "payment-service",
    "order-service"
]
```

A loop can process each service:

```python
for service in ecs_services:
    print(service)
```

The same concept can later be combined with AWS SDK operations to:

- Check service status
- Retrieve desired count
- Check running count
- Trigger deployments
- Validate service configuration
- Generate reports

---

# 58. DevOps Use Case: Kubernetes Resources

A list can also represent Kubernetes resources:

```python
pods = [
    "frontend-pod",
    "backend-pod",
    "worker-pod"
]
```

The script can iterate through the list:

```python
for pod in pods:
    print(pod)
```

The same list-processing concepts apply regardless of where the data originated.

---

# 59. DevOps Use Case: File Processing

A script may collect file names:

```python
files = [
    "application.log",
    "error.log",
    "access.log"
]
```

Then process them:

```python
for file in files:
    print(file)
```

Possible automation:

```text
Files
  │
  ▼
List
  │
  ▼
Loop
  │
  ├── Check
  ├── Read
  ├── Filter
  └── Process
```

---

# 60. DevOps Use Case: Deployment Target List

A deployment script may maintain target environments:

```python
environments = [
    "development",
    "staging",
    "production"
]
```

The list can be searched:

```python
if "production" in environments:
    print("Production environment available")
```

This becomes useful when building automation around deployment targets.

---

# 61. Lists as Temporary Data Structures

A Python list is often used as temporary in-memory storage.

For example:

```text
External Source
      │
      ▼
Python Script
      │
      ▼
List
      │
      ▼
Process Data
      │
      ▼
Output / Action
```

The external source could be:

```text
API
AWS
Kubernetes
File
Database
User Input
Command Output
```

---

# 62. Choosing Direct Iteration

Prefer:

```python
for service in services:
    print(service)
```

when the index is not required.

Advantages:

- Simpler
- Easier to read
- Less indexing logic
- Lower chance of index errors

---

# 63. Choosing Index-Based Iteration

Use:

```python
for index in range(len(services)):
    print(index, services[index])
```

when the index itself is required.

Examples:

```text
Need list position
Need to modify by index
Need index-based comparison
Need to display index
```

---

# 64. Choosing `enumerate()`

When both index and value are required, consider:

```python
for index, service in enumerate(services):
    print(index, service)
```

This expresses the intention clearly:

```text
Give me:
    index
    value
```

---

# 65. Choosing `in`

If the only requirement is:

> Does this item exist?

Use:

```python
if target in services:
    print("Found")
```

There is no need to manually iterate through the list just to perform a simple membership test.

---

# 66. Choosing Manual Search

A manual loop is useful when the search requires additional processing.

For example:

```python
for index, service in enumerate(services):

    if service.lower() == target.lower():
        print(f"Found at index {index}")
        break
```

This gives access to:

```text
Value
Index
Comparison logic
Additional actions
```

---

# 67. `break` vs Complete Search

If the requirement is:

> Find the first matching service.

Then:

```python
break
```

is appropriate.

If the requirement is:

> Find every matching service.

Do not stop at the first match.

Conceptually:

```text
First Match Required
        │
        ▼
      break
```

versus:

```text
All Matches Required
        │
        ▼
Continue Loop
```

---

# 68. Complete List Processing Flow

A typical inventory-processing script can follow this structure:

```text
              START
                │
                ▼
        Create Empty List
                │
                ▼
       Receive Input Data
                │
                ▼
         append() Items
                │
                ▼
        List is Populated
                │
                ▼
        Process the List
          /     |      \
         /      |       \
     Display   Count   Search
       │        │        │
       └────────┼────────┘
                │
                ▼
             Result
                │
                ▼
               END
```

---

# 69. Best Practices

### 1. Use descriptive list names

Prefer:

```python
service_names = []
```

over:

```python
x = []
```

---

### 2. Use direct iteration when indexes are unnecessary

Prefer:

```python
for service in services:
    print(service)
```

instead of unnecessarily using:

```python
for index in range(len(services)):
    print(services[index])
```

---

### 3. Use `enumerate()` when both index and value are needed

```python
for index, service in enumerate(services):
    print(index, service)
```

---

### 4. Use `in` for simple membership tests

```python
if service_name in services:
    ...
```

---

### 5. Normalize user input when appropriate

```python
value = input().strip().lower()
```

---

### 6. Do not assign the return value of `append()`

Correct:

```python
services.append("api")
```

---

### 7. Remember zero-based indexing

```text
First element → index 0
Second element → index 1
Third element → index 2
```

---

### 8. Avoid unnecessary index manipulation

If you only need values:

```python
for service in services:
```

is usually clearer.

---

# 70. Quick Reference

```text
Create Empty List
        │
        ▼
items = []
```

```text
Add Item
        │
        ▼
items.append(value)
```

```text
Number of Items
        │
        ▼
len(items)
```

```text
Access Item
        │
        ▼
items[index]
```

```text
Search Item
        │
        ▼
value in items
```

```text
Loop Values
        │
        ▼
for item in items:
```

```text
Loop Index + Value
        │
        ▼
for index, item in enumerate(items):
```

```text
Remove Value
        │
        ▼
items.remove(value)
```

```text
Remove by Index
        │
        ▼
items.pop(index)
```

---

# 71. Common List Questions

### Is a Python list ordered?

Yes.

Lists maintain insertion order.

### Can a list contain duplicate values?

Yes.

```python
items = ["api", "api", "web"]
```

### Can a list be modified?

Yes.

Lists are mutable.

### Does indexing start from 0?

Yes.

### Does `len()` return the last index?

No.

It returns the number of elements.

### Does `append()` return the updated list?

No.

`append()` modifies the list and returns `None`.

### Can a list contain different data types?

Yes.

```python
items = ["api", 10, True, 5.5]
```

Although mixing unrelated types should be done only when it makes sense.

---

# 72. Key Concept Summary

```text
List
 │
 ├── Ordered
 ├── Mutable
 ├── Allows duplicates
 ├── Zero-based indexing
 ├── Supports dynamic growth
 │
 ├── append()
 ├── remove()
 ├── pop()
 ├── len()
 │
 ├── for loop
 ├── enumerate()
 ├── in
 │
 └── Index-based access
```

---

# 73. Key Takeaways

- A **list** stores multiple values in one variable.
- An empty list can be created using `[]` or `list()`.
- `append()` adds an item to the end of a list.
- `append()` modifies the list and returns `None`.
- Python lists use **zero-based indexing**.
- The first element has index `0`.
- `len()` returns the number of elements.
- The last index is `len(list) - 1`.
- Lists can be processed using `for` loops.
- Direct iteration is useful when only values are required.
- `range(len(list))` can be used when indexes are required.
- `enumerate()` provides both index and value.
- `in` performs a membership test.
- String values can be normalized with methods such as `lower()` and `strip()`.
- A Boolean flag can track whether a search was successful.
- `break` can stop searching after the required match is found.
- Lists are mutable and their elements can be changed.
- Lists are heavily used in DevOps automation for inventories, resources, services, files, environments, and deployment targets.