"""
Design Patterns for QA Automation

Common patterns in test automation:
1. Singleton - single instance (e.g., driver, config)
2. Factory - create objects (e.g., test data, drivers)
3. Builder - complex object creation (e.g., test requests)
4. Page Object Model (POM) - encapsulate page interactions
5. Strategy - different test approaches
6. Decorator - add behavior (e.g., logging, retry)
"""


# ============================================================================
# 1. SINGLETON - single instance
# ============================================================================
# Problem: You need only ONE instance of something (e.g., driver, config).
# Solution: Control creation so the same object is reused every time.
# Use in QA: driver, database connection, configuration manager

class DatabaseConnection:
    """Only one database connection exists during tests"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance

    def connect(self):
        self.connected = True
        print("DB connected")

    def is_connected(self):
        return self.connected


def singleton_example():
    print("\n1) SINGLETON - one instance")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print("Same object?", db1 is db2)  # True
    db1.connect()
    print("db2 connected?", db2.is_connected())  # True


# ============================================================================
# 2. FACTORY - create objects
# ============================================================================
# Problem: Creating objects has complex logic (e.g., different test user types).
# Solution: Put creation logic in a factory method or class.
# Use in QA: create test users, test data, driver instances

class TestUser:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"User({self.username}, role={self.role})"


class UserFactory:
    @staticmethod
    def create_admin():
        return TestUser("admin", "admin123", "admin")

    @staticmethod
    def create_regular_user():
        return TestUser("user1", "pass123", "user")

    @staticmethod
    def create_guest():
        return TestUser("guest", "guest123", "guest")


def factory_example():
    print("\n2) FACTORY - create test users")
    admin = UserFactory.create_admin()
    user = UserFactory.create_regular_user()
    guest = UserFactory.create_guest()

    print(admin)
    print(user)
    print(guest)


# ============================================================================
# 3. BUILDER - complex object creation
# ============================================================================
# Problem: Object has many optional parameters (e.g., API request setup).
# Solution: Build it step-by-step with a fluent interface.
# Use in QA: API request builders, test data setup with many options

class TestRequest:
    """Build a complex HTTP request for testing"""

    def __init__(self):
        self.method = None
        self.url = None
        self.headers = {}
        self.body = None

    def __repr__(self):
        return f"Request({self.method} {self.url}, headers={self.headers})"


class RequestBuilder:
    def __init__(self):
        self.request = TestRequest()

    def with_method(self, method):
        self.request.method = method
        return self

    def with_url(self, url):
        self.request.url = url
        return self

    def with_header(self, key, value):
        self.request.headers[key] = value
        return self

    def with_body(self, body):
        self.request.body = body
        return self

    def build(self):
        return self.request


def builder_example():
    print("\n3) BUILDER - build complex request")
    request = (RequestBuilder()
               .with_method("POST")
               .with_url("https://api.example.com/users")
               .with_header("Content-Type", "application/json")
               .with_header("Authorization", "Bearer token123")
               .with_body({"name": "John"})
               .build())

    print(request)


# ============================================================================
# 4. PAGE OBJECT MODEL (POM) - encapsulate page
# ============================================================================
# Problem: Page selectors and interactions scattered across tests.
# Solution: Create a class per page that encapsulates selectors and actions.
# Use in QA: UI automation, selenium, reduce duplication, easy maintenance

class LoginPage:
    """Encapsulate login page interactions"""

    def __init__(self, driver_name="chrome"):
        self.driver = driver_name
        self.username_field = "input#username" # page locator
        self.password_field = "input#password" # page locator
        self.login_button = "button#login" # page locator

    def enter_username(self, username): # action
        print(f"{self.driver}: typing {username} in {self.username_field}")

    def enter_password(self, password): # action
        print(f"{self.driver}: typing {password} in {self.password_field}")

    def click_login(self): # action
        print(f"{self.driver}: clicking {self.login_button}")

    def login(self, username, password):
        """High-level action"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


def pom_example():
    print("\n4) PAGE OBJECT MODEL - encapsulate page")
    page = LoginPage("chrome")
    page.login("john@example.com", "secret123")


# ============================================================================
# 5. STRATEGY - different test approaches
# ============================================================================
# Problem: Different ways to achieve same goal (standard login, social, MFA).
# Solution: Define each approach as a separate strategy, swap at runtime.
# Use in QA: test different login methods, API vs UI testing, different browsers

class LoginStrategy:
    """Base strategy for login"""

    def login(self, username, password):
        raise NotImplementedError


class StandardLogin(LoginStrategy):
    def login(self, username, password):
        return f"Standard login: {username}"


class SocialLogin(LoginStrategy):
    def login(self, username, password):
        return f"Social login: {username}"


class MFALogin(LoginStrategy):
    def login(self, username, password):
        return f"MFA login: {username} (requires 2FA)"


class TestRunner:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_login(self, username, password):
        return self.strategy.login(username, password)


def strategy_example():
    print("\n5) STRATEGY - different login approaches")

    runner = TestRunner(StandardLogin())
    print(runner.execute_login("user1", "pass"))

    runner = TestRunner(SocialLogin())
    print(runner.execute_login("user1", "pass"))

    runner = TestRunner(MFALogin())
    print(runner.execute_login("user1", "pass"))


# ============================================================================
# 6. DECORATOR - add behavior (retry, logging)
# ============================================================================
# Problem: Add extra behavior to functions without changing them (logging, retry).
# Solution: Wrap the function with a decorator that adds the behavior.
# Use in QA: retry flaky tests, log test execution, measure performance, timeout handling

def retry(max_attempts=3):
    """Decorator: retry test if it fails"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"Attempt {attempt}: {func.__name__}")
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"  Failed, retrying...")
        return wrapper
    return decorator


@retry(max_attempts=3)
def flaky_test():
    """Simulates a flaky test"""
    import random
    if random.random() < 0.7:
        raise AssertionError("Test failed randomly")
    return "Test passed"


def decorator_example():
    print("\n6) DECORATOR - retry flaky test")
    try:
        result = flaky_test()
        print(f"Final result: {result}")
    except AssertionError as e:
        print(f"Failed after retries: {e}")


# ============================================================================
def main():
    print("=" * 70)
    print("Design Patterns for QA Automation - Learning Roadmap")
    print("=" * 70)

    singleton_example()
    factory_example()
    builder_example()
    pom_example()
    strategy_example()
    decorator_example()

    print("\n" + "=" * 70)
    print("Interview tips:")
    print("- Singleton: driver, config, database connections")
    print("- Factory: test data, driver creation")
    print("- Builder: complex request/test data setup")
    print("- POM: organize page interactions, reuse selectors")
    print("- Strategy: different testing approaches (API, UI, mobile)")
    print("- Decorator: logging, retries, performance metrics")
    print("=" * 70)


if __name__ == "__main__":
    main()
