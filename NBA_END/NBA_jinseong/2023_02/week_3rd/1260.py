# [BOJ] 1260. DFS와 BFS
# 소요 시간 : 30분

# N: 정점개수, M: 간선개수, V: 시작정점 번호
N, M, V = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(v):
    visited[v] = True
    list_dfs.append(v)
    for next_v in sorted(edges[v]):
        if not visited[next_v]:
            dfs(next_v)


def bfs(v):
    visited[v] = True
    queue = [v]
    while queue:
        now_v = queue.pop(0)
        list_bfs.append(now_v)
        for next_v in sorted(edges[now_v]):
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)


visited = [False] * (N + 1)
list_dfs = []
list_bfs = []

dfs(V)
visited = [False] * (N + 1)

bfs(V)

print(*list_dfs)
print(*list_bfs)