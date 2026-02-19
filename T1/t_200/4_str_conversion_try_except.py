# 4. Convert a string to an integer safely (with exception handling).
def convert_str_to_int_safely(a):
    try:
        conv = int(a)
    except:
        print(f"{a} is not a valid number")
        """
        Bare except: is risky
        Catching everything can hide real bugs (like KeyboardInterrupt).
        👉 Better to catch specific exceptions:
        ValueError → invalid string
        TypeError → None, wrong type
        """
    else:
        print(f"Conversion from {a} to {conv} is done propely")
    finally:
        print("Function is finished")

convert_str_to_int_safely("8982")
b = ""
print(f"Insert Your string: {b}")
b = input()
print("convert_str_to_int_safely RUN:")
convert_str_to_int_safely(b)

#########################################
# improved version
#########################################

def convert_str_to_int_safely(a):
    try:
        conv = int(a)
    except ValueError:
        print(f"'{a}' is not a valid number")
        return None
    except TypeError:
        print("Input must be a string or number")
        return None
    else:
        print(f"Conversion from '{a}' to {conv} is done properly")
        return conv
    finally:
        print("Function is finished")


convert_str_to_int_safely("8982")

b = input("Insert your string: ")
print("convert_str_to_int_safely RUN:")
convert_str_to_int_safely(b)


# Interview-style solution
def convert_str_to_int_safely(value):
    """
    Safely converts a string to an integer.

    Args:
        value (str): The value to convert

    Returns:
        int | None: Converted integer if successful, otherwise None
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

"""
assert convert_str_to_int_safely("42") == 42
assert convert_str_to_int_safely("abc") is None
assert convert_str_to_int_safely(None) is None
"""