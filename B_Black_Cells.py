def can_paint_all_cells(a, n, k):
    # This function checks if it's possible to cover all cells in `a` with the given `k`
    max_reach = a[0] + k  # Start from the first cell in `a` with range `k`
    added_extra = False   # Track if we used the one extra cell

    for i in range(1, n):
        if a[i] > max_reach:
            if added_extra:  # If we've already used an extra cell and still can't reach, fail
                return False
            added_extra = True
            max_reach = a[i - 1] + 2 * k  # Extend range by using one extra cell
            if a[i] > max_reach:  # If even with extra cell we can't reach the next cell
                return False
        else:
            max_reach = a[i] + k  # Update reachable range if the cell is within reach

    return True

def minimum_k_for_test_case(a):
    n = len(a)
    low, high = 0, a[-1] - a[0]  # The max possible `k` is the max distance between any two points in `a`
    
    while low < high:
        mid = (low + high) // 2
        if can_paint_all_cells(a, n, mid):
            high = mid  # Try for a smaller `k`
        else:
            low = mid + 1  # Increase `k`
    
    return low

# Reading input
t = int(input())  # Number of test cases
results = []

for _ in range(t):
    n = int(input())  # Number of cells in this test case
    a = list(map(int, input().split()))  # List of cells that need to be painted
    results.append(minimum_k_for_test_case(a))

# Printing results for each test case
for result in results:
    print(result)
