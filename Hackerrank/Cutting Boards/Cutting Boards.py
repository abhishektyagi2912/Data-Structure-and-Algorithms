
t=int(input())
for i in range(t):
    row,column = list(map(int,input().split()))
    xa= list(map(int,input().split()))
    ya= list(map(int,input().split()))
    xa.sort()
    ya.sort()
    xarr=xa[::-1]
    yarr=ya[::-1]
    pivot_x=0
    pivot_y=0
    cost=0
    cutedge_x=1
    cutedge_y=1
    while pivot_x<row-1 and pivot_y<column-1:
        if xarr[pivot_x]>yarr[pivot_y]:   
            cost+=cutedge_y*xarr[pivot_x]
            cutedge_x+=1
            pivot_x+=1
        else:
            cost+=cutedge_x*yarr[pivot_y]      
            cutedge_y+=1
            pivot_y+=1
    while pivot_x>=row-1 and pivot_y<column-1:   
        cost+=cutedge_x*yarr[pivot_y]
        cutedge_y+=1
        pivot_y+=1
    while pivot_x<row-1 and pivot_y>=column-1:   
        cost+=cutedge_y*xarr[pivot_x]
        cutedge_x+=1
        pivot_x+=1
    print(cost%1000000007)
