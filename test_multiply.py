def multiply(a, b):
    return a * b


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_negativ():
    assert multiply(-2, 5) == -10
