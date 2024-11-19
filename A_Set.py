import sys


import sys
import math
import sys

input=sys.stdin.read
data=input().split()

t=int(data[0])
idx=1
x=[]
for i in range(t):
    l=int(data[idx])
    r=int(data[idx+1])
    k=int(data[idx+2])
    idx+=3
    
    largest=r//k
    if largest>=l:
        c=largest-l+1
    else:
        c=0
    x.append(str(c))

print("\n".join(x))

