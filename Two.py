def twoSum(nums, target):
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d:
            return [d[r], i]
        d[j] = i
    
a=twoSum([3,2,4],6)
print(a)   