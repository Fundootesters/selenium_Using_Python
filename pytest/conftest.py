import pytest

@pytest.yield_fixture()
def setup():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetUp():
    print("Running conftest demo one time setUp")
    yield
    print("Running conftest demo one time tearDown")