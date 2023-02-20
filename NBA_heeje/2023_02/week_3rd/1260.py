# [BOJ] 1260. DFS와 BFS
# 소요 시간 : 30분

import sys
input = sys.stdin.readline

def dfs(n):
    visited[n] = True
    dfs_list.append(n)
    for w in sorted(adj_list[n]):
        if not visited[w]:
            dfs(w)


def bfs(n):
    visited[n] = True
    queue = [n]
    while queue:
        v = queue.pop(0)
        bfs_list.append(v)
        for w in sorted(adj_list[v]):
            if not visited[w]:
                visited[w] = True
                queue.append(w)


N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

dfs_list = []
bfs_list = []

dfs(V)
visited = [False] * (N + 1)
bfs(V)

print(*dfs_list)
print(*bfs_list)