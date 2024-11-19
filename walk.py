def walk(N, cities, A, B, P, Q, C, D, Y):
    x_a, x_b, x_c, x_d = cities[A-1], cities[B-1], cities[C-1], cities[D-1]
    
    d = abs(x_b - x_a)
    w = d * P
    
    if A == C and B == D:
        t = abs(x_c - x_a) * P
        
        if t <= Y:
            t_t = abs(x_d - x_c) * Q
            train_time = Y + t_t
            
            return min(w, train_time)
    
    return w

'''N = 4
cities = [1,2,3,4]
A, B = 1, 3
P, Q = 3, 2
C, D, Y = 2, 4, 14
print(walk(N, cities, A, B, P, Q, C, D, Y))'''
T=int(input())
for i in range(T):
    N, A, B, C, D, P, Q, Y=map(int,input().split())
    cities=list(map(int,input().split()))
    print(walk(N, cities, A, B, P, Q, C, D, Y))





'''N = 4
cities = [1,2,3,4]
A, B = 1, 3
P, Q = 3, 2
C, D, Y = 2, 4, 14
x_a, x_b, x_c, x_d = cities[A-1], cities[B-1], cities[C-1], cities[D-1]
    
d = abs(x_b - x_a)
w = d * P

if A == C and B == D:
    t = abs(x_c - x_a) * P
    
    if t <= Y:
        t_t = abs(x_d - x_c) * Q
        train_time = Y + t_t
        break

        
        print(min(w, train_time))
'''

