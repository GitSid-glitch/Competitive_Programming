import heapq

def variable_damage(queries):
    heroes = []  # Max-heap (negative values) to store heroes' health
    artifacts = []  # Min-heap to store artifacts' durability
    total_damage_needed = 0
    artifact_total = 0
    results = []

    for query_type, value in queries:
        if query_type == 1:
            # Add hero with health 'value'
            heapq.heappush(heroes, -value)  # Push as negative for max-heap behavior
            total_damage_needed += value
        else:
            # Add artifact with durability 'value'
            heapq.heappush(artifacts, value)
            artifact_total += value

        # Now calculate how many rounds Monocarp can survive
        if not heroes:
            results.append(0)
        else:
            max_rounds = (total_damage_needed + artifact_total) // len(heroes)
            results.append(max_rounds)

    return results


# Reading inputs from the user
if __name__ == "__main__":
    n = int(input())  # Number of queries
    queries = []
    
    for _ in range(n):
        t, v = map(int, input().split())
        queries.append((t, v))
    
    # Get the results for each query
    results = variable_damage(queries)
    
    # Output each result
    for result in results:
        print(result)
