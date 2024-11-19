t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    r=input()
    stack=[]
    x=0
    
    for j in s:
        stack.append(j)
        while len(stack)>=2 and stack[-2]!=stack[-1]and x<len(r):
            sub=r[x]
            stack.pop()
            stack.pop()
            stack.append(sub)
            x+=1
    
    if len(stack)==1:
        print("YES")
    else:
        print("NO")
 