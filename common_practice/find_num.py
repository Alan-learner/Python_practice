nums = [-1, 0, 3, 5, 9, 12]
target = 9
class Solution:
    def search(nums, target):
        lenth = len(nums)
        left, right = 0, lenth
        dist = lenth
        res = -1
        while dist > 2:
            mean = (right + left) // 2
            if nums[mean] == target:
                res = mean
                break
            elif nums[mean] < target:
                left = mean
            else:
                right = mean
            dist = right - left
        return res

result = Solution.search(nums, target)
print(result)