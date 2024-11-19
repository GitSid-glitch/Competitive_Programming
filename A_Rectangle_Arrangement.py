def r_arrange(n):
    
    mw,mh=0,0
    
    for i in range(n):
        w,h=map(int,input().split())
        mw=max(mw, w)
        mh=max(mh, h)
    
    print(2*(mw + mh))


t=int(input())
for i in range(t):
    n=int(input())
    r_arrange(n)