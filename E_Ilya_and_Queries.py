s=input().strip()
m=int(input().strip())

l=[0]*len(s)
for i in range(1,len(s)):
    l[i]=l[i-1]+(1 if s[i]==s[i-1] else 0)

for i in range(m):
    li,ri=map(int,input().split())
    print(l[ri-1]-l[li-1])
