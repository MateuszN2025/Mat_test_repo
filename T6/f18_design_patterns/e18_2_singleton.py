import w_r
from threading import Lock


class ApiSession:
	_instance = None
	_lock = Lock()

	def __new__(cls):
		if cls._instance is None:
			# Only one thread can create the shared test session.
			with cls._lock:
				if cls._instance is None:
					cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self, base_url="https://test-api.local"):
		# Avoid resetting the session when another test asks for the same object.
		if getattr(self, "_initialized", False): 
        # Safety: getattr(self, "_initialized", False) returns False when the attribute doesn't exist. 
			return

		self.base_url = base_url
		self.auth_token = "token-from-login"
		self._initialized = True

	def get_headers(self):
		return {"Authorization": f"Bearer {self.auth_token}"}


def test_login_endpoint():
    session = ApiSession()
    # pretend login happened once
    # later tests reuse the same authenticated session
    print("login test uses:", session.base_url, session.get_headers())
    print(session)
    return session

def test_profile_endpoint():
    session = ApiSession()
    print("profile test uses:", session.base_url, session.get_headers())
    print(session)
    return session


@w_r
def main():
	session_1 = test_login_endpoint()
	session_2 = test_profile_endpoint()

	print("same shared session:", session_1 is session_2)


main()

"""
import pytest


class ApiSession:
    def __init__(self, base_url="https://test-api.local"):
        self.base_url = base_url
        self.auth_token = "token-from-login"

    def get_headers(self):
        return {"Authorization": f"Bearer {self.auth_token}"}

--------------------------------------------------------

@pytest.fixture(scope="session")
def api_session():
    return ApiSession()
    
    
def test_login_endpoint(api_session):
    print(api_session.base_url, api_session.get_headers())


def test_profile_endpoint(api_session):
    print(api_session.base_url, api_session.get_headers()) 
"""

