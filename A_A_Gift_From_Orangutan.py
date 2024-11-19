'''from itertools import permutations

def score(a):
    n=len(a)
    max_sum=float('-inf')

    for p in permutations(a):
        b=[0]*n
        c =[0]*n

        b[0]=p[0]
        c[0]=p[0]

        for i in range(1,n):
            b[i]=min(b[i-1],p[i])
            c[i]=max(c[i-1],p[i])

        t = 0
        for i in range(n):
            t+=c[i]-b[i]
        if t > max_sum:
            max_sum=t

    return max_sum

t=int(input())

for i in range(t):
    n=int(input())  
    a=list(map(int, input().split()))  
    result = score(a)
    print(result)
'''




def score(a):
    a.sort()
    
    n=len(a)
    l=[]
    
    start=0        
    end=n-1   
    
    while start<=end:
        if start==end:
            l.append(a[end])
        else:
            l.append(a[end])
            l.append(a[start])
        start+=1
        end-=1
    
    b=[0]*n
    c=[0]*n

    b[0]=l[0]
    for i in range(1,n):
        b[i]=min(b[i-1],l[i])

    c[0]=l[0]
    for i in range(1,n):
        c[i]=max(c[i-1],l[i])

    t=sum(c[i]-b[i] for i in range(n))
    return t

t=int(input())
for i in range(t):
    n=int(input())  
    a=list(map(int, input().split()))  
    result = score(a)
    print(result)

