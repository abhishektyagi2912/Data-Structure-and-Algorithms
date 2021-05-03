def candies(n, arr):
    candies = [1] * len(arr)
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            candies[i+1] = max(candies[i+1], candies[i] + 1)
    for i in reversed(range(1, len(arr))):
        if arr[i] < arr[i-1]:
            candies[i-1] = max(candies[i-1], candies[i] + 1)
    return sum(candies)
