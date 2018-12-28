import pytest

@pytest.yield_fixture()
def setup():
    print('Before Method')
    yield
    print('Tear down after method')


def test_demo3_method1(setup):
    print('Method 2 excuted')


def test_demo3_method2(setup):
    print('Method 2 Executed')