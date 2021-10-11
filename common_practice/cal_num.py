class clanum():
    def cla(self, x):
        cnt = 0
        for k in range(1, x + 1):
            y, z = str(k ** 2), len(str(k))
            num = int(y[-z:])
            if num == k:
                cnt += 1
        return cnt


def main():
    n = int(input())
    res = clanum().cla(n)
    print(res + 1)


if __name__ == '__main__':
    main()