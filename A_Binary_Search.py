n,k=map(int,input().split())
arr=list(map(int,input().split()))
q = [ int(i ) for i in input().split()]
for i in q:
    l=0
    h=n-1
    while (l<=h):
        mid=(l+h)//2
        if i==arr[mid]:
            print("YES")
            break
        elif i> arr[mid]:
            l=mid+1
        elif i<arr[mid]:
            h=mid-1
    else :
        print("NO")