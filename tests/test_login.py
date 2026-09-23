def test_token(login_token):
    assert login_token.startswith('abc')