def ispair(arr, x):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] ==x:
                return True
    return False

a=ispair([3,2,8,15,-8], 17)
print(a)