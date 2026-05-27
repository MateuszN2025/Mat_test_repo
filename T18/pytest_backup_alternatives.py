import pytest
import requests

# ==============================================================================
# PRE-REQUISITE: Dummy 'run_app' fixture
# (Added so the test functions have the expected dependencies)
# ==============================================================================
@pytest.fixture
def run_app():
    return {"url": "https://api.example.com/users"}


# ==============================================================================
# ALTERNATIVE 1: Yield a Tuple (Simplest)
# ==============================================================================
@pytest.fixture
def api_setup():
    with requests.Session() as session:
        restore_queue = []
        
        def backup_user(url):
            response = session.get(url)
            if response.status_code == 200:
                restore_queue.append((url, response.json()))
            return response
        
        # Yield them together as a tuple
        yield session, backup_user
        
        for url, original_data in restore_queue:
            session.put(url, json=original_data)

@pytest.mark.parametrize("user_id, exp_resp", ((2, 200), (3, 200)))
def test_PUT_t5_alt1(run_app, api_setup, user_id, exp_resp):
    # Unpack the tuple right at the start of the test
    session, backup_user = api_setup
    
    user_url = f"{run_app['url']}/{user_id}"    
    
    # Use the separated function and session
    response_get = backup_user(user_url)    
    response_put = session.put(user_url, json={"name": "Klint"})


# ==============================================================================
# ALTERNATIVE 2: A Custom Wrapper Class (Most Robust)
# ==============================================================================
class TestClient:
    def __init__(self):
        self.session = requests.Session()
        self.restore_queue = []

    def backup_user(self, url):
        response = self.session.get(url)
        if response.status_code == 200:
            self.restore_queue.append((url, response.json()))
        return response

    def restore_all(self):
        for url, original_data in self.restore_queue:
            self.session.put(url, json=original_data)
        self.session.close()

@pytest.fixture
def client():
    # Instantiate your custom client
    api_client = TestClient()
    yield api_client
    
    # Trigger the cleanup explicitly
    api_client.restore_all()

@pytest.mark.parametrize("user_id, exp_resp", ((2, 200), (3, 200)))
def test_PUT_t5_alt2(run_app, client, user_id, exp_resp):
    user_url = f"{run_app['url']}/{user_id}"    
    
    # Use your custom class methods
    response_get = client.backup_user(user_url)    
    response_put = client.session.put(user_url, json={"name": "Klint"})


# ==============================================================================
# ALTERNATIVE 3: A Separate Fixture for Backups (Most "pytest-like")
# ==============================================================================
@pytest.fixture
def session_fixture():
    # Keep this pure and simple
    with requests.Session() as session:
        yield session

@pytest.fixture
def backup_user(session_fixture):
    # This fixture USES the session_fixture
    restore_queue = []
    
    def _backup(url):
        response = session_fixture.get(url)
        if response.status_code == 200:
            restore_queue.append((url, response.json()))
        return response
        
    yield _backup
    
    # Teardown logic
    for url, original_data in restore_queue:
        session_fixture.put(url, json=original_data)

@pytest.mark.parametrize("user_id, exp_resp", ((2, 200), (3, 200)))
def test_PUT_t5_alt3(run_app, session_fixture, backup_user, user_id, exp_resp):
    user_url = f"{run_app['url']}/{user_id}"    
    
    # Call the backup fixture like a normal function
    response_get = backup_user(user_url)    
    
    # Use the standard session fixture for normal requests
    response_put = session_fixture.put(user_url, json={"name": "Klint"})
