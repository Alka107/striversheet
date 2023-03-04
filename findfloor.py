def findFloor(A,N,X):
    low=0
    high=N-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if A[mid]==X:
            return mid
        elif A[mid]>X:
            high=mid-1
        else:
            ans=mid
            low=mid+1
    return ans

a=findFloor([1,2,8,10,11,12,19],7,0)
print(a)