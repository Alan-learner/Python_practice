import requests

"""
    接口测试，用request实现
"""
#   准备数据
url = 'http://www.baidu.com'

#   模拟请求
res = requests.post(url=url)
print(res.text)
print(res.status_code)
print(res)
#   获取响应并处理(断言)
status_code = 302
assert status_code == res.status_code, 'failed for some reasons'
