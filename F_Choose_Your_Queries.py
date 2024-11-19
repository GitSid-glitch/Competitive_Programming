import sys
sys.setrecursionlimit(10**6)

def solve():
    n, m = map(int, input().split())

    edg = [None] * m
    G = [[] for _ in range(n)]

    for i in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        edg[i] = (x, y)
        G[x].append(i)
        G[y].append(i)

    vis = [False] * n
    use = [False] * m
    pa = []

    def get(e, x):
        return edg[e][0] ^ edg[e][1] ^ x

    def dfs(u):
        vis[u] = True
        lst = -1
        for e in G[u]:
            if use[e]:
                continue
            use[e] = True
            v = get(e, u)
            t = -1
            if not vis[v]:
                t = dfs(v)
            if t != -1:
                pa.append((e, t))
            elif lst != -1:
                pa.append((lst, e))
                lst = -1
            else:
                lst = e
        return lst

    for i in range(n):
        if not vis[i]:
            dfs(i)

    ans = [(0, 0)] * m
    for a, b in pa:
        if a > b:
            a, b = b, a
        x = edg[a][0]
        if edg[b][0] != x and edg[b][1] != x:
            x = edg[a][1]
        if edg[a][0] == x:
            ans[a] = (1, 0)
        else:
            ans[a] = (0, 1)
        if edg[b][0] == x:
            ans[b] = (-1, 0)
        else:
            ans[b] = (0, -1)

    for a, b in ans:
        if a + b == 0:
            a = 1
        if a != 0:
            print(f"x{'+' if a > 0 else '-'}")
        else:
            print(f"y{'+' if b > 0 else '-'}")


def main():
    t = 1
    # t = int(input())
    
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
