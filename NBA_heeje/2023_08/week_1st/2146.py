# [BOJ] 2146. 다리 만들기
# 소요 시간 : 60분

import sys
from collections import deque
input = sys.stdin.readline

def rename_island(sy, sx):
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = True
    matrix[sy][sx] = team

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and matrix[ny][nx] == 1:
                visited[ny][nx] == True
                matrix[ny][nx] = team
                queue.append((ny, nx))


def find_shortest_bridge(team):
    global shortest_bridge
    dist = [[-1] * N for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == team:
                queue.append((i, j))
                dist[i][j] = 0
    
    while queue:
        y, x = queue.popleft()

        if dist[y][x] == shortest_bridge:
            continue

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and dist[ny][nx] == -1:
                if matrix[ny][nx] != 0:
                    shortest_bridge = min(shortest_bridge, dist[y][x])
                else:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny, nx))


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
team = 2

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            rename_island(i, j)
            team += 1

shortest_bridge = 200
for i in range(2, team):
    find_shortest_bridge(i)

print(shortest_bridge)