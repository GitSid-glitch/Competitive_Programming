import sys
from itertools import accumulate

input = sys.stdin.read
data = input().split()

t = int(data[0])
idx = 1

results = []

for _ in range(t):
    n, k = map(int, data[idx:idx+2])
    idx += 2
    C = list(map(int, data[idx:idx+n]))
    idx += n

    C.sort()
    prefix = [0] + list(accumulate(C))

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for m in range(1, n + 1):
        dp[m] = dp[m - 1] + C[m - 1]
        if m >= k + 1:
            dp[m] = min(dp[m], dp[m - k - 1] + prefix[m] - prefix[m - k])
    
    results.append(' '.join(map(str, dp[1:])))

sys.stdout.write('\n'.join(results) + '\n')

