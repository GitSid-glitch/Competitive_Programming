t=int(input())
for i in range(t):
    n=int(input())
    students=[]
    for j in range(n):
        s=tuple(map(int,input().split()))
        students.append(s)
    final=[]
    x=0
    for l,r in students:
        x=max(x,l)
        if x>r:
            final.append(0)
        else:
            final.append(x)
            x+=1
    print(*final)
