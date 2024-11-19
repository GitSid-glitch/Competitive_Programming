import math

# Function to calculate Euclidean distance
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Input parsing
N, S, T = map(int, input().split())
segments = []
for _ in range(N):
    A, B, C, D = map(int, input().split())
    segments.append(((A, B), (C, D)))

# Precompute the distances between all points and the origin (0, 0)
origin = (0, 0)
distances = {}
for i in range(N):
    (A1, B1), (C1, D1) = segments[i]
    distances[(origin, (A1, B1))] = dist(0, 0, A1, B1) / S
    distances[(origin, (C1, D1))] = dist(0, 0, C1, D1) / S

for i in range(N):
    (A1, B1), (C1, D1) = segments[i]
    distances[((A1, B1), (C1, D1))] = dist(A1, B1, C1, D1)
    distances[((C1, D1), (A1, B1))] = dist(C1, D1, A1, B1)
    
# Initialize DP table to large values
INF = float('inf')
dp = [[INF] * 2 for _ in range(1 << N)]
dp[0][0] = dp[0][1] = 0  # Start at the origin with no segments printed

# Iterate over all possible states
for mask in range(1 << N):
    for last in range(N):
        if not (mask & (1 << last)):
            continue
        for prev in range(N):
            if mask & (1 << prev) and prev != last:
                # Transition from previous segment to current segment
                (A1, B1), (C1, D1) = segments[prev]
                (A2, B2), (C2, D2) = segments[last]
                dist_prev_to_current = distances[((A1, B1), (A2, B2))]
                time_to_print = dist(A2, B2, C2, D2) / T
                dp[mask][last] = min(dp[mask][last], dp[mask ^ (1 << last)][prev] + dist_prev_to_current + time_to_print)

# Find the minimum time needed
result = min(dp[(1 << N) - 1][last] for last in range(N))
print(f"{result:.6f}")
