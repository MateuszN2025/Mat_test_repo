import pytest
import requests

@pytest.fixture
def session_fixture():
    with requests.Session() as session:
        yield session
        

@pytest.fixture
def preserve_user(session_fixture: requests.Session, run_app, user_id):
    backuped_users = []
    base_url = run_app['url']    
    user_url: str = base_url + "/" + str(user_id)
    
    def backup_user():                
        original_user = session_fixture.get(user_url)
        backuped_users.append(original_user.json())
        return backuped_users
    
    yield session_fixture, user_url, backup_user
    
    for user in backuped_users:
        response = session_fixture.post(base_url ,json=user)
        assert response.status_code == 200, "user was not restored"
    

@pytest.mark.patch
@pytest.mark.parametrize("user_id, exp_sts",((1,200),))
def test_patch_t6(preserve_user,
                  user_id,
                  exp_sts):
    
    user_patch_update = {"name": "Patchers"}
    session, user_url, backup_user = preserve_user
    
    response_patch = session.patch(user_url, json=user_patch_update)
    assert response_patch.status_code == 200, "user was not updated"
    response_patch = session.patch(user_url, json=user_patch_update)
    