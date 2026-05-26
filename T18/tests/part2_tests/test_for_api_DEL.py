# import pytest
# import requests
#
# @pytest.mark.parametrize("user_id, exp_res",
#                          ((2, ""),
#                           (3, {"detail":"User not found"})))
# def test_4_delete_user(run_app, user_id, exp_res):
#     with requests.Session() as session:
#         response_get_user = session.get(f"{run_app['url']}/{user_id}")
#         if response_get_user.status_code == 200:  
#             try:     
#                 response_delete = session.delete(f"{run_app['url']}/{user_id}")
#                 assert response_delete.status_code == 204, "user was not deleted"
#                 assert response_delete.text == exp_res, "message body is not empty"
#                 response_get_deleted_user = session.get(f"{run_app['url']}/{user_id}")
#                 assert response_get_deleted_user.status_code == 404, "user was not deleted"                
#             finally:
#                 user_data = response_get_user.json()  
#                 response_post = session.post(run_app['url'], json=user_data)
#                 assert response_post.status_code == 201, "user was not created"
#                 response_get_user = session.get(f"{run_app['url']}/{user_id}")
#                 assert response_get_user.status_code == 200, "user was not stored"
#         else:
#             assert response_get_user.status_code == 404, "user supposed to not be found but it is"
#             assert response_get_user.json() == exp_res, "User is found but shouldn't"
# ######################################################################################################    
# 
# import pytest
# import requests
# 
# # --- Test 1: The Happy Path (Successful Deletion) ---
# @pytest.mark.parametrize("user_id", (2,))
# def test_delete_existing_user(run_app, user_id):
#     with requests.Session() as session:
#         user_url = f"{run_app['url']}/{user_id}"
        
#         # 1. Arrange: Ensure user exists and save data
#         response_get_user = session.get(user_url)
#         assert response_get_user.status_code == 200, f"Setup failed: User {user_id} not found"
#         user_data = response_get_user.json()
        
#         try:
#             # 2. Act: Delete the user
#             response_delete = session.delete(user_url)
            
#             # 3. Assert: Verify deletion
#             assert response_delete.status_code == 204, "User was not deleted"
#             assert response_delete.text == "", "Message body is not empty"
            
#             # Verify user is actually gone
#             response_get_deleted = session.get(user_url)
#             assert response_get_deleted.status_code == 404, "User still exists after deletion"
            
#         finally:
#             # 4. Cleanup: Restore the user
#             response_post = session.post(run_app['url'], json=user_data)
#             if response_post.status_code != 201:
#                 pytest.fail("Teardown failed: User was not recreated")


# # --- Test 2: The Sad Path (Deleting a Non-Existent User) ---
# @pytest.mark.parametrize("user_id, exp_res", (
#     (3, {"detail": "User not found"}),
# ))
# def test_delete_non_existent_user(run_app, user_id, exp_res):
#     with requests.Session() as session:
#         user_url = f"{run_app['url']}/{user_id}"
        
#         # 1. Arrange: Ensure user is definitely NOT there before we start
#         assert session.get(user_url).status_code == 404, f"Setup failed: User {user_id} exists but shouldn't"
        
#         # 2. Act: Attempt to delete the non-existent user
#         response_delete = session.delete(user_url)
        
#         # 3. Assert: Verify API handles the bad request correctly
#         # Assuming your API returns 404 on bad deletes. Adjust if it returns 400 or 204!
#         assert response_delete.status_code == 404, "Expected a 404 Not Found on deletion attempt"
#         assert response_delete.json() == exp_res, "Error message body did not match expected"
# ######################################################################################################   

import pytest
import requests

# --- 1. The Fixture (State Management) ---
# The core definition of a Factory pattern is that it handles the complex logic of creating something 
# (setting up state, building objects, fetching data) so the client (your test) doesn't have to.

@pytest.fixture
def preserve_user(run_app):
    """
    Saves a user's state before a test and restores it afterward.
    """
    session = requests.Session()
    users_to_restore = []

    # This inner function is what the test will actually call
    # Closure (a function returning another function).
    def _save_state(user_id):
        user_url = f"{run_app['url']}/{user_id}"
        response = session.get(user_url)
        
        # If the user exists, save their data for the teardown phase
        if response.status_code == 200:
            users_to_restore.append(response.json())
        elif response.status_code != 404:
            pytest.fail(f"Unexpected status {response.status_code} when looking up user {user_id}")
            
        return user_url

    # Pause the fixture and hand control over to the test
    yield _save_state

    # --- TEARDOWN PHASE ---
    # This runs automatically after the test finishes (pass or fail)
    for user_data in users_to_restore:
        restore_response = session.post(run_app['url'], json=user_data)
        if restore_response.status_code != 201:
            # Log or warn here. Pytest will report this as an error in the teardown phase.
            pytest.fail(f"Teardown failed: Could not restore user {user_data.get('id')}")
            
    session.close()


# --- 2. The Tests ---

@pytest.mark.parametrize("user_id", (2,))
def test_delete_existing_user(preserve_user, user_id):
    # 1. Arrange: Call the fixture to save the user state and get the URL
    user_url = preserve_user(user_id)
    # preserve_user is no longer the fixture itself. 
    # It has essentially become an alias for the _save_state function.
    # 
    # # 1. Pytest runs the fixture up to the yield
    # the_thing_that_was_yielded = _save_state 

    # # 2. Pytest passes that thing into your test using the fixture's name
    # preserve_user = the_thing_that_was_yielded 

    # # 3. Inside your test, you add parentheses to call it!
    # user_url = preserve_user(user_id) 

    # # Which is literally the exact same as calling:
    # user_url = _save_state(user_id)
    
    with requests.Session() as session:
        # Verify setup was successful
        assert session.get(user_url).status_code == 200, "Setup failed: User not found"
        
        # 2. Act
        response_delete = session.delete(user_url)
        
        # 3. Assert
        assert response_delete.status_code == 204, "User was not deleted"
        assert response_delete.text == "", "Message body is not empty"
        assert session.get(user_url).status_code == 404, "User still exists after deletion"

        # Notice there is no try/finally block here! 
        # Once the test finishes, the `preserve_user` fixture resumes and restores the user.


@pytest.mark.parametrize("user_id, exp_res", (
    (3, {"detail": "User not found"}),
))
def test_delete_non_existent_user(run_app, user_id, exp_res):
    # We don't need the preserve_user fixture here since the user doesn't exist
    with requests.Session() as session:
        user_url = f"{run_app['url']}/{user_id}"
        
        # 1. Arrange
        assert session.get(user_url).status_code == 404, "Setup failed: User exists but shouldn't"
        
        # 2. Act
        response_delete = session.delete(user_url)
        
        # 3. Assert
        assert response_delete.status_code == 404, "Expected a 404 Not Found"
        assert response_delete.json() == exp_res, "Error message did not match expected"