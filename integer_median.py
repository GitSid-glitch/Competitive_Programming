def modular_inverse(a, mod):
    """Returns the modular inverse of a under modulo mod using Fermat's Little Theorem."""
    return pow(a, mod - 2, mod)

def calculate_probability(N, M):
    MOD = 998244353

    if N == 1:
        # With only one number, the median is always an integer
        return 1

    # Total number of combinations of picking N integers from M
    total_combinations = M**N % MOD

    if N % 2 == 1:
        # If N is odd, all cases have integer medians
        valid_combinations = total_combinations
    else:
        # If N is even, we count cases where median is an integer
        # Half the combinations will have (N/2)-th and (N/2+1)-th smallest sum to even
        valid_combinations = total_combinations // 2

    # Probability fraction: P / Q
    P = valid_combinations
    Q = total_combinations

    # Compute Q^-1 modulo MOD
    Q_inv = modular_inverse(Q, MOD)

    # Return P * Q^-1 modulo MOD
    return (P * Q_inv) % MOD

# Input handling
if __name__ == "__main__":
    N, M = map(int, input().split())
    result = calculate_probability(N, M)
    print(result)
