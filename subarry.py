def maxLen( n, arr):
    mydict=dict()
    sum=0
    maxlen=0
    for i in range(n):
        sum+=arr[i]
        
        if sum==0:
            maxlen=i+1
        elif sum in mydict:
            maxlen=max(maxlen, i-mydict[sum])
        else:
            mydict[sum]=i
    return maxlen
a=maxLen(8,[15,-2,2,-8,1,7,10,23])
print(a)