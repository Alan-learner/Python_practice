"""
    给出一个名字，该名字有26个字符组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。

给出多个名字，计算每个名字最大可能的“漂亮度”。
"""


def main():
    name = input()
    dic = dict()
    for k in name:
        dic[k] = dic.get(k, 0) + 1
    sum = 0
    items = list(dic.items())
    items.sort(key=lambda x: x[1], reverse=True)
    num = 26
    for x, y in items:
        sum += y * num
        num -= 1
    print(sum)


if __name__ == '__main__':
    """
    input:
        2
        zhangsan
        lisi
    """
    n = int(input())
    """
    output:
        192
        101
    """
    while True:
        try:
            main()
        except Exception as e:
            break
