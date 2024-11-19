def max_possible_value(t, test_):
    res = []
    for i in range(t):
        n = test_[i][0]
        a = sorted(test_[i][1])
        
    
        current_value = a[0]
        for j in range(1, n):
            current_value = (current_value + a[j]) // 2
        
        res.append(current_value)
    
    return res

t = int(input())  # number of test cases
test_ = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_.append((n, a))


res = max_possible_value(t, test_)
for k in res:
    print(k)
