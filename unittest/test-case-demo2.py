import unittest


class TestCaseDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*********before class**********", end="")

    def setUp(self):
        print("I will run once before every testdemo")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every testdemo")

    @classmethod
    def tearDownClass(cls):
        print('*************after class*********')


if __name__ == '__main__':
    unittest.main(verbosity=2)
