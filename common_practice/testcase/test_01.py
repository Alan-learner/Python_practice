from common_practice.aw_libs.api_key import Key

import unittest
from ddt import ddt, data, unpack


# 装置器，数据驱动模块


@ddt()
class case(unittest.TestCase):
    @data([200, 'successful'], [201, 'faile for some reason!'])
    @unpack
    # 报错逻辑：出现exception情况，或者断言逻辑错误
    def test_01_(self, exp,rep):
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
