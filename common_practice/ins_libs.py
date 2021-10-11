import os
libs = ['numpy', 'matplotlib', 'pillow', 'sklearn', 'requests',\
        'jieba','beautifulsoup4', 'wheel','networkx', 'sympy',\
        'pyinstaller', 'django', 'flask', 'werobot', 'pyqt5',\
        'pandas', 'pyopeng1', 'pypdf2', 'docopt', 'pygame']

cnt_sus = 0
cnt_fal = 0
for lib in libs:
    try:
        os.system('pip install '+ lib)
        print('sussessful')
        cnt_sus += 1
    except:
        print('failed,somehow')
        cnt_fal += 1

print('成功安装：', cnt_sus)
print('失败：', cnt_fal)
