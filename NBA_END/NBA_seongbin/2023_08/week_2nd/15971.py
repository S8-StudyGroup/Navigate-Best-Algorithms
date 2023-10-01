# [BOJ] 15971. 두 로봇
# 소요 시간 : 00분
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, a, b = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y, v = map(int, input().split())
    graph[x].append((y, v))
    graph[y].append((x, v))


def bfs():
    queue = deque([(a, 0, 0)])
    visited = [False] * (n + 1)
    visited[a] = True

    while queue:
        x, total_path, max_value = queue.popleft()
        if x == b:
            return total_path - max_value
        for y, v in graph[x]:
            if not visited[y]:
                visited[y] = True
                queue.append((y, total_path + v, max(max_value, v)))


answer = bfs()

print(answer)
