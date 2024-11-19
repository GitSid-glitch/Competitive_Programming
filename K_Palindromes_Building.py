import math
from collections import Counter
t=int(input())  
for i in range(t):
    n=int(input())  
    s=input()  
    f=Counter(s)
    o=0
    for i in f.values():  
        if i%2!=0:       
            o+=1       
    if o>1:
        print("0")
    else:
    
        hf=[]  
        for i in f.values():  
            i=i//2  
            hf.append(i)        
        midlength=sum(hf)  
        
        nu=math.factorial(midlength)
        du=1
        for i in hf:
            du*=math.factorial(i)
        
        print(nu//du)

