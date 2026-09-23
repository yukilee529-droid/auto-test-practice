import pytest


def is_adult(age):
    return age >= 18


@pytest.mark.parametrize('age,expected', [(17, False), (18, True), (30, True), (5, False)])
def test_is_adult(age,expected):
    print(f'年龄{age}，期望{expected}，实际{is_adult(age)}')
    assert is_adult(age) == expected

