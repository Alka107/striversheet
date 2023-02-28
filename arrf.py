def countFreq(arr):
 
    x=dict()
 
    
    for i in range(len(arr)):

        if arr[i] in x:
            x[arr[i]] += 1
        else:
            x[arr[i]] = 1
             
    return x
    # for t in x :
    #     print(t, " ", x[t])


a=countFreq([10, 20, 20, 10, 10, 20, 5, 20 ])
print(a)