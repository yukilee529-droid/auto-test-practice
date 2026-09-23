# 自动化测试实践（pytest）

## 项目简介

本仓库沉淀基于 **Python + pytest** 的自动化测试实践，覆盖用例组织、fixture 依赖注入、参数化、标记与跳过，并持续扩展接口自动化、UI 自动化与持续集成。

## 技术栈

- Python 3
- pytest（及 pytest-mock、pytest-xdist、pytest-cov 等插件）
- Allure 测试报告
- Git / GitHub 版本管理

## 目录结构

```text
.
├── pytest.ini              # pytest 配置：默认参数、自定义标记
├── test_*.py               # 各类测试用例
├── mytests/                # conftest + 用例（依赖注入实践）
└── tests/
    ├── conftest.py
    ├── test_login.py
    └── api/                # 接口用例（持续完善）
```

## 测试实践覆盖

- 用例组织与 `assert` 断言
- fixture 依赖注入、`yield` 前置/后置清理
- fixture 作用域：function / class / module / session
- `conftest.py` 共享 fixture
- 参数化：`@pytest.mark.parametrize` 与 `fixture(params=...)`
- 标记 mark 与按标记筛选（`-m`）
- 跳过 `skip` / `skipif`、预期失败 `xfail`

## 如何运行

```bash
pip install pytest

python3 -m pytest -v            # 运行全部用例
python3 -m pytest -m smoke -v   # 只跑 smoke 标记用例
```

## 扩展方向

- 接口自动化：requests + pytest + Allure
- UI 自动化：Playwright
- 持续集成：GitHub Actions / Jenkins
- 性能测试：JMeter
