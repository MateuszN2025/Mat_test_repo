import pytest
import requests

@pytest.fixture
def session_fixture():
    with requests.Session() as session:
        # Keep track of URLs and their original data
        restore_queue = []
        
        # 1. The Problem This Solves
        # In your original code, the fixture tried to tear down (restore) the data,
        # but it didn't know the user_url because user_url was defined inside the test function.
        # Define a helper function to back up the data
        # Inner function remembers the variables from the outer function
        def backup_user(url):
            response = session.get(url)
            if response.status_code == 200:
                restore_queue.append((url, response.json()))
            return response
        
        # Attach the helper to the session object so tests can use it
        # Dynamic Assignment (Monkey-Patching)
        # Because we attached backup_user directly to the session object,
        # and the fixture yields that session object to the test,
        # your test function now has a specialized tool!
        # session.backup_user = backup_user
        
        
        session.backup_user = backup_user
        yield session
       
        
        # Pass the session to the test
        # yield session, backup_user
        
        # TEARDOWN: Restore the original data for any backed-up URLs
        for url, original_data in restore_queue:
            session.put(url, json=original_data)


@pytest.mark.parametrize("user_id, exp_resp",
                         ((2, 200),
                          (3, 200)))
def test_PUT_t5(run_app, session_fixture: requests.Session, user_id, exp_resp):
    
    # session, backup_user = session_fixture
    
    new_user_data = {"name": "Klint", "age": 133}
    new_user_exp_data = {"id": user_id, **new_user_data}
    user_url = f"{run_app['url']}/{user_id}"    
    
    # 1. Check if user exists AND tell the fixture to back them up
    # response_get = backup_user(user_url) 
    response_get = session_fixture.backup_user(user_url)    
    if response_get.status_code != 200:
        pytest.fail(reason=f"User {user_id} does not exist.", pytrace=False)

    # 2. Update the user
    # response_put = session.put(user_url, json=new_user_data)
    response_put = session_fixture.put(user_url, json=new_user_data)
    assert response_put.status_code == exp_resp, f"User update failed. Status: {response_put.status_code}"
    
    # 3. Retrieve and verify the updated user
    # response_put = session.get(user_url) 
    response_get_updated = session_fixture.get(user_url) 
    assert response_get_updated.status_code == exp_resp, "Updated user could not be retrieved."
    assert new_user_exp_data == response_get_updated.json(), "Data returned does not match the payload sent."

# #####################################################            
# @pytest.mark.parametrize("user_id, exp_resp",
#                          ((1, 200),
#                           (2, 200),
#                           (3, 200)))
# def test_PUT_t5(run_app, user_id, exp_resp):
    
#     new_user_data = {"name": "Klint", "age": 133}
#     new_user_exp_data = {"id": user_id, **new_user_data}
#     user_url = f"{run_app['url']}/{user_id}"
#     # base_url = run_app['url']
    
#     with requests.Session() as session:
#         response_get = session.get(user_url)
#         # print(f"ℹ️ {session.get(base_url).json()}")
        
#         if response_get.status_code != 200:
#             pytest.fail(reason=f"User {user_id} does not exist.", pytrace=False)
#         preserve_previous_user_data = response_get.json()
        
#         try:
#             response_put = session.put(user_url, json=new_user_data)
#             assert response_put.status_code == exp_resp, f"User update failed. Status: {response_put.status_code}"
#             response_get = session.get(user_url) 
#             # print(f"ℹ️ {session.get(base_url).json()}")
#             assert response_get.status_code == exp_resp, "Updated user could not be retrieved."
#             assert new_user_exp_data == response_get.json(), "Data returned does not match the payload sent."
#         finally:
#             response_put = session.put(user_url, json=preserve_previous_user_data)
#             response_get = session.get(user_url)
#             # print(f"ℹ️ {session.get(base_url).json()}")
        
        
    