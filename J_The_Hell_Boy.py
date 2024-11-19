'''def sub(arr, n): 
    a=1; 
    for i in range(0,n): 
        a=a*(arr[i]+1) 
    return a-1
  
T=int(input())
for i in range(T):
    n=int(input())
    arr=list(map(int, input().split()))

    n=len(arr) 
  
    print(sub(arr, n))'''


import sys
mod=10**9+7
input=sys.stdin.read
output=sys.stdout.write

def sub(arr,n): 
    a=1
    for i in range(0,n): 
        a=a*(arr[i]+1) 
    return(a-1)%mod

data=input().split()  
T=int(data[0])  
idx=1  

result=[]
for i in range(T):
    n=int(data[idx])  
    arr=list(map(int,data[idx+1:idx+1+n]))  
    idx+=n+1  
    result.append(str(sub(arr,n)))  
output("\n".join(result)+"\n") 