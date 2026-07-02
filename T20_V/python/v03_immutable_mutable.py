# Senior insight: Python's model is technically called 
# pass-by-object-reference (not "by value" or "by reference").
# Whether a function can affect the caller depends entirely
# on whether the object is mutable — not on how you pass it.

def func(var: int) -> int:
    # 'var' is a local name — rebinding it does NOT affect the caller's variable
    print("  inside func, before rebind, id(var):", id(var))   # same id as 'a'
    var = 10
    print("  inside func, after rebind,  id(var):", id(var))   # DIFFERENT — new int object
    return var

def func_list(var_l: list) -> list:
    # 'var_l' points to the SAME list object as the caller — mutation IS visible outside
    print("  inside func_list, before mutation, id(var_l):", id(var_l))  # same id as b_list
    # var_l[0] = 200 # changing the same list object (mutation)
    var_l = [999] # new list creation - different object (rebind)
    print("  inside func_list, after rebind,  id(var_l):", id(var_l))  # DIFFERENT — new object, b_list outside unchanged
    return var_l

a = 2
b_list = [3]

print("------------------------------------------")
print("var a immutable")
print(a, "id:", id(a))          # 2
print("function call")
print(func(a))                  # 10 — local rebind, caller's 'a' unchanged
print("var a again")
print(a, "id:", id(a))          # still 2, same id — object never changed
print("------------------------------------------")
print("var b_list mutable")
print(b_list, "id:", id(b_list))    # [3]
print("function call")
print(func_list(b_list))            # [200] — mutated in place
print("var b_list again")
print(b_list, "id:", id(b_list))    # (mutation) [200], SAME id — same object, different content
                                    # (rebind) still [3], DIFFERENT id from var_l inside — rebind didn't reach caller
                                    
                                    
def increment(n: int) -> int:
    return n + 1

print("------------------------------------------")
count = 0
# count = increment(count)  # count is now 1
# count = ...  →  rebinds the name 'count' to the returned value 1
# print(count) # 1
increment(count)
print(count)

def aaa(n: int) -> int:
    ...