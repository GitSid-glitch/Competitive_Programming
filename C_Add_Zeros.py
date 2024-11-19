def max_length_after_operations(t, test_cases):
    results = []
    for n, a in test_cases:
        a.sort()  # Sort the array to simplify the search
        operations = 0  # Number of valid operations

        # Use a greedy + binary search approach
        for i in range(n):
            if a[i] <= n + operations:
                operations += 1  # Perform the operation

        # Final length of the array after all possible operations
        results.append(n + operations)

    return results

# Reading input and output
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results and print them
results = max_length_after_operations(t, test_cases)
for result in results:
    print(result)
