"""
MP3 Player因为屏幕较小，显示歌曲列表的时候每屏只能显示几首歌曲，用户要通过上下键才能浏览所有的歌曲。为了简化处理，假设每屏只能显示4首歌曲，光标初始的位置为第1首歌。

现在要实现通过上下键控制光标移动来浏览歌曲列表，控制逻辑如下：

歌曲总数<=4的时候，不需要翻页，只是挪动光标位置。

光标在第一首歌曲上时，按Up键光标挪到最后一首歌曲；光标在最后一首歌曲时，按Down键光标挪到第一首歌曲。
"""
"""
输入说明：
1 输入歌曲数量
2 输入命令 U或者D
输出说明
1 输出当前列表
2 输出当前选中歌曲
输入例子：
10
UUUU
预期输出：
7 8 9 10 
7
"""
def fun1(n, step):
    res = 1
    for k in range(n):
        print(k + 1, end=' ')
    print('')
    for k in step:
        if k == 'U' and res == 1:
            res = n
        elif k == 'D' and res == n:
            res = 1
        elif k == 'U' and res != 1:
            res -= 1
        elif k == 'D' and res != n:
            res += 1
    print(res)


def fun2(n, step):
    res = 1
    lis = [1, 2, 3, 4]
    for k in step:
        if k == 'U' and res == 1:
            res = n
            lis = [n - 3, n - 2, n - 1, n]
        elif k == 'D' and res == n:
            res = 1
            lis = [1, 2, 3, 4]
        elif k == 'U' and res == lis[0]:
            res -= 1
            for k in range(4):
                lis[k] -= 1
        elif k == 'D' and res == lis[3]:
            res += 1
            for k in range(4):
                lis[k] += 1
        elif k == 'U':
            res -= 1
        elif k == 'D':
            res += 1
    for k in lis:
        print(k, end=' ')
    print('')
    print(res)


def main():
    num = int(input())
    step = input()
    if num <= 4:
        fun1(num, step)
    else:
        fun2(num, step)


main()