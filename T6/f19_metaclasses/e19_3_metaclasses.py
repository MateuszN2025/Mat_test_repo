import w_r

class TestCaseMeta(type):
    # Registry lets the framework discover every valid test class.
    registry = {}

    def __new__(mcls, name, bases, namespace):
        # Allow the shared base class to be created without validation.
        if name == "BaseTest":
            return super().__new__(mcls, name, bases, namespace)

        # bases contains the parent classes declared in the class header.
        if not any(base.__name__ == "BaseTest" for base in bases):
            raise TypeError(f"{name} must inherit from BaseTest")

        if not name.startswith("Test"):
            raise TypeError("Test class must start with 'Test'")

        # namespace is the class body before Python turns it into a class object.
        endpoint = namespace.get("endpoint")
        # data = {"endpoint": "/users"}
        # value = data.get("endpoint")
        if not isinstance(endpoint, str) or not endpoint.startswith("/"):
            raise TypeError(f"{name} must define endpoint like '/users'")

        test_methods = [attr_name for attr_name, value in namespace.items()
                        if attr_name.startswith("test_") and callable(value)]
        if not test_methods:
            raise TypeError(f"{name} must define at least one test_ method")

        # Add derived metadata to the class before it is created.
        namespace["declared_test_methods"] = tuple(sorted(test_methods))
        cls = super().__new__(mcls, name, bases, namespace)
        # Keep a central registry for discovery or reporting.
        mcls.registry[name] = cls
        return cls


class BaseTest(metaclass=TestCaseMeta):
    base_url = "https://api.example.com"


class TestUsersApi(BaseTest):
    endpoint = "/users"

    def test_get_users(self):
        return f"GET {self.base_url}{self.endpoint}"

    def test_create_user(self):
        return f"POST {self.base_url}{self.endpoint}"

@w_r
def main():
    test_case = TestUsersApi()
    print(TestUsersApi.declared_test_methods)
    print(test_case.test_get_users())
    print(sorted(TestCaseMeta.registry))
    print("------------------------------------------")
    data = {"endpoint": "/users"}
    value = data.get("endpoint")
    print(value) # /users
    print("------------------------------------------")


if __name__ == "__main__":
    main()