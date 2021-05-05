

n, k = map(int, input().split())
prices = list(sorted(map(int, input().split())))
toys = 0

for price in prices:
    if price <= k:
        k -= price
        toys += 1
    else:
        break

print(toys)

"""
Sample Input/Output:
Example 1:
Input:
7 50
1 12 5 111 200 1000 10
Output:
4



"""

