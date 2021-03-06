import math
import os
import random
import re
import sys

def fibonacciModified(t1, t2, n):
    dp =[0]*(n)

    dp[0]= t1
    dp[1]= t2

    for i in range(2, n, 1):
        dp[i]= dp[i-1]**2 + dp[i-2]
    
    return dp[n-1]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = raw_input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
