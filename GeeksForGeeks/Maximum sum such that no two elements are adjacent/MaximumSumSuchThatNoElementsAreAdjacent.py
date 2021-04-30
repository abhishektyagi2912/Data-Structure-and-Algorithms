
arr = [5, 5, 10, 100, 10, 5] 

sumOdd = 0
sumEven = 0

for i in arr:
    if sumEven>sumOdd:
        ele = sumEven  
    else: 
        ele = sumOdd 
    sumOdd = sumEven + i 
    sumEven = ele 

if sumEven>sumOdd:
    print(sumEven)
else:
    print(sumOdd)
