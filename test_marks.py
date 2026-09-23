import pytest


@pytest.mark.smoke
def test_fast():
    assert 1==1

@pytest.mark.slow
def test_big():
    assert sum(range(100000)) == 4999950000