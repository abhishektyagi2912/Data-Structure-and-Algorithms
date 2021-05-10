import math
import os
import random
import re
import sys

def plusMinus(arr):
    l=len(arr)
    cn=0  
    cp=0  
    cz=0 
    for i in arr:
        if i<0:    
            cn+=1
        elif i>0:   
            cp+=1
        else:
            cz+=1
        
    p=cp/l
    n=cn/l
    z=cz/l
    print(format(p,".6f"))  
    print(format(n,".6f"))  
    print(format(z,".6f"))
            
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
