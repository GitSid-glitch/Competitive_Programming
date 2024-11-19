'''def total_manhattan_distance(test_cases):
    results = []
    for n, m, r, c in test_cases:
        # Determine the index of the person who leaves (1-based to 0-based index)
        leave_index = (r - 1) * m + (c - 1)

        total_distance = 0
        total_people = n * m

        # Calculate the movement cost for each person after the leaving person
        for i in range(leave_index + 1, total_people):
            # Original position (1-based row, column)
            original_row = i // m + 1
            original_col = i % m + 1

            # New position (after shifting leftward)
            new_row = (i - 1) // m + 1
            new_col = (i - 1) % m + 1

            # Calculate Manhattan distance for the shift
            distance = abs(original_row - new_row) + abs(original_col - new_col)
            total_distance += distance

        results.append(total_distance)

    return results

# Input reading and output
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = total_manhattan_distance(test_cases)
for result in results:
    print(result)'''



'''def manhattan_distance_sum(test):
    results = []
    for n, m, r, c in test:
    # Step 1: Find the index of the person leaving (1-based index)
        i = (r - 1) * m + c

        total_distance = 0

        # Step 2: Calculate the Manhattan distance for each movement of persons j > i
        for j in range(i + 1, n * m + 1):
            # Original position of person j: (r0, c0)
            r0, c0 = divmod(j - 1, m)

            # New position of person j: (r1, c1) (one position back in row-major order)
            r1, c1 = divmod(j - 2, m)

            # Calculate Manhattan distance for the move
            total_distance += abs(r0 - r1) + abs(c0 - c1)
        results.append(total_distance)

    return results

t=int(input())
for i in range(t):
    test=[tuple(map(int,input().split()))]
    results=manhattan_distance_sum(test)
    for i in results:
        print(i)

'''

def manhattan_distance(n, m, r, c):
    # Calculate distances to each of the four corners from (r, c)
    d1 = abs(r - 1) + abs(c - 1)         # Top-left corner
    d2 = abs(r - 1) + abs(c - m)         # Top-right corner
    d3 = abs(r - n) + abs(c - 1)         # Bottom-left corner
    d4 = abs(r - n) + abs(c - m)         # Bottom-right corner
    # The result is the maximum distance to any of the corners
    return max(d1, d2, d3, d4)

# Reading input
import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
results = []
idx = 1
for _ in range(t):
    n = int(data[idx])
    m = int(data[idx+1])
    r = int(data[idx+2])
    c = int(data[idx+3])
    results.append(manhattan_distance(n, m, r, c))
    idx += 4

# Output results
print("\n".join(map(str, results)))


