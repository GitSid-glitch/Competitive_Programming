q = int(input())  
for _ in range(q):
    s = input()
    t = input()
    x=0
    l=min(len(s),len(t))
    for i in range(l):
        if s[i]==t[i]:
            x+=1
        else:
            break
    if x>0:
        print(len(s)+len(t)-x+1)
    else:
        print(len(s)+len(t))

