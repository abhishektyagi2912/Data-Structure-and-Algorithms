
import math
import os
import random
import re
import sys

def breakingRecords(scores):
    scores = list(scores)                      
    mi = scores[0]
    ma = scores[0]
    mic = 0
    mac = 0
    for i in scores:                           
        if i < mi:
            mi = i
            mic += 1
        if i > ma:
            ma = i
            mac += 1
    return (str(mac),str(mic))                 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))   

    result = breakingRecords(scores)                   

    fptr.write(' '.join(map(str, result)))              
    fptr.write('\n')

    fptr.close()
