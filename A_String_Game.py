t=input()
p=input()
a=list(map(int,input().split()))
l=list(t)
k=list(p)
c=0
for i in a:
    l[i-1]=0
    c+=1
    if ', '.join(map(str, k)) not in ', '.join(map(str, l)):
        break
print(c)