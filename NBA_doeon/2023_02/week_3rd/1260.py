# [BOJ] 1260. DFS와 BFS
# 소요 시간 : 30분

def dfs(s):
    stack.append(s)
    visited[s] = 1

    while stack:
        p = stack.pop()
        visited[p] = 1
        answer_dfs.append(p)

        for np in graph[p]:
            if visited[np] == 0:
                dfs(np)

def bfs(s):
    visited = [0] * (n + 1)
    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        p = queue.pop(0)
        answer_bfs.append(p)

        for np in graph[p]:
            if visited[np] == 0:
                queue.append(np)
                visited[np] = 1


n, e, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
answer_dfs = []
answer_bfs = []
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for line in graph:
    line.sort()

visited = [0] * (n + 1)
stack = []

dfs(v)
print(*answer_dfs)

bfs(v)
print(*answer_bfs)