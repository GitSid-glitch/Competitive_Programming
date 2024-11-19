n=int(input())
l=[]
for i in range(2*n):
    s=input().split()
    if s[0]=="add":
        l.append((s[0],int(s[1])))
    else:
        l.append((s[0],None))

stack=[]
count_c=0
box=1

for i in l:
    if i[0]=="add":
        f,x=i
        stack.append(x)
    elif i[0]=="remove":
        if stack and stack[-1]==box:
            stack.pop()
        else:
            if stack:
                count_c+=1
                stack.clear()  
        box+=1
        
print(count_c)

