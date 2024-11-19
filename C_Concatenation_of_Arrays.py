def problem_c(t, tc):
    r = []
    for test in tc:
        n, arrays = test
        # Sort each pair, ensuring that the smaller element comes first
        p = [[min(a[0], a[1]), max(a[0], a[1])] for a in arrays]
        p.sort()
        
        # Create a new arrangement of the output
        r1 = []
        for i in range(len(p)):
            # Append the first element of the pair
            r1.append(p[i][0])
        for i in range(len(p)):
            # Append the second element of the pair
            r1.append(p[i][1])
        
        r.append(r1)
    return r

# Input reading
t = int(input())
tc = []
for i in range(t):
    n = int(input())
    arrays = [list(map(int, input().split())) for _ in range(n)]
    tc.append((n, arrays))

# Process and get the result
r = problem_c(t, tc)

# Output the result
for r1 in r:
    print(" ".join(map(str, r1)))
