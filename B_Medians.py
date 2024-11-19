'''def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  # number of test cases
    idx = 1  # start index for reading test case data
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])  # length of array
        k = int(data[idx + 1])  # target median value
        idx += 2
        
        # Check if it is possible to create subarrays with median k
        # If k is positioned within the array such that it could be a median value, we proceed.
        # Specifically, we need k to be in the central position of a sequence that allows it to be a median.
        
        # We need at least one subarray such that its median is k
        if k > (n + 1) // 2:
            results.append("-1")
            continue
        
        # If possible, choose the smallest m such that median of medians is k
        m = (n + 1) // 2  # The minimum odd m that divides n around the center
        positions = []
        
        # Generate left borders
        for i in range(m):
            positions.append(i * 2 + 1)  # left borders for odd-length intervals
        
        # Record the result for the current test case
        results.append(f"{m}")
        results.append(" ".join(map(str, positions)))
    
    # Print all results for each test case
    sys.stdout.write("\n".join(results) + "\n")
solve()'''

def solve():
    t = int(input())  # Number of test cases
    results = []
    
    for _ in range(t):
        n, k = map(int, input().split())
        
        # The array is just [1, 2, ..., n], so we can directly work with indices
        a = list(range(1, n + 1))
        
        # Check if k is within the bounds of the median's possible values
        if a[n // 2] != k:
            results.append("-1")
            continue
        
        # Choose m subarrays such that the medians work out
        # The simplest choice is subarrays of length 1.
        m = n  # Take all elements as single-element subarrays
        
        # Output m and the starting indices of each subarray
        results.append(f"{m}")
        results.append(" ".join(str(i + 1) for i in range(n)))
    
    # Print all results
    print("\n".join(results))

solve()

# Example usage:
# Input:
# 4
# 1 1
# 3 2
# 3 3
# 15 8

# Expected Output:
# 1
# 1
# 3
# 1 2 3
# -1
# 5
# 1 4 7 10 13
