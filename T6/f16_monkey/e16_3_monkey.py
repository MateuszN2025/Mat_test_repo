import wrapping


def original_func():
    print(">>> original <<<")
    
def monkey_func():
    print("monkey🐒")

@wrapping
def main():
    """IMPORTANT"""
    global original_func
    # do not create a local variable named original_func
    # use the module-level name instead
#
    
    print("=== MONKEY ===")
    original_func()
    monkey_func()
    print(f"original_func(): {original_func()}")
    # original_func = lambda: None
    # print(f"original_func  : {original_func}")
    original_func = monkey_func
    original_func()
#
main()

# print("=== MONKEY ===")
# original_func()
# monkey_func()
"""IMPORTANT"""
# original_func = monkey_func
# original_func()