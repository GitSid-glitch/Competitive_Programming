from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    # Read n and q
    n = int(data[0])
    q = int(data[1])

    # Read the binary array and transform it (0 -> -1)
    arr = [int(x) for x in data[2:n + 2]]
    transformed = [1 if x == 1 else -1 for x in arr]

    # Collect queries and store them with their indices
    queries = []
    index = n + 2
    for i in range(q):
        l = int(data[index]) - 1  # Convert to 0-based indexing
        r = int(data[index + 1])  # Right index (exclusive for easier Mo's processing)
        queries.append((l, r, i))
        index += 2

    # Mo's algorithm requires sorting queries based on blocks and right index
    BLOCK_SIZE = int(n ** 0.5)

    def mo_sort(query):
        l, r, idx = query
        block = l // BLOCK_SIZE
        return (block, r if block % 2 == 0 else -r)

    # Sort queries according to Mo's ordering
    queries.sort(key=mo_sort)

    # Mo's algorithm variables
    curr_l, curr_r, curr_sum = 0, 0, 0
    freq = defaultdict(int)
    freq[0] = 1  # Initial prefix sum of 0

    # Result array to store answers for all queries
    result = [0] * q

    # Process each query in Mo's order
    for l, r, idx in queries:
        # Expand range to the right (move `curr_r` rightwards)
        while curr_r < r:
            curr_sum += transformed[curr_r]
            result[idx] += freq[curr_sum]
            freq[curr_sum] += 1
            curr_r += 1

        # Shrink range from the right (move `curr_r` leftwards)
        while curr_r > r:
            curr_r -= 1
            freq[curr_sum] -= 1
            result[idx] -= freq[curr_sum]
            curr_sum -= transformed[curr_r]

        # Expand range to the left (move `curr_l` leftwards)
        while curr_l > l:
            curr_l -= 1
            curr_sum += transformed[curr_l]
            result[idx] += freq[curr_sum]
            freq[curr_sum] += 1

        # Shrink range from the left (move `curr_l` rightwards)
        while curr_l < l:
            freq[curr_sum] -= 1
            result[idx] -= freq[curr_sum]
            curr_sum -= transformed[curr_l]
            curr_l += 1

    # Print all results for each query
    sys.stdout.write('\n'.join(map(str, result)) + '\n')
solve()