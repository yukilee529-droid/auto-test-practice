import pytest


@pytest.mark.parametrize('score,expected', [(59, "不及格"),
                                            (60, "及格"),
                                            (90, "及格"),
                                            (0, "不及格")], ids=["差1分", "刚好60", "高分", "零分"])
def test_grade(score, expected):
    grade = '及格' if score >= 60 else '不及格'
    assert grade == expected


@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', [10, 20])
def test_combo(x, y):
    print(f'x={x}, y={y}, 和={x + y}')
    assert x + y in (11, 12, 21, 22)
