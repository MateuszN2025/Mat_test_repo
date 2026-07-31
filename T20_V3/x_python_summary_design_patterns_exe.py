print("------------------------------------------")
# ============================================================================
# 1. SINGLETON - single instance
# ============================================================================
# Problem: You need only ONE instance of something (e.g., driver, config).
# Solution: Control creation so the same object is reused every time.
# Use in QA: driver, database connection, configuration manager

"""

It avoids creating the same heavy object many times.
It gives one consistent state and one access point across the framework.

Short answer:
We use singleton in tests to share one common object, save setup cost,
and keep one source of truth. But in most modern Python test frameworks,
fixtures are safer and more maintainable. 

If creating the object is expensive, singleton reduces waste.
tradeoff:
Singletons often make tests harder to isolate.
Shared global state can leak between tests.
Debugging becomes harder when one test changes
the singleton and another test fails later.

Better design with fixtureℹ️

"""

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

singleton_example()

print("------------------------------------------")

# ============================================================================
# 2. FACTORY - create objects
# ============================================================================
# Problem: Creating objects has complex logic (e.g., different test user types).
# Solution: Put creation logic in a factory method or class.
# Use in QA: create test users, test data, driver instances

"""

If you create them manually in every test, you repeat setup and make tests noisy.
It removes duplicate setup from tests.
It keeps test data consistent.
If object creation changes, you update it once in the factory instead of many tests.
It makes tests easier to read because the test focuses on behavior, not setup details.

"""

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
    
factory_example()

print("------------------------------------------")

# ============================================================================
# 3. BUILDER - complex object creation
# ============================================================================
# Problem: Object has many optional parameters (e.g., API request setup).
# Solution: Build it step-by-step with a fluent interface.
# Use in QA: API request builders, test data setup with many options

"""

You can build complex objects gradually
The test code stays readable

TestRequest = the product
RequestBuilder = the mechanic assembling the product
self.request = the product currently being assembled

This is exactly why Builder is different from Factory. 
A factory usually creates and returns a ready object in one step. 
A builder creates an empty or partial object first, 
keeps it in internal state, and lets you shape it over multiple steps. 

Builder needs internal state because it builds 
the same object across several steps, while 
Factory usually creates and returns the object in one step. 

Short version:
Builder: "start now, finish later"
Factory: "create now, return now"

Factory creates a ready object in one step, 
while Builder creates an object gradually, 
so it can be configured and changed step by step before it is returned. 

"""

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
    
builder_example()


print("------------------------------------------")


# ============================================================================
# 4. PAGE OBJECT MODEL (POM) - encapsulate page
# ============================================================================
# Problem: Page selectors and interactions scattered across tests.
# Solution: Create a class per page that encapsulates selectors and actions.
# Use in QA: UI automation, selenium, reduce duplication, easy maintenance

"""

Why we use POM:
selectors are in one place
UI changes are easier to fix
tests are easier to read
duplication is reduced
POM makes tests simpler because 
page-related UI logic is encapsulated in a class. 

"""

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
    
pom_example()

print("------------------------------------------")