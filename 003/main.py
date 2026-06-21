N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

# ノードsからの距離を求める関数
def dfs(s):
    dist = [-1] * N
    dist[s] = 0

    stack = [s]
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            stack.append(nv)
    return dist


dist0 = dfs(0)
u = max(enumerate(dist0), key=lambda x: x[1])[0]
distu = dfs(u)
print(max(distu) + 1)
