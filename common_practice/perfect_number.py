'''
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。

它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。

例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。s

输入n，请输出n以内(含n)完全数的个数。计算范围, 0 < n <= 500000
'''

def isperfect(x):
    total = 0
    for k in range(1, x):
        if x % k == 0:
            total += k
    if total == x:
        return True
    else:
        return False


def main():
    n = int(input())
    cnt = 0
    for k in range(1, n + 1):
        if isperfect(k):
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
