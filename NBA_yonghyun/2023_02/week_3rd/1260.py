# [BOJ] 1260. DFS와 BFS
# 소요 시간 : 30분

# [백준] 1260. DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())

node = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


def dfs(start):
    now_list = sorted(node[start])
    for i in now_list:
        if not visited[i]:
            visited[i] = 1
            dfs_result.append(i)
            dfs(i)
    else:
        return

visited[v] = 1
dfs_result = [v]
dfs(v)
print(*dfs_result)


bfs_result = [v]
queue = deque([v])
def bfs(start):
    while queue:
        now = queue.popleft()
        now_list = sorted(node[now])
        for i in now_list:
            if visited[i]:
                queue.append(i)
                visited[i] = 0
                bfs_result.append(i)

visited[v] = 0      # 아까 썼던 visited 재사용 해야쥥
bfs(v)
print(*bfs_result)