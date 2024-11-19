def pir(x):
    l=[]
    for a,b in x:
        if a>=b:
            l.append(a)  
        else:
            l.append(max(0,2*a-b))  
    return l

t=int(input())  
for i in range(t):
    x=[tuple(map(int, input().split()))]

    l=pir(x)
    for i in l:
        print(i)


'''t=int(input())  
for i in range(t):
    x=[tuple(map(int, input().split()))]
    l=[]
    for a,b in x:
        if a>=b:
            l.append(a)  
        else:
            l.append(max(0,2*a-b))  
    for i in l:
        print(i)
'''