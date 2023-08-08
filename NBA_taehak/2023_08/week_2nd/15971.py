# [BOJ] 15971. 두 로봇
# 소요 시간 : 00분
import sys
from collections import deque

sys.setrecursionlimit(100000)

# Input
room_cnt, robot_a, robot_b = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(room_cnt - 1)]

# graph
graph = [[] for _ in range(room_cnt + 1)]
for a, b, d in edges:
    graph[a].append((b, d))
    graph[b].append((a, d))

# dfs = 81점
visited = [False] * (room_cnt + 1)


def dfs(node, max_d=0, sum_d=0):
    visited[node] = True

    if node == robot_b:
        print(sum_d - max_d)

    for next_node, d in graph[node]:
        if not visited[next_node]:
            dfs(next_node, max(max_d, d), sum_d + d)
    
    visited[node] = False


# bfs
def bfs(a, b):
    queue = deque()
    queue.append((a, 0, 0))
    visited = [False] * (room_cnt + 1)
    visited[a] = True

    while queue:
        node, max_dist, sum_dist = queue.popleft()

        if node == b:
            return sum_dist - max_dist

        for v, dist in graph[node]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, max(max_dist, dist), sum_dist + dist))



# Output
# dfs(robot_a)
print(bfs(robot_a, robot_b))