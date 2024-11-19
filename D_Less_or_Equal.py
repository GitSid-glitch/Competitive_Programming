def less_equal(k,a):

    if k==0:
        if a[0] > 1:
            print(1)
        else:
            print(-1)
    elif k==n or a[k]>a[k-1]:
        print(a[k-1])
    else:
        print(-1)

n,k=map(int, input().split())
a=sorted(map(int, input().split()))
less_equal(k,a)
