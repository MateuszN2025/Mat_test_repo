import requests
import pytest

def test_standalone_get_status_code_all_users(run_app: dict):
    response = requests.get(url=run_app['url'])
    # print(f"response.json()|{response.json()}") # dict, list, etc.
    # print(f"response.text|{response.text}") # str 
    assert response.status_code == 200, "wrong status code"

# TestLogin
# TestUserRegistration
# TestCheckoutFlow
# TestShoppingCart
# TestPasswordReset

class TestClass:
    def test_1_get_status_code_all_users(self, run_app: dict):
        response = requests.get(url=run_app['url'])
        assert response.status_code == 200, "wrong status code"
        
    @pytest.mark.easy
    @pytest.mark.parametrize("u_id, exp_data, exp_sts",
                            ((1, {"id":1,"name":"Bob","age":43}, 200),
                            (2, {"id":2,"name":"Sam","age":54}, 200),
                            (3, {'detail': 'User not found'}, 404)))
    def test_2_get_status_code_one_user(self, run_app, log_time, u_id, exp_data, exp_sts):
        response = requests.get(url=f"{run_app['url']}/{u_id}")
        assert response.json() == exp_data
        assert response.status_code == exp_sts, "wrong status code"
    