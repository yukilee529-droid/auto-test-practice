import pytest


@pytest.fixture
def sample_data():
    print("fixture 被调用了一次")
    data = {'user': 'tester', 'age': 18}
    return data


def test_user_name(sample_data):
    print(type(sample_data))
    print(sample_data)
    assert sample_data['user'] == 'tester'


def test_user_age(sample_data):
    assert sample_data['age'] == 18
