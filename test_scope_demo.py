import pytest


@pytest.fixture(scope="session")
def browser():
    print('session启动浏览器（整个会话只跑1次')
    yield '浏览器实例'
    print('session关闭浏览器（所有用例结束后跑1次')

@pytest.fixture(scope='function')
def page(browser):
    print('function新建页面')
    yield f'新页面 on {browser}'
    print('function关闭页面')

def test_a(page):
    print('用例A执行中')
    print("page 的值是：", page)
    assert '新页面' in page

def test_b(page):
    print('用例B执行中')
    assert '新页面' in page