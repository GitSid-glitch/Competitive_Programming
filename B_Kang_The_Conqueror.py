MOD=10**9 + 7

t=int(input())  

for i in range(t):
    n=int(input())  
    arr=list(map(int,input().split()))  
    
    arr.sort()
    
    result=0
    subset_2=1  
    
    for j in range(n):
        result=(result+arr[j]*subset_2)%MOD
        subset_2=(subset_2*2)%MOD  

    print(result)
