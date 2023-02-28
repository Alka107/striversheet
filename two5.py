def twoSum(nums, target):
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d:
            return [d[r], i]
        d[j] = i
    
a=twoSum([2,7,11,15],9)
print(a)