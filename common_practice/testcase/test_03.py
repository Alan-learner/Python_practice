from common_practice.aw_libs.api_key import Key

import unittest
from ddt import ddt, data, unpack, file_data

"""
    使用文件格式分离测试数据，使代码结构更加优化、复用率提高
"""


# 装置器，数据驱动模块


@ddt()
class case3(unittest.TestCase):
    @file_data('./data.yaml')
    # 报错逻辑：出现exception情况，或者断言逻辑错误
    def assignment(self, kwargs):
        for key, value in kwargs.items():
            # value为字典
            if type(value) == dict:
                self.assignment(value)
            # value有具体值
            if value:
                pass
            # value为空
            else:
                kwargs[key] = getattr(self, key)
        return kwargs

    def test_03_(self, exp, rep):
        # 准备数据
        key = Key()
        url = 'http://www.bilibili.com'
        data = {
            'username': 'admin',
            'password': '123'
        }
        # 模拟请求
        res = key.do_post(url=url)
        # 获取响应并断言处理
        rel = key.get_value('"font-weight":"res.text"', 'font-weight')
        print(exp)
        final = key.assert_text(res.status_code, exp)
        self.assertTrue(final, rep)


if __name__ == '__main__':
    unittest.main()
