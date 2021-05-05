def maxSubsetSum(arr):
    
    n = len(arr) 
    dp = [0]*n   
    dp[0] = arr[0] 
    dp[1] = max(arr[1], dp[0]) 
    
    for i in range(2,n):
       # Therefore we can either take one and then skip one, or skip one and run the subroutine.
        dp[i] = max(arr[i], dp[i-1], arr[i] + dp[i-2])
    # in the dp, we store the max sum for the subarray up till the length of the subarray.
    #  Hence simply return the last item in this to get the answer
    return dp[-1]
