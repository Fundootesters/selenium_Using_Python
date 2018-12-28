import pytest


@pytest.yield_fixture()
def setup():
    print('Running setup before method')
    yield
    print('Running setup after method')
