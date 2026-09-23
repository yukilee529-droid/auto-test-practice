import pytest


@pytest.fixture(scope='module')
def api_client(login_token):
    return {"Authorization": f"Bearer {login_token}"}

@pytest.fixture
def env():
    return 'dev'