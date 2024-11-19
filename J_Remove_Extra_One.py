n=int(input())
p=list(map(int, input().split()))

prefix_sum_max=[0]*n
prefix_sum_max[0]=p[0]
for i in range(1,n):
    prefix_sum_max[i]=max(prefix_sum_max[i-1],p[i])

ir = 1  
for i in range(1,n):
    if p[i]>prefix_sum_max[i-1]:
        ir+=1

maximum_records=ir
x=p[0]

for i in range(n):
    records=0
    current_max=0
    for j in range(n):
        if j==i:
            continue
        if p[j]>current_max:
            current_max=p[j]
            records+=1

    if records>maximum_records:
        maximum_records=records
        x=p[i]
    elif records==maximum_records and p[i]<x:
        x=p[i]

print(x)
