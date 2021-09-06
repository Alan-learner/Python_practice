import unittest


class TestCases(unittest.TestCase):
    @classmethod    # 添加装饰器
    def setUpClass(cls) -> None:
        print('打开浏览器')
    #
    @classmethod
    def tearDownClass(cls) -> None:
        print('关闭浏览器')

    def setUp(self) -> None:
        print('Alan is handsome')
    #
    def tearDown(self) -> None:
        print('that is right')

    def test_case_01(self):
        print('really_1?')

    # def test_case_02(self):
    #     print('really_2?')
    #
    # def test_case_999(self):
    #     print('999')
    #
    def test_case_03(self):
        print('really_3?')
    #
    # def test_case_04(self):
    #     print('really_4?')


if __name__ == '__main__':
    unittest.main()
    # smoke_test = unittest.TestSuite()   # 创造测试套件实例对象
    # # 添加待测用例（冒烟）
    # smoke_test.addTests([TestCases('test_case_999'), TestCases('test_case_03')])
    # # 运行待测用例
    # run_tclist = unittest.TextTestRunner()
    # run_tclist.run(smoke_test)