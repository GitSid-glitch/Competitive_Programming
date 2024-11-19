def takecards(n, k, c):
    c_count = {}
    for i in c:
        if i in c_count:
            c_count[i] += 1
        else:
            c_count[i] = 1
    
    u = sorted(c_count.keys())
    
    m = 0
    cg = 0  
    left = 0  
    
    for j in range(len(u)):
        if j > 0 and u[j] > u[j - 1] + 1:
            while left < j:
                cg -= c_count[u[left]]
                left += 1
        
        cg += c_count[u[j]]
        
        while j - left + 1 > k:
            cg -= c_count[u[left]]
            left += 1
        
        m = max(m, cg)
    
    return m

t = int(input())  
for _ in range(t):
    n, k = map(int, input().split())  
    c = list(map(int, input().split()))  
    print(takecards(n, k, c))
