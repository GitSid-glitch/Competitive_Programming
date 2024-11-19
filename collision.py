'''def c(r, b):
    c = 0
    for x, u in r:
        for y, v in b:
            if y * v == x * u:
                c += 1
    return c

r = [(1, 2)]
b = [(2,1)]
t = c(r, b)
print(t)
n,m=int(input())
for _ in range()'''



'''def c(r, b):
    c_c = {}

    for x, u in r:
        p = x * u
        if p in c_c:
            c_c[p] += 1
        else:
            c_c[p] = 1

    c = 0
    for y, v in b:
        p = y * v
        if p in c_c:
            c += c_c[p]

    return c
n, m = map(int, input().split())
r = [tuple(map(int, input().split())) for _ in range(n)]
b = [tuple(map(int, input().split())) for _ in range(m)]
result = c(r, b)
print(result)  '''

'''def c(r, b):
    c_c = {} 
    c = 0

    for x, u in r:
        for y, v in b:
            if u > 0 and v > 0:  
                t = x / v if u == v else y / u
                if t == x / u == y / v:  
                    p = (x, y)
                    
                    if p not in c_c or c_c[p] > t:
                        c_c[p] = t
                        c += 1  
    return c


n, m = map(int, input().split())
r = [tuple(map(int, input().split())) for _ in range(n)]
b = [tuple(map(int, input().split())) for _ in range(m)]
result = c(r, b)
print(result)  
'''

'''def c(r, b):
    r.sort()
    b.sort()

    c_d = {}
    c = 0

    i, j = 0, 0
    n, m = len(r), len(b)

    while i < n and j < m:
        x, u = r[i]
        y, v = b[j]

        if u > 0 and v > 0:
            t_r = x / u
            t_b = y / v

            if t_r == t_b:
                p = (x, y)
                t = t_r  

                if p not in c_d or c_d[p] > t:
                    c_d[p] = t
                    c += 1

        if u <= v:
            i += 1
        else:
            j += 1

    return c

n, m = map(int, input().split())
r = [tuple(map(int, input().split())) for _ in range(n)]
b = [tuple(map(int, input().split())) for _ in range(m)]
result = c(r, b)
print(result)
'''
'''def c(r, b):
    red_disappeared = set()
    blue_disappeared = set()
    c = 0

    for i, (x, u) in enumerate(r):
        for j, (y, v) in enumerate(b):
            if i in red_disappeared or j in blue_disappeared:
                continue
            
            red_time = x / v
            blue_time = y / u
            
            if red_time == blue_time:
                c += 1
                red_disappeared.add(i)
                blue_disappeared.add(j)

    return c

n, m = map(int, input().split())
r = [tuple(map(int, input().split())) for _ in range(n)]
b = [tuple(map(int, input().split())) for _ in range(m)]

result = c(r, b)
print(result)
'''


'''def c(r, b):
    map = {}
    c = 0

    for y, v in b:
        map[y * v] = True

    for x, u in r:
        if x * u in map:
            c += 1
            del map[x * u]

    return c

n, m = map(int, input().split())  
r = [tuple(map(int, input().split())) for _ in range(n)]  
b = [tuple(map(int, input().split())) for _ in range(m)]  

result = c(r, b)
print(result)'''

'''def c(r, b):
    # Dictionary to track potential collision ps
    mp = {}
    c = 0

    # Populate the map with ps for blue balls
    for y, v in b:
        p = y * v
        if p not in mp:
            mp[p] = []
        mp[p].append((y, v))

    # Check c for each red ball
    for x, u in r:
        p = x * u
        if p in mp:
            c += 1
            # Remove the entry to avoid multiple c with the same red ball
            del mp[p]

    return c

# Input reading
n, m = map(int, input().split())  
r = [tuple(map(int, input().split())) for _ in range(n)]  
b = [tuple(map(int, input().split())) for _ in range(m)]  

result = c(r, b)
print(result)
'''
'''from math import gcd
from collections import defaultdict

def c(r, b):
    # Dictionary to store the count of red balls by their collision ratio
    red_ratio_count = defaultdict(int)
    
    # Process each red ball and store its ratio in the dictionary
    for x, u in r:
        g = gcd(x, u)  # Reduce x/u to its simplest form
        ratio = (x // g, u // g)  # Store ratio as a tuple
        red_ratio_count[ratio] += 1

    c = 0
    
    # Process each blue ball and check for matching ratios in the red dictionary
    for y, v in b:
        g = gcd(y, v)  # Reduce y/v to its simplest form
        ratio = (y // g, v // g)  # Store ratio as a tuple
        if ratio in red_ratio_count:
            c += red_ratio_count[ratio]
            # Once counted, remove to avoid double counting with other blue balls
            del red_ratio_count[ratio]
    
    return c

# Input reading
n, m = map(int, input().split())
r = [tuple(map(int, input().split())) for _ in range(n)]
b = [tuple(map(int, input().split())) for _ in range(m)]

result = c(r, b)
print(result)


'''
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
