t= int(input())                             

for i in range(t):
    a = list(map(int, input().split()))     
    if a[2] < 41:                           
        print(a[0]*a[1]*a[2])
