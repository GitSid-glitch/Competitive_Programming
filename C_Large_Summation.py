'''t=int(input())
mod=10**9+7
for i in range(t):
    n=int(input())  
    ar=list(map(int, input().split())) 

    m=max(ar)

    if ar.count(m)==n:
        next_m=m
    else:
        l=[]
        for x in ar:
            if x!=m:
                l.append(x)
        next_m=max(l)  

    for x in ar:
        if x!=m:
            max_sum=(x+m)%mod
        else:
            max_sum=(x+next_m)%mod
        print(max_sum, end=" ")

    print()'''



'''import sys

input=sys.stdin.read
output=sys.stdout.write

mod=10**9+7

def solve():
    d=input().split()
    idx=0
    t=int(d[idx])
    idx+=1
    r=[]
    
    for i in range(t):
        n=int(d[idx])
        idx+=1
        ar=list(map(int, d[idx:idx + n]))
        idx+=n
        
        m=max(ar)
        
        if ar.count(m)==n:
            next_m=m
        else:
            l=[]
            for x in ar:
                if x!=m:
                    l.append(x)
            next_m=max(l)
        
        for x in ar:
            if x!=m:
                max_sum=(x+m)%mod
            else:
                max_sum=(x+next_m)%mod
            r.append(str(max_sum)+" ")
        
        r.append("\n")
    
    output("".join(r))

solve()'''


'''import sys

mod=10**9+7

def solve():
    input=sys.stdin.read
    data=input().split()
    
    idx=0
    T=int(data[idx])
    idx+=1
    results=[]
    
    for _ in range(T):
        n=int(data[idx])
        idx+=1
        arr=list(map(int, data[idx:idx+n]))
        idx+=n
        
        max_val=-1
        second_max_val=-1
        
        for num in arr:
            if num>max_val:
                second_max_val=max_val
                max_val=num
            elif num>second_max_val:
                second_max_val=num
        
        r=[]
        for num in arr:
            if num==max_val:
                r.append((num+second_max_val)%mod)
            else:
                r.append((num+max_val)%mod)
        
        results.append(" ".join(map(str,r)))
    
    sys.stdout.write("\n".join(results)+"\n")

solve()'''
















