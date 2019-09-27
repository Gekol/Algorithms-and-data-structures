def work(nums):
    if len(nums) <= 1:
        return nums
    n = max(nums)
    d = len(str(n))
    extent_10 = 1
    res = []
    for i in range(d):
        for j in range(10):
            for k in nums:
                current_radix = (k // extent_10) % 10
                if current_radix == j:
                    res.append(k)
        extent_10 *= 10
        nums = res[:]
        res = []
    return nums

print(work([3, 2, 12, 54, 35, 76, 89, 71, 17]))