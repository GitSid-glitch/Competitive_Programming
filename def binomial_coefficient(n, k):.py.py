def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = 1
    denom = 1
    for i in range(k):
        num *= (n - i)
        denom *= (i + 1)
    return num // denom

def count_binary_strings(N):
    if N % 2 != 0:
        return 0  # If N is odd, return 0
    k = N // 2
    return binomial_coefficient(2 * k, k)


N = int(input())
print(count_binary_strings(N))
