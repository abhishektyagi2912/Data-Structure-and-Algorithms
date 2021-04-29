

string = input("Enter string: ")                  

ocurance = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]          

for c in string:                                   
    o = ord(c)
    if o > 47 and o < 58:
        ocurance[o-48] += 1

for i in ocurance:                                 
    print(i, end=" ")
print()                                         
