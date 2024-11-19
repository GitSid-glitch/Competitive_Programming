def max_plate_area(n,m,a,b):
    a=[0]+sorted(a)+[n]
    b=[0]+sorted(b)+[m]



    horizontal_gap=0
    for i, j in zip(a,a[1:]):
        horizontal_gap=max(horizontal_gap, j - i)
    
    vertical_gap = 0
    for i, j in zip(b,b[1:]):
        vertical_gap=max(vertical_gap,j - i)
    
   
    return horizontal_gap*vertical_gap

n,m=map(int,input().split())  
x,y=map(int,input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
print(max_plate_area(n,m,a,b))  
