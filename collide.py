from collections import Counter

def c(r, b):
    mp = Counter(y * v for y, v in b)
    c = 0

    for x, u in r:
        p = x * u
        if mp[p] > 0:
            c += 1
            mp[p] -= 1
            if mp[p] == 0:
                del mp[p]

    return c

n, m = map(int, input().split())  
r = [tuple(map(int, input().split())) for _ in range(n)]  
b = [tuple(map(int, input().split())) for _ in range(m)]  

result = c(r, b)
print(result)
