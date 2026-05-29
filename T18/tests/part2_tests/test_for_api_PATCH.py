import pytest
import requests

@pytest.fixture
def session_fixture():
    with requests.Session() as session:
        yield session
        

@pytest.fixture
def preserve_user(session_fixture: requests.Session, run_app):
    backuped_users = []
    base_url = run_app['url']    
    
    
    def backup_user(user_id):         
        user_url: str = base_url + "/" + str(user_id)       
        original_user = session_fixture.get(user_url)
        backuped_users.append(original_user.json())
        return user_url
    
    yield session_fixture, backup_user
    
    for user in backuped_users:
        response = session_fixture.post(base_url ,json=user)
        assert response.status_code == 200, "user was not restored"
    
    response_get = session.get(user_url)
    print(f"ℹ️ {response_get.json()}")
    

@pytest.mark.patch
@pytest.mark.parametrize("user_id, exp_sts",((1,200),))
def test_patch_t6(preserve_user,
                  user_id,
                  exp_sts):
    
    user_patch_update = {"name": "Patchers"}
    session, backup_user = preserve_user
    user_url = backup_user(user_id)
    
    response_get = session.get(user_url)
    print(f"ℹ️ {response_get.json()}")
    
    response_patch = session.patch(user_url, json=user_patch_update)
    assert response_patch.status_code == exp_sts, "user was not updated"
    