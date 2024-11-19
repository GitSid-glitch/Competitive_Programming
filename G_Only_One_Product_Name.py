from collections import defaultdict

# Function to perform DFS and find connected components
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def find_min_ng_list_size(N, product_names):
    # Build the directed graph
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)  # To handle reverse direction as well

    # Add edges to the graph
    for name in product_names:
        u = name[0]
        v = name[1]
        graph[u].append(v)
        reverse_graph[v].append(u)
    
    # Combine normal and reverse graph edges to ensure undirected component discovery
    full_graph = defaultdict(list)
    for u in graph:
        full_graph[u].extend(graph[u])
    for v in reverse_graph:
        full_graph[v].extend(reverse_graph[v])

    # Find the number of connected components in the undirected graph
    visited = set()
    components = 0

    # For each node (A to Z), perform DFS if it's not visited
    for letter in range(ord('A'), ord('Z') + 1):
        node = chr(letter)
        if node in full_graph and node not in visited:
            dfs(full_graph, node, visited)
            components += 1
    
    # Return the number of components (which is the number of NG list strings)
    return components

# Input
N = int(input())  # Number of product names
product_names = [input().strip() for _ in range(N)]

# Output the result
print(find_min_ng_list_size(N, product_names))
