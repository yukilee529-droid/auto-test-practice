def test_get_user(api_client):
    assert api_client['Authorization'].startswith('Bearer')

def test_env(env):
    print("\n[api用例] 拿到的 env =",env)
    assert env == 'dev'