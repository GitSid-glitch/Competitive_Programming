t = int(input())
for _ in range(t):
    n=int(input())
    if n < 5:
        print(-1)
    else:
        q = 1
        while q < n + 1:
            if q != 5:
                print(q, end=" ")
            q += 2
        print(5,4,end=" ")
        
        q=2
        while q < n + 1:
            if q != 4:
                if q == n or q == n - 1:
                    print(q, end="\n")
                else:
                    print(q, end=" ")

            q += 2

