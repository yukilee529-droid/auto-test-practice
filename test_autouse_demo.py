import pytest


@pytest.fixture(autouse=True)
def clean_env():
    print('[自动] 每个用例前：清理环境')
    yield
    print('[自动] 每个用例后：还原环境')
def test_a():
    print('用例 A 执行中（参数表里没有 clean_env）')
    assert  1==1
def test_b():
    print("用例 B 执行中（参数表里也没有）")
    assert 2 == 2