"""
    this stript calculates the max profit range from a serial of number in four ways
"""
import random
from time import time


class max_profit_compute:
    def __init__(self, n):
        self.data_amount = n
        self.data_list = self.generate_data(n)
        print(self.data_list)

    def generate_data(self, x):
        random.seed(11)
        data_list = []
        for k in range(x):
            num = round(random.uniform(-10.0, 10.0), 2)
            data_list.append(num)
        return data_list

    def merge(self, res1, res2):
        range1, max1 = res1[0], res1[1]
        range2, max2 = res2[0], res2[1]
        if range1[1] == range2[0]:
            if max1 * max2 > 0:
                return (range1[0], range2[1]), max1 + max2
            elif max1 >= max2:
                return range1, max1
            else:
                return range2, max2
        range3 = (range1[0], range2[1])
        max3 = max1 + max2 + sum(self.data_list[range1[1]:range2[0]])
        lis = [(range1, max1), (range2, max2), (range3, max3)]
        lis.sort(key=lambda item: item[1], reverse=True)
        return lis[0]

    def recursion(self, x, y):
        max_num = self.data_list[x]
        p, q = x, y
        if y - x == 1:
            max_num = self.data_list[x]
            p, q = x, y
            return (p, q), max_num
        elif y - x == 2:
            a, b = self.data_list[x], self.data_list[x + 1]
            if a * b >= 0:
                max_num = a + b
                p, q = x, y
            elif a < b:
                max_num = b
                p, q = y - 1, y
            else:
                max_num = a
                p, q = x, x + 1
            return (p, q), max_num
        else:
            center = (x + y) // 2
            res1, res2 = self.recursion(x, center), self.recursion(center, y)
            res = self.merge(res1, res2)
            p, q = res[0]
            max_num = res[1]
        return (p, q), max_num

    def algo1(self):
        # 遍历，暴力破解
        print('暴力破解算法：')
        start_time = time()
        res = {}
        for p in range(self.data_amount):
            for q in range(1, self.data_amount - p):
                total = sum(self.data_list[p:(p + q)])
                res[(p, p + q)] = total
        result = sorted(res.items(), key=lambda item: item[1], reverse=True)
        print('最大值区间为{},最大总和为{},用时:{:.3f}秒'.format(result[0][0], result[0][1], time() - start_time))

    def algo2(self):
        # 动态记录
        print('暴力算法改进：')
        start_time = time()
        max = self.data_list[0]
        x, y = 0, 0
        for p in range(self.data_amount):
            sum = self.data_list[p]
            for q in range(1, self.data_amount - p):
                sum += self.data_list[p + q]
                if sum > max:
                    max = sum
                    x, y = p, p + q + 1
        run_time = time() - start_time
        print('最大值区间为{},最大总和为{},用时:{:.6f}秒'.format((x, y), max, run_time))

    def algo3(self):
        # 分治、递归
        print('分治、递归算法：')
        start_time = time()
        range, max = self.recursion(0, self.data_amount)
        run_time = time() - start_time
        print('最大值区间为{},最大总和为{},用时:{:.8f}秒'.format(range, max, run_time))

    def algo4(self):
        # 正反遍历、动态规划
        start_time = time()
        print('正反遍历算法：')
        x, y = 0, self.data_amount
        max_num = self.data_list[0]
        sum1, sum2 = 0, 0
        cnt1, cnt2 = 1, self.data_amount - 1
        for k in self.data_list:
            sum1 += k
            if sum1 > max_num:
                y = cnt1
                max_num = sum1
            cnt1 += 1
        max_num = self.data_list[-1]
        for k in self.data_list[::-1]:
            sum2 += k
            if sum2 > max_num:
                x = cnt2
                max_num = sum2
            cnt2 -= 1
        range = (x, y)
        max = sum(self.data_list[x:y])
        run_time = time() - start_time
        print('最大值区间为{},最大总和为{},用时:{:9f}秒'.format(range, max, run_time))


def main(x):
    compute = max_profit_compute(x)
    compute.algo4()
    compute.algo3()
    compute.algo2()
    compute.algo1()


if __name__ == '__main__':
    main(10)
