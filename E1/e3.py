x = 3
print(3 % 60)
print(65 % 60)
print(10 % 3)
print(62 / 60) # 1.033...
print(62 // 60) # 1
print(62 % 60) # 2
print(5 // 60) # 0.083...
print((1 // 60) % 60)
print((130 // 60) % 60)
print(int(130 / 60) % 60)

# make a rectangle with raws, columns and specify filling with specific character

"""
| Feature                           | List               | Tuple                         | Set                                 | Dictionary                 |
| --------------------------------- | ------------------ | ----------------------------- | ----------------------------------- | -------------------------- |
| **Syntax**                        | `[ ]`              | `( )`                         | `{ }`                               | `{key: value}`             |
| **Ordered?**                      | Yes                | Yes                           | No (unordered)                      | Yes *(Python 3.7+)*        |
| **Mutable?**                      | Yes                | No                            | Yes                                 | Yes                        |
| **Allows Duplicates?**            | Yes                | Yes                           | No                                  | Keys: No, Values: Yes      |
| **Indexed?**                      | Yes                | Yes                           | No                                  | By keys                    |
| **Stores**                        | Sequence of items  | Fixed sequence of items       | Unique items                        | Key-value pairs            |
| **Can Contain Mixed Data Types?** | Yes                | Yes                           | Yes                                 | Yes                        |
| **Hashable / Can Be Key?**        | No                 | Yes *(if immutable contents)* | No                                  | No                         |
| **Common Use Case**               | Dynamic collection | Fixed/constant data           | Remove duplicates, membership tests | Structured data / mappings |
| **Example**                       | `[1, 2, 3]`        | `(1, 2, 3)`                   | `{1, 2, 3}`                         | `{"a": 1, "b": 2}`         |
"""

"""

* is only syntax for packing or unpacking at the point where Python parses the function definition or call. args is just the variable name that exists inside the function.

Example:
def f(*args):
    print(args)

What this means is:

In the function definition, *args tells Python: "collect all extra positional arguments into one tuple".
Inside the function body, that collected tuple is stored in a normal variable named args.
After that, you use args because * is not part of the variable name.
So this:
def f(*args):
    print(args)

is roughly like saying:

take many positional arguments
pack them into a tuple
name that tuple args
Example call:
f(1, 2, 3)

Inside the function:
args == (1, 2, 3)

The same idea applies in calls:
numbers = [1, 2, 3]
f(*numbers)

Here *numbers means: unpack the list into separate positional arguments.

Short version:

*args in a definition = pack incoming positional arguments
*something in a call = unpack a sequence into positional arguments
args inside the function = just the normal variable holding the packed values
"""