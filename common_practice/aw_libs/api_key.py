"""
    接口的关键字驱动封装类
"""
import json

import jsonpath

import requests


class Key():

    # get方法，不传则为None,传了则覆盖为所传参数
    def do_get(self, url, params=None, headers=None, **kwargs):
        return requests.get(url=url, params=params, headers=headers, kwargs=kwargs)

    # post方法
    def do_post(self, url, **kwargs):
        return requests.post(url=url, **kwargs)

    # 断言方法封装
    def assert_text(self, reality, expect):
        try:
            assert reality == expect
            return True
        except Exception as e:
            print(e)
            print('实际与预期不符，实际：{}，预期：{}'.format(reality, expect))
            return False

    # 获取键值对应方法
    def get_value(self, res, key):
        try:
            txt = json.loads(res)
            value = jsonpath.jsonpath(txt, '$..{}'.format(key))  # 返回list类型
            if value:
                if len(value) == 1:
                    return value[0]
                else:
                    return value
            else:
                return value
        except:
            return None

