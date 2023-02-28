# [BOJ] 1260. DFS와 BFS
# 소요 시간 : 30분

# DFS와 BFS

def dfs(node):
    visited[node] = True
    dfs_result.append(node)
    for next_node in sorted(edges[node]):
        if not visited[next_node]:
            dfs(next_node)


def bfs(start):
    visited[start] = True
    que = [start]
    que.sort()
    while que:
        node = que.pop(0)
        bfs_result.append(node)
        for next_node in sorted(edges[node]):
            if not visited[next_node]:
                visited[next_node] = True
                que.append(next_node)


node_cnt, edge_cnt, start_node = map(int, input().split())

edges = [[] for _ in range(node_cnt + 1)]
visited = [False] * (node_cnt + 1)

for _ in range(edge_cnt):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

dfs_result = []
bfs_result = []

dfs(start_node)

visited = [False] * (node_cnt + 1)

bfs(start_node)

print(*dfs_result)
print(*bfs_result)