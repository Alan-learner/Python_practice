import requests

"""
    接口测试，用request实现
"""
#   准备数据
url = 'url on your websit'

#   模拟请求
res = requests.post(url=url)
print(res.text)
print(res.status_code)
print(res)
#   获取响应并处理