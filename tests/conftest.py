import pytest


@pytest.fixture(scope='session')
def login_token():
    print('\n[顶层conftest] 登录拿token，整个会话只执行1次')
    return 'abc123-token'

@pytest.fixture()
def env():
    return 'prod'