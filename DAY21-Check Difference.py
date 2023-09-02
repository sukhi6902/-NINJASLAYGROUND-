def checkDiff(arr, N, K):
    # Write your code here.
    arr = sorted(arr)
    i = 0
    j = 1
    while j<N:
        d = arr[j]-arr[i]
        if d==K:
            return True
        elif d > K:
            i+=1
        else:
            j+=1
        
        if i==j:
            j+=1
    
    return False
