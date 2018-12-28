import pytest

@pytest.yield_fixture()
def setup():
    print('Before setup')
    yield
    print('after setup')


def test_demo2_method1(setup):
    print('Method 1 status')


def test_demo2_method2(setup):
    print('Method 2 status')
