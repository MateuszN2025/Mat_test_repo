import requests
import pytest


# 1. Keep it in the Test File (Local Scope)
#   If data_payload is only ever going to be used by tests 
#   inside this specific file, leave it exactly where it is.

@pytest.fixture
def data_payload():
    return {
        "name": "Manny",
        "age": 98
    }


@pytest.mark.hard
def test_3_post_add_new_user(run_app: dict, data_payload: dict):
    session = requests.Session()
    response_post = session.post(url=run_app['url'], json=data_payload)
    assert response_post.status_code == 201, "❌ user cannot be created ❌"
    new_id = response_post.json()["id"]
    # Creates a brand new dictionary combining the fixture data and the new ID
    expected_user_data = {**data_payload, "id": new_id}
    response_get = session.get(url=f"{run_app['url']}/{new_id}")
    assert response_get.status_code == 200, "❌ user unavailable ❌"
    assert expected_user_data == response_get.json(), "❌ data inconsistent ❌"
    response_delete = session.delete(url=f"{run_app['url']}/{new_id}")
    assert response_delete.status_code in [200, 202, 204]
    
    
    
    """
    2. Test Teardown (Cleanup)
    In API testing, it is a best practice to leave the database exactly as you found it.
    You can do this by adding a DELETE request at the very end of your test to remove "Manny".
    This prevents your test database from filling up with hundreds of 
    identical users every time your CI/CD pipeline runs.
    """
    
    
    # for user in response_get.json():
    #     id_list.append(user["id"])
    # new_id = max(id_list)
    # new_user_data = dict1
    # new_user_data["id"] = new_id
    # print(f"new_user_data|{new_user_data}")
    # print(f"new_user_data|{response_get.json()[new_id-1]}")
    # assert new_user_data == response_get.json()[new_id-1]
    

# import requests
# import pytest

# @pytest.mark.hard
# def test_3_post_add_new_user(run_app: dict):
#     # 1. Define test data locally to prevent global state mutation
#     user_payload = {
#         "name": "Manny",
#         "age": 98
#     }

#     # 2. Create the user
#     response_post = requests.post(url=run_app['url'], json=user_payload)
#     assert response_post.status_code == 201, f"❌ user cannot be created. Response: {response_post.text} ❌"
    
#     # 3. Get all users and parse JSON exactly once
#     response_get = requests.get(url=run_app['url'])
#     assert response_get.status_code == 200, "❌ Failed to fetch users ❌"
#     users_list = response_get.json()

#     # 4. Find the new ID safely using a list comprehension
#     id_list = [user["id"] for user in users_list]
#     new_id = max(id_list)

#     # 5. Find the actual user in the list rather than guessing the index
#     created_user = next((user for user in users_list if user["id"] == new_id), None)
#     assert created_user is not None, f"❌ User with ID {new_id} not found in GET response ❌"

#     # 6. Prepare expected data and assert
#     expected_user_data = user_payload.copy()
#     expected_user_data["id"] = new_id
    
#     assert expected_user_data == created_user, "❌ Created user data does not match payload ❌"
