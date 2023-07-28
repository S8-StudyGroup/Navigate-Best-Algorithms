# [BOJ] 15900. 나무 탈출
# 소요 시간 : 00분
from collections import deque
import sys
input = sys.stdin.readline

# Input => node_cnt, graph
node_cnt = int(input())
graph = [[] for _ in range(node_cnt + 1)]
for _ in range(node_cnt - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs => sum_depth
que = deque([1])
sum_depth = 0
visited = [False] * (node_cnt + 1)
depth = 0

while que:
    for _ in range(len(que)):
        node = que.popleft()    
        visited[node] = True

        if len(graph[node]) == 1 and node != 1:
            sum_depth += depth
        else:
            for child_node in graph[node]:
                if not visited[child_node]:
                    que.append(child_node)

    depth += 1

# Output
if sum_depth % 2 == 0: print('No')
else: print('Yes')
