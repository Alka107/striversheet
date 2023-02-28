# import math
# def pickGifts(gifts, k):
#     #for i in range(1,len(gifts)):
#     x=max(gifts)
#     t=math.sqrt(x)
#     return t








# def removeDuplicates(nums):
#     nums=list(set(nums))
#     #t=x[:]
#     nums.sort()
#     return len(nums)

# def rotate(nums, k):
#     if len(nums)>k:

# nums=[1,2,3,4,5]    
# k=5
# k=k%len(nums)   
# print(k)
#     #k = k % len(nums)
#         nums[:] = nums[-k:] + nums[:-k]
#         return nums

# a=rotate([1,2] ,3)

# print(a)
# def searchMatrix(matrix, target):
#     n = len(matrix)//2
#     e = len(matrix[0])-1
#     low = 0
#     high = len(matrix)-1
#     flag = 0
#     while(low < high):
#         if matrix[n][e] == target:
#             return True
#         if matrix[n][e] > target:
#             high = n
#         elif matrix[n][e] < target:
#             low = n + 1
#         n = (low + high) // 2
#     for i in range(e+1):
#         if matrix[high][i] == target:
#             return True
#     return False

# a=searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)
# print(a)


