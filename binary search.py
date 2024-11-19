'''arr=list(map(int,input().split()))
k=int(input())
l=0
flag=False
h=len(arr)-1
for i in range(len(arr)):
    mid=(l+h)//2
    if k==mid:
        print("Yes")
        break
    if k>mid:
        l==mid'''

arr=list(map(int,input().split()))
k=int(input())
l=0
h=len(arr)-1
while (l<=h):
    mid=(l+h)//2
    if k==mid:
        print("Yes")
        break
    elif k>mid:
        l=mid+1
    elif k<mid:
        h=mid-1
else :
    print("NO")

    
