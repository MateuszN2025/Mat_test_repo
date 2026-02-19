import requests

class APITestSuite:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json'
        }

    def test_endpoint_availability(self, endpoint):
        """Test if endpoint is accessible"""
        response = requests.get(f"{self.base_url}{endpoint}")
        assert response.status_code == 200, f"Endpoint {endpoint} not accessible"

    def test_create_resource(self, endpoint, payload):
        """Test resource creation"""
        response = requests.post(
            f"{self.base_url}{endpoint}", 
            json=payload, 
            headers=self.headers
        )
        assert response.status_code == 201
        return response.json()

    def test_update_resource(self, endpoint, resource_id, payload):
        """Test resource update"""
        response = requests.put(
            f"{self.base_url}{endpoint}/{resource_id}", 
            json=payload, 
            headers=self.headers
        )
        assert response.status_code == 200


# Example Usage
def run_api_tests():
    api_test = APITestSuite('https://api.example.com')

    # Test user endpoint
    api_test.test_endpoint_availability('/users')

    # Create user
    new_user = {
        'name': 'John Doe',
        'email': 'john@example.com'
    }
    created_user = api_test.test_create_resource('/users', new_user)
    
    # Update user
    update_payload = {'name': 'John Updated'}
    api_test.test_update_resource('/users', created_user['id'], update_payload)

run_api_tests()