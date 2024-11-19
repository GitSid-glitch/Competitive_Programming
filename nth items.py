import math

def minimum_payment_per_test_case(n, k, prices):
    # Sort prices to utilize the free-item offer optimally
    prices.sort()
    
    # Compute prefix sums to calculate costs quickly
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + prices[i - 1]
    
    # Result array to store the minimum payment required for each m = 1 to n
    result = [0] * n
    
    # Calculate minimum costs for each number of items m
    for m in range(1, n + 1):
        # Number of items we actually have to pay for to get exactly m items, using the free item offer
        pay_count = (m + k) // (k + 1)
        
        # Minimum cost is the sum of the cheapest 'pay_count' items
        result[m - 1] = prefix_sum[pay_count]
    
    return result

# Process all test cases
t = int(input())
output = []
for _ in range(t):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    output.append(" ".join(map(str, minimum_payment_per_test_case(n, k, prices))))

# Print all results for each test case
print("\n".join(output))
