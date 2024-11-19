import math
import sys
input = sys.stdin.read

def calculate_mex(arr, n):
    """Calculate the MEX (minimum excluded element) for the array `arr` up to n."""
    present = [False] * (n + 1)
    for num in arr:
        if num < n:
            present[num] = True
    for i in range(n + 1):
        if not present[i]:
            return i
    return n

def solve(test_cases):
    results = []
    for n, b, c in test_cases:
        if b == 0:
            # Case where b = 0, all elements are the same, a_i = c
            if 0 <= c < n:
                results.append(0)  # Already a permutation if c is in the range [0, n-1]
            else:
                results.append(-1)  # Impossible to form a permutation
            continue

        # Check if gcd(b, n) == 1 for possible full coverage of 0 to n-1
        if math.gcd(b, n) != 1:
            results.append(-1)
            continue
        
        # Simulate replacements to form a permutation for smaller values of n
        a = [(b * i + c) % n for i in range(n)]
        operations = 0
        seen_states = set()

        while True:
            mex = calculate_mex(a, n)
            max_val = max(a)

            # If the max value is already less than n, we have a permutation
            if max_val < n:
                results.append(operations)
                break
            
            # Replace the leftmost max element with MEX
            max_index = a.index(max_val)
            a[max_index] = mex
            operations += 1

            # Detect cycles to prevent infinite loops
            state = tuple(a)
            if state in seen_states:
                results.append(-1)
                break
            seen_states.add(state)

    return results

# Example usage with test cases
data = input().strip().splitlines()
t = int(data[0])
test_cases = [tuple(map(int, line.split())) for line in data[1:t+1]]
results = solve(test_cases)
print("\n".join(map(str, results)))
