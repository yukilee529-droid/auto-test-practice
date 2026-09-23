import pytest


@pytest.fixture(params=['admin','guest','root'],ids=['管理员','访客','超管'])
def role(request):
    return request.param

def test_role(role):
    print('当前角色',role)
    assert role in ('admin','guest','root')