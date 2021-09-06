"""
[多条件排序]
输入一个只包含小写英文字母和数字的字符串，
按照不同字符统计个数由多到少输出统计结果，
如果统计的个数相同，则按照ASCII码由小到大排序输出。
"""



def main():
    x = input()
    y = set(x)
    z = {}
    for k in y:
        z[k] = (x.count(k),ord(k))
    lis = list(z.items())
    lis.sort(key=lambda x:(x[1][0], -x[1][1]), reverse=True)
    for k in lis:
        a, b = k
        print(a, end='')


main()