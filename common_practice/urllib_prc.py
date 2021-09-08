import urllib.request



# response = urllib.request.urlopen('http://www.baidu.com')  # 直接使用URLopen读取
# txt1 = response.read().decode('utf-8')   # 直接使用URLopen读取
# # print(txt1)

request = urllib.request.Request('http://www.baidu.com')    # 使用request读取
response2 = urllib.request.urlopen(request)
txt2 = response2.read().decode('utf-8')
print(txt2)
print('--'*20)
print(response2.status)
print('--'*20)
print(response2.getcode)
print('--'*20)
print(response2.reason)
print('--'*20)
print(response2.headers)
print('--'*20)