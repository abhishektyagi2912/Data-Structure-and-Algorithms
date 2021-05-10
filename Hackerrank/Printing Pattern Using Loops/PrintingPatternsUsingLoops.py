# Algorithm: 
#   This pattern is an observational one. For eg, if n = 3
#       3 3 3 3 3
#       3 2 2 2 3
#       3 2 1 2 3
#       3 2 2 2 3
#       3 3 3 3 3
#   The no. of columns and rows are equal to (2 * n - 1).
#   The first (n - 1) and last (n - 1) rows can easily be printed using nested for loops
#   The middle row can be implemented using a single for loop


n = int(input())

for i in range(1 , n):
    temp = n
    for j in range(1 , n):
        if(j <= i and j != 1):
            temp -= 1
        print(temp , end = " ")
    print(temp , end = " ")
    for j in range(1 , n):
        if(j >= n - i + 1):
            temp += 1
        print(temp , end = " ")
    print("")

temp = n
for i in range(1 , n):
    print(temp , end = " ")
    temp -= 1

print("1" , end = " ")

for i in range(1 , n):
    temp += 1
    print(temp , end = " ")
print("")

m = 1
for i in range(n - 1 , 0 , -1):
    temp = n
    for j in range(1 , n):
        if(j <= i and j != 1):
            temp -= 1
        print(temp , end = " ")
    print(temp , end = " ")
    for j in range(1 , n):
        if(j >= m + 1):
            temp += 1
        print(temp , end = " ")
    print("")
    m += 1
