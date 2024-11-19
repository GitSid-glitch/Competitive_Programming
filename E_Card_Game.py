MOD = 998244353

# Helper function to compute factorial % MOD
def factorial(x, mod):
    result = 1
    for i in range(2, x + 1):
        result = (result * i) % mod
    return result

# Helper function to compute modular inverse using Fermat's little theorem
def mod_inverse(x, mod):
    return pow(x, mod - 2, mod)

# Helper function to compute binomial coefficient % MOD
def binomial_coefficient(n, k, mod):
    if k > n:
        return 0
    num = factorial(n, mod)
    denom = (factorial(k, mod) * factorial(n - k, mod)) % mod
    return (num * mod_inverse(denom, mod)) % mod

def count_ways_to_win(n, m):
    # Special case: If there is only one suit (n = 1), the answer is always 2
    if n == 1:
        return 2

    # All m cards of suit 1 must go to the first player
    # Remaining (n-1) * m cards need to be split evenly
    remaining_cards = (n - 1) * m
    half = remaining_cards // 2

    # Calculate the binomial coefficient C(remaining_cards, half) % MOD
    ways = binomial_coefficient(remaining_cards, half, MOD)
    return ways

# Input reading
n, m = map(int, input().split())
result = count_ways_to_win(n, m)
print(result)
