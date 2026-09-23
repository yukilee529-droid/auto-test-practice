import pytest

@pytest.mark.parametrize('browser_name',['chrome','firefox'])
def test_by_parametrize(browser_name):
    print(browser_name)

@pytest.fixture(params=['chrome','firefox'])
def browser(request):
    name=request.param
    print(f'准备启动：{name}')
    driver =f'{name}浏览器对象'
    yield driver
    print(f'清理关闭{name}')

def test_by_fixture_params(browser):
    print(f'在{browser}上测试')