# [BOJ] 1260. DFS와 BFS
# 소요 시간 : 30분

import sys
from collections import deque

input = sys.stdin.readline

# dfs
def dfs(v):
    visited[v] = True
    result.append(v)
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

#bfs
def bfs(v):
    visited = [True] + [False] * N
    dq = deque([v])
    visited[v] = True
    while dq:
        v = dq.popleft()
        result.append(v)
        for next_v in graph[v]:
            if not visited[next_v]:
                dq.append(next_v)
                visited[next_v] = True

N, M, V = map(int, input().strip().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

graph = list(map(sorted, graph))

visited = [True] + [False] * N
result = []
dfs(V)
print(*result)

result = []
bfs(V)
print(*result)
