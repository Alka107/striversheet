def jkhdd(arr):
    x=len(arr)
    t=set(arr)
    y=len(t)
    h=x-y
    return h
a=jkhdd([1,4,4,5])
print(a)