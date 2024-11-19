MOD = 998244353

MAX_ = 22  # Since 2^22 > 4 * 10^6
p = [2**i for i in range(MAX_ + 1)]

def count_configurations(Y):
    dp = [0] * (Y + 1)
    dp[0] = 1  
    for i in p:
        if i > Y:
            break
        for c_u in range(Y, i - 1, -1):  
            dp[c_u] = (dp[c_u] + dp[c_u - i]) % MOD

    return dp[Y]

import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
q = list(map(int, data[1:t+1]))

results = [count_configurations(Y) for Y in q]
sys.stdout.write("\n".join(map(str, results)) + "\n")
