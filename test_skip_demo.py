import sys

import pytest


@pytest.mark.skip(reason='功能还没上线，先不跑')
def test_not_ready():
    assert False


@pytest.mark.skipif(sys.version_info < (3, 10), reason='需要 Python 3.10 以上')
def test_new_feature():
    assert 1 == 1


@pytest.mark.xfail(reason='已知 bug，等开发修')
def test_known_bug():
    assert 1 == 2


@pytest.mark.xfail(reason='bug 修好后要记得删标记', strict=True)
def test_bug_fixed_strict():
    assert 1 == 1
