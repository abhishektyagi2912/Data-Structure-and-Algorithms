# Approach:
# Main observation, The least difference between the numbers, the higer the value after modulo
# eg:
#  -1%7=6
#  -2%7=5
#  and so on so we have to minimize the difference between them. 
 # 	The main problem in the question was to find just greater number than our prefixSum. For that we used bisect, 
# 	bisect_right tell you if their is any greater element than our current element. 

# formula used is:

import bisect
t=int(input())
for _ in range(t):
	n,m=map(int,input().split())
	l=list(map(int,input().split()))
	maxi=0
	prefixSum=0
	SortedPrefix=[]
	for i in range(n):
		prefixSum=(prefixSum+l[i])%m 
		maxi=max(maxi,prefixSum) 
		index=bisect.bisect_right(SortedPrefix,prefixSum) 
		if index<len(SortedPrefix): 
			maxi=max(maxi,(prefixSum-SortedPrefix[index]+m)%m)

		bisect.insort(SortedPrefix,prefixSum) 

	print(maxi)
