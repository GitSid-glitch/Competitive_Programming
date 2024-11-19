t=int(input())
tu=[list(map(int,input().split())) for i in range(t)]
x={}   #count x
y={}    #count y
for j,k in tu: 
    if j in x:
        x[j]+=1
    else:
        x[j]=1
    if k in y:
        y[k]+=1
    else:
        y[k]=1

tr=0
for f,g in tu:
    tr+=(x[f]-1)*(y[g]-1)
print(tr)