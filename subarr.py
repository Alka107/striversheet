def issum(arr,sum):
    for i in range(len(arr)):
        curr_sum=0
        for j in range(i,len(arr)):
            curr_sum +=arr[j]
            if curr_sum==sum:
                return True
    return False
a=issum([5,8,6,13,3,1],22)
print(a)