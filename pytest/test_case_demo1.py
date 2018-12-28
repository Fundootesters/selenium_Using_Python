"""
Notes:
    1. .py file name should be start with test_ for eg. test_login.py
    2. method name should also start with '_' for eg. test_method_entercreds

PyTest Naming Conventions
When using pytest, it is very important to follow naming
conventions.
If we don't follow naming conventions, then pytest will not pick
up tests from the file.
• File names should start or end with “test”, as in
test_example.py or example_test.py
• Class name should start with “Test”, as in TestExample
• Test method names should start with “test_”, as in
test_example

"""

import pytest


@pytest.fixture()
def setup():
    print("Running demo1 setUp")


def test_demo1_method1(setup):
    print("Running demo1 method A")


def test_demo1_method2(setup):
    print("Running demo1 method B")