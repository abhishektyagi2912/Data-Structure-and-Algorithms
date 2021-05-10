lst=[]

s=""

q=int(input())

for i in range(q):
    inp=input()
    t=inp[0]
    w=inp[2:len(inp)]
    if t=="1":
        lst.append(s)
        s=s+w
    #To delete last n characters
    elif t=="2":
        lst.append(s)
        s=s[:-int(w)]
    #To print the nth character
    elif t=="3":
        print(s[int(w)-1])
    #To undo
    elif t=="4":
        s=lst.pop()
    else:
        pass
