from collections import defaultdict

def dfs(node, parent, graph, leaders, leader_count):
    """Perform DFS to calculate the number of leaders in each subtree."""
    # Start with 1 if the current node is a leader, else 0
    count = 1 if node in leaders else 0
    
    # Explore all connected nodes
    for neighbor in graph[node]:
        if neighbor != parent:  # Avoid revisiting the parent
            count += dfs(neighbor, node, graph, leaders, leader_count)
    
    # Store the total leader count for this subtree
    leader_count[node] = count
    return count

def solve():
    # Read input
    n, k = map(int, input().split())
    leader_states = list(map(int, input().split())) if k > 0 else []

    # Build the graph (tree)
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Store leader counts for each subtree
    leader_count = [0] * (n + 1)

    # Use DFS to compute leader counts starting from node 1
    total_leaders = dfs(1, -1, graph, set(leader_states), leader_count)

    # Count valid democratic splits
    valid_splits = 0
    for i in range(2, n + 1):  # Start from node 2 since 1 is the root
        leaders_in_subtree = leader_count[i]
        leaders_in_remaining = total_leaders - leaders_in_subtree

        # A split is valid if both parts have 0 or more than 1 leaders
        if leaders_in_subtree != 1 and leaders_in_remaining != 1:
            valid_splits += 1

    print(valid_splits)

# Run the solution function
solve()
