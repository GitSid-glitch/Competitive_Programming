def difference_array(arr):
    diff = [arr[0]] + [arr[i] - arr[i - 1] for i in range(1, len(arr))] + [0]
    return diff
def apply_update(diff, l, r, val):
    diff[l] += val
    if r + 1 < len(diff): diff[r + 1] -= val
def finalize(diff):
    for i in range(1, len(diff) - 1):
        diff[i] += diff[i - 1]
    return diff[:-1]
arr = [10, 5, 20, 40]
diff = difference_array(arr)
apply_update(diff, 1, 3, 10)
updated_arr = finalize(diff)
print("Updated array:", updated_arr)