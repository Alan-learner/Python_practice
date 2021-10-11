class Solution:
    def magicalString(self, n: int) -> int:
        a = [1, 2, 2]
        if n == 0:
            return 0
        if n < 4:
            return 1

        p = 2
        q = 2
        while q < n - 1:
            if a[p] == 2:
                a.extend([1, 1] if a[q] == 2 else [2, 2])
                p += 1
                q += 2
            else:
                a.append(1 if a[q] == 2 else 2)
                p += 1
                q += 1

        return a.count(1) - 1 if len(a) != n and a[n] == 1 else a.count(1)