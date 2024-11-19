t=int(input())  

for _ in range(t):
    n=int(input())  
    a=list(map(int,input().split()))  
    
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    s=0
    for c in d.values():
        s+=c // 2

    print(s) 


'''t = int(input())  
for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))  
    f = [0] * (n + 1)  

    for i in a:
        f[i] += 1

    c=0
    for i in range(1,n + 1):
        c+=f[i]//2

    print(c)  
'''