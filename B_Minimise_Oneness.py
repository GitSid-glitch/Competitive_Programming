t=int(input())  
results=[]

for _ in range(t):
    n=int(input())  
    s=''.join('01'[(i % 2)] for i in range(n))
    results.append(s)

print('\n'.join(results))
