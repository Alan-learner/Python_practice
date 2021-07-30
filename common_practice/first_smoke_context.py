import unittest


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        print('Alan is handsome')

    def tearDown(self) -> None:
        print('that is right')

    def test_case_01(self):
        print('really_1?')

    def test_case_02(self):
        print('really_2?')

    def test_case_03(self):
        print('really_3?')

    def test_case_04(self):
        print('really_4?')


if __name__ == '__main__':
    # unittest.main()
    smoke_test = unittest.TestSuite()
    smoke_test.addTests([TestCases('test_case_01'), TestCases('test_case_03')])
    unittest.TextTestRunner().run(smoke_test)