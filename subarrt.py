def subArraySum(arr, n, sum):
 
    
    for i in range(0,n):
        currentSum = arr[i]
        if(currentSum == sum):
            print("Sum found at indexes",i)
            return
        else:
            
            for j in range(i+1,n):
                currentSum += arr[i]
                if(currentSum == sum):
                    print("Sum found between indexes",i,"and",j)
                    return
    print("No Subarray Found")