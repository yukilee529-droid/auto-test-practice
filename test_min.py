import pytest


@pytest.mark.parametrize('age', [17, 18, 30, 5])
def test_print_age(age):
    print('这次拿到的age是', age)
    assert age >= 0
