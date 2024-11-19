'''t=int(input())
results=[]
for i in range(t):
    s1=input().strip()
    s2=input().strip()
    a=len(s1)  #len(s1(n))
    r=s2[::-1]
    b=len(r)   #len(reverse of s2(m))
    l=[[0]*(b+1) for i in range(a+1)]
    for j in range(1, a+1):
        for k in range(1, b+1):
            if s1[j-1]==r[k-1]:
                l[j][k]=l[j-1][k-1]+1
            else:
                max(l[j-1][k],l[j][k-1])

    results.append(l[a][b])

for result in results:
    print(result)
'''
t=int(input())
results=[]
for i in range(t):
    s1=input().strip()
    s2=input().strip()
    c_s1={}     #count s1
    c_s2={}     #count s2
    for j in s1:
        if j in c_s1:
            c_s1[j]+=1
        else:
            c_s1[j]=1

    for j in s2:
        if j in c_s2:
            c_s2[j]+=1
        else:
            c_s2[j]=1

    m=0     #max palindromic count
    for j in s1:
        if j in s2:
            m=max(m,2*min(c_s1[j],c_s2[j]+1))
    results.append(m)

for k in results:
    print(k)
