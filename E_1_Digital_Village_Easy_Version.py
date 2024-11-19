import heapq
from collections import defaultdict

def solve():
    # Reading the number of test cases
    t = int(input())
    
    for _ in range(t):
        # Reading number of houses, number of cables, and number of houses requiring internet
        n, m, p = map(int, input().split())
        
        # Reading the list of houses requiring internet
        need_internet = list(map(int, input().split()))
        
        # Reading the graph edges and their latencies
        graph = defaultdict(list)
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Function to perform multisource Dijkstra's Algorithm
        def multisource_dijkstra(servers):
            # Initialize distances with infinity
            min_latency = [float('inf')] * (n + 1)
            pq = []
            
            # Initialize all servers in the priority queue with 0 latency
            for server in servers:
                heapq.heappush(pq, (0, server))
                min_latency[server] = 0
            
            # Dijkstra's Algorithm
            while pq:
                current_latency, u = heapq.heappop(pq)
                
                if current_latency > min_latency[u]:
                    continue
                
                for v, w in graph[u]:
                    new_latency = max(current_latency, w)
                    if new_latency < min_latency[v]:
                        min_latency[v] = new_latency
                        heapq.heappush(pq, (new_latency, v))
            
            # Return the latencies for the houses that require internet
            return [min_latency[house] for house in need_internet]
        
        # We need to find the minimum latency for each k = 1 to n (number of servers)
        results = []
        for k in range(1, n + 1):
            # We select the first `k` houses as servers (naive approach)
            if k <= len(need_internet):
                servers = need_internet[:k]
                latencies = multisource_dijkstra(servers)
                results.append(sum(latencies))
            else:
                # If k > number of houses needing internet, total latency becomes 0
                results.append(0)
        
        # Output the results for this test case
        print(" ".join(map(str, results)))

# Sample input execution
solve()
