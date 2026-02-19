class Functions:
    def __init__(self, *args):
        self.args = args

    def func_add(self):
        total = 0
        for item in self.args:
            if isinstance(item, list):
                total += sum(item)
            else:
                total += item
        return total

# Examples
f1 = Functions([3, 2, 3, 4])          # one list
f2 = Functions([1, 2], [3, 4, 5])     # multiple lists
f3 = Functions([1, 2], 10, 20)        # mix of list + numbers

print(f1.func_add())  # 12
print(f2.func_add())  # 15
print(f3.func_add())  # 33

# | Call              | `args` becomes   |
# | ----------------- | ---------------- |
# | `f(1,2,3)`        | `(1,2,3)`        |
# | `f([1,2,3])`      | `([1,2,3],)`     |
# | `f([1,2], [3,4])` | `([1,2], [3,4])` |
#So be careful — lists become one argument, not multiple numbers.
print("###############################")

def sum_only_numbers(*args):
    total = 0
    for value in args:
        if isinstance(value, (int, float)):  # check if number
            total += value
    return total

print(sum_only_numbers(3, "Hi", 7.5, [2,3]))


