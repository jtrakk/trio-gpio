import inspect
import pytest
from trio.testing import trio_test

@pytest.fixture
async def foo():
    yield "bar"

@pytest.hookimpl(tryfirst=True)
def pytest_pyfunc_call(pyfuncitem):
    if inspect.iscoroutinefunction(pyfuncitem.obj):
        pyfuncitem.obj = trio_test(pyfuncitem.obj)
