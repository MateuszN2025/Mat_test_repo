import w_r

class SimpleMeta(type):
    def __new__(mcls, name, bases, namespace):
        namespace["created_by_meta"] = True
        print("------------------------------------------")
        print(f"name {name}")
        print(f"bases {bases}")
        print(f"namespace {namespace}")
        print("------------------------------------------")
        # __new__ must return the newly created class object.
        return super().__new__(mcls, name, bases, namespace)

class Cat(metaclass=SimpleMeta):
    #                       mcls     name   bases     namespace
    # SimpleMeta.__new__(SimpleMeta, "Cat", (), {"__module__": "...", "__qualname__": "Cat"})
    pass

# @w_r
def main():
    c1 = Cat()
    print(c1.created_by_meta)
    
main()