def prefix_sum_2d(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    prefix_sum_matrix = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            prefix_sum_matrix[i][j] = matrix[i][j]
            if i > 0:
                prefix_sum_matrix[i][j] += prefix_sum_matrix[i - 1][j]
            if j > 0:
                prefix_sum_matrix[i][j] += prefix_sum_matrix[i][j - 1]
            if i > 0 and j > 0:
                prefix_sum_matrix[i][j] -= prefix_sum_matrix[i - 1][j - 1]
    return prefix_sum_matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = prefix_sum_2d(matrix)
print("Original matrix:")
for row in matrix:
    print(row)
print("\n2D Prefix sum matrix:")
for row in result:
    print(row)