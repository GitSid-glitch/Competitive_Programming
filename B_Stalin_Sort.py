'''def minimum_removals_to_vulnerable(t, test_cases):
    results = []
    
    for n, arr in test_cases:
        # Track the longest non-increasing subsequence
        lis = []
        
        for num in arr:
            # Find the position in lis where num should go to maintain non-increasing order
            pos = binary_search_descending(lis, num)
            
            # If position is within current list, replace it; otherwise, append
            if pos < len(lis):
                lis[pos] = num
            else:
                lis.append(num)
        
        # Minimum removals = total elements - longest non-increasing subsequence length
        results.append(n - len(lis))
    
    return results

def binary_search_descending(arr, x):
    """ Binary search to find insertion point for x in descending order list `arr`. """
    lo, hi = 0, len(arr)
    
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] >= x:
            lo = mid + 1
        else:
            hi = mid
            
    return lo

# Input Reading and Execution
t = int(input().strip())
test_cases = [(int(input().strip()), list(map(int, input().strip().split()))) for _ in range(t)]

# Run the function and print results
results = minimum_removals_to_vulnerable(t, test_cases)
for result in results:
    print(result)'''



def min_removals_to_make_vulnerable(arr):
    n = len(arr)
    if n <= 1:
        return 0  # If the array is empty or has one element, no removals needed

    valid_elements = []  # This will hold the elements that can form a vulnerable array

    for num in arr:
        # If valid_elements is empty or the current number is less than or equal to the last element in valid_elements
        if not valid_elements or num <= valid_elements[-1]:
            valid_elements.append(num)
        else:
            # This number cannot be added to valid_elements, we consider it a removal
            continue  # Skip adding this number

    # The number of removals required
    return n - len(valid_elements)

# Test case
arr = [3, 6, 4, 9, 2, 5, 2]
removals = min_removals_to_make_vulnerable(arr)
print("Minimum removals to make the array vulnerable:", removals)

