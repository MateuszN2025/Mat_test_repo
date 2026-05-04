import w_r


# class UpperText(str):
#     def __new__(cls, value):
#         return super().__new__(cls, value.upper())

class TraceMeta(type):
    def __prepare__(name, bases):
        print("1. TraceMeta.__prepare__")
        return {}

    def __new__(mcls, name, bases, namespace):
        print("2. TraceMeta.__new__")
        return super().__new__(mcls, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        print("3. TraceMeta.__init__")
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print("4. TraceMeta.__call__")
        return super().__call__(*args, **kwargs)


class User(metaclass=TraceMeta):
    print("class body is executing")

    def __new__(cls, name):
        print("5. User.__new__")
        return super().__new__(cls)

    def __init__(self, name):
        print("6. User.__init__")
        self.name = name





# @w_r
def main():
    # text = UpperText("hello")
    # print(text)   # HELLO
    print("------------------------------------------")
    u = User("Alice")
    print(u.name)
    
main()