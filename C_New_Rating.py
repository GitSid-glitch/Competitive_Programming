import sys
input = sys.stdin.read

def max_possible_rating(n, a):
    # Prefix calculations
    prefix = [0] * n
    x = 0
    for i in range(n):
        if a[i] > x:
            x += 1
        elif a[i] < x:
            x -= 1
        prefix[i] = x

    # Suffix calculations
    suffix = [0] * n
    x = 0
    for i in range(n - 1, -1, -1):
        if a[i] > x:
            x += 1
        elif a[i] < x:
            x -= 1
        suffix[i] = x

    # The maximum rating achievable by skipping exactly one interval
    max_rating = -float('inf')

    # Try skipping every possible interval
    for r in range(1, n):
        # Check by skipping from l to r, combine the prefix up to l-1 and suffix from r+1
        if r < n:
            max_rating = max(max_rating, prefix[r - 1] + suffix[r])

    return max_rating

def main():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        results.append(str(max_possible_rating(n, a)))
    
    # Print all results at once to avoid TLE due to multiple I/O operations
    print("\n".join(results))

# Run this function if taking input from standard input as for competitive programming
main()
