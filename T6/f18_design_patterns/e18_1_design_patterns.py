"""
Fast roadmap: 3 design patterns worth learning first for test automation.

Order to learn:
1. Factory - you create test data, drivers, clients all the time.
2. Page Object Model (POM) - the default structure for UI automation.
3. Singleton - useful, but apply carefully for shared config/session objects.

What matters:
- Learn the problem each pattern solves before memorizing definitions.
- Keep examples close to test code: driver, page, user, API client.
- In automation, readability and maintenance matter more than cleverness.

Senior insight:
- Factory and POM remove duplication safely.
- Singleton can hide state and make tests order-dependent, so use it sparingly.

Short practice task:
- Build one LoginPage, one WebDriverFactory, and one Config singleton.
"""
import w_r

def print_roadmap():
	roadmap = """
================ FAST ROADMAP FOR QA AUTOMATION ================

1. FACTORY
Why first:
- In tests, you constantly create objects: drivers, users, payloads, API clients.
- Factory gives one place for creation rules.

Learn this:
- Hide object creation behind a function or class.
- Return different objects for different environments or test roles.

Use in automation:
- create_driver("chrome")
- create_user("admin")
- create_api_client("staging")

Common mistake:
- Putting test logic into the factory instead of only creation logic.

2. PAGE OBJECT MODEL (POM)
Why second:
- UI tests become unreadable when selectors and click/type steps are repeated.
- POM separates page behavior from test assertions.

Learn this:
- One class per page or page fragment.
- Keep locators and user actions inside the page object.
- Keep assertions mostly in the test layer.

Use in automation:
- LoginPage(driver).login("user", "secret")

Common mistake:
- Turning page objects into giant classes with too many assertions.

3. SINGLETON
Why third:
- It is common for config, logger, or one shared session object.
- It is easy to misuse and create hidden shared state.

Learn this:
- Ensure only one instance exists.
- Understand when shared state is safe and when it breaks test isolation.

Use in automation:
- config manager
- logger
- sometimes a session manager

Common mistake:
- Using singleton for webdriver in parallel tests.

Recommended study flow:
- Day 1: write a Factory for users and drivers.
- Day 2: move a login test into POM.
- Day 3: implement a small Config singleton and discuss tradeoffs.
"""
	# print(roadmap)


class Driver:
	def __init__(self, browser_name):
		self.browser_name = browser_name

	def __repr__(self):
		return f"Driver(browser='{self.browser_name}')"


class DriverFactory:
	@staticmethod
	def create(browser_name):
		supported_browsers = {"chrome", "firefox", "edge"}
		if browser_name not in supported_browsers:
			raise ValueError(f"Unsupported browser: {browser_name}")
		return Driver(browser_name)


class Config:
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance.base_url = "https://test-app.local"
		return cls._instance


class LoginPage:
	def __init__(self, driver):
		self.driver = driver
		self.username_input = "#username"
		self.password_input = "#password"
		self.submit_button = "#submit"

	# Keep selectors and user actions here so tests stay readable and stable.
	def login(self, username, password):
		return (
			f"[{self.driver.browser_name}] type '{username}' into {self.username_input}, "
			f"type '{password}' into {self.password_input}, click {self.submit_button}"
		)

@w_r
def run_examples():
	print("\n================ TINY EXAMPLES ================")

	chrome_driver = DriverFactory.create("chrome")
	print("Factory:", chrome_driver)

	config_a = Config()
	config_b = Config()
	print("Singleton same object:", config_a is config_b)
	print("Singleton base_url:", config_a.base_url)

	login_page = LoginPage(chrome_driver)
	print("POM:", login_page.login("admin", "secret"))


if __name__ == "__main__":
	print_roadmap()
	run_examples()
