def work(nums_to_sort):
    if len(nums_to_sort) <= 1:
        return nums_to_sort
    n = max(nums_to_sort)
    nums = [0][:] * (n + 1)
    for i in nums_to_sort:
        nums[i] += 1
    res = []
    for i in range(len(nums)):
        for j in range(nums[i]):
            res.append(i)
    return res