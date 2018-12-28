import pytest

@pytest.mark.run(order=1)
def test_demo2_methodA(oneTimeSetUp, setup):
    print("Running conftest demo2 method A")


@pytest.mark.run(order=3)
def test_demo3_methodC(oneTimeSetUp, setup):
    print("Running conftest demo2 method C")



@pytest.mark.run(order=5)
def test_demo3_methodE(oneTimeSetUp, setup):
    print("Running conftest demo2 method E")


@pytest.mark.run(order=4)
def test_demo3_methodD(oneTimeSetUp, setup):
    print("Running conftest demo2 method D")


@pytest.mark.run(order=2)
def test_demo3_methodB(oneTimeSetUp, setup):
    print("Running conftest demo2 method B")