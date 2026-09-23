import pytest


@pytest.fixture
def db_conn():
    print('setup:连接数据库')
    conn = '打开的数据库连接'
    yield conn
    print('teardown：关闭数据库连接')

def test_query_user(db_conn):
    print('用力执行中，正在使用：',db_conn)
    assert db_conn == '打开的数据库连接'
    # assert db_conn == '错误的值'