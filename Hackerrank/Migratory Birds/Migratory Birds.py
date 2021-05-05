from collections import Counter


def migratoryBirds(arr):
    m=[]
    c = dict(Counter(arr))
    for i in c.items():
        #when 2 or more values are common 
        if i[1]==max(c.values()):
            m.append(i[0])
     #retrieve smallest id number 
    return min(m)


if __name__ == '__main__':
    #Input List 
    arr_count = int(input().strip())
    arr = list(map(int, input().split(' ')))
    result = migratoryBirds(arr)
    print(result)
