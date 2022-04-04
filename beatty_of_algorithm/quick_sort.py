"""
    quick sort algorium
"""
import random


class sort_algo():
    def __init__(self, n):
        self.data_lis = self.data_generater(n)

    def data_generater(self, n):
        return [random.randint(1, 100) for k in range(n)]

    def quick_sort(self, lis):
        length = len(lis)
        if length == 0:
            return []
        elif length == 1:
            return lis
        else:
            lis1, lis2 = [], []
            povit = lis.pop(-1)
            for k in lis:
                if povit >= k:
                    lis1.append(k)
                else:
                    lis2.append(k)
            res = self.quick_sort(lis1)
            res.append(povit)
            return res + self.quick_sort(lis2)

    def python_sort(self, lis):
        lis.sort()
        return lis


def main():
    quick_sort = sort_algo(800)
    data_lis = quick_sort.data_lis[:]
    print('data_lis:', data_lis)
    print("python_sort_list:", quick_sort.python_sort(data_lis))
    print("quick_sorted_lis:", quick_sort.quick_sort(data_lis))


if __name__ == '__main__':
    main()
