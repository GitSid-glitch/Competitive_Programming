def prefix_sum(arr):
    prefix_sum_array = [0] * len(arr)
    prefix_sum_array[0] = arr[0]  
    for i in range(1, len(arr)):
        prefix_sum_array[i] = prefix_sum_array[i - 1] + arr[i]
    return prefix_sum_array
arr = [1, 2, 3, 4, 5]
result = prefix_sum(arr)
print("Original array:", arr)
print("Prefix sum array:", result)