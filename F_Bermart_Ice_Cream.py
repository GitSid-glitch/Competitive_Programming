def can_paint_all_cells(a, n, k):
    # This function checks if it's possible to cover all cells in `a` with the given `k`
    max_reach = a[0]  # Start from the first cell in `a`
    for i in range(1, n):
        if a[i] > max_reach + k:
            # If the next required cell is beyond the current reachable range
            max_reach = a[i] + k  # Shift the range to start from this cell
            # Check if we need an additional cell to bridge the gap
            if a[i] - a[i - 1] > 2 * k:
                return False  # Can't reach this cell even with the extra

    return True

def minimum_k(t, test_cases):
    results = []
    for a in test_cases:
        n = len(a)
        low, high = 0, (a[-1] - a[0])  # The max possible `k` is the max distance between any two points in `a`
        
        while low < high:
            mid = (low + high) // 2
            if can_paint_all_cells(a, n, mid):
                high = mid  # Try for a smaller `k`
            else:
                low = mid + 1  # Increase `k`
        
        results.append(low)
    return results

# Input parsing and calling `minimum_k`
t = int(input())  # Number of test cases
results = []

for _ in range(t):
    n = int(input())  # Number of cells in this test case
    a = list(map(int, input().split()))  # List of cells that need to be painted
    results.append(can_paint_all_cells(a))

# Printing results for each test case
for result in results:
    print(result)