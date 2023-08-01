# [BOJ] 2146. 다리 만들기
# 소요 시간 : 00분
from collections import deque

def bfs(x,y,group):
    queue = deque([(x,y)])
    board[x][y] = -1
    groups.append([])
    groups[group].append((x,y))
    while queue:
        x, y = queue.pop()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0:
                queue.append((nx, ny))
                groups[group].append((nx, ny))
                board[nx][ny] = -1
    return group + 1


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

groups = []
group_num = 0
queue = deque([])
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            group_num = bfs(i, j, group_num)

min_dist = 10000
for group1 in range(group_num):
    for group2 in range(group1 + 1, group_num):
        for land1 in groups[group1]:
            for land2 in groups[group2]:
                min_dist = min(abs(land2[0] - land1[0]) + abs(land2[1] - land1[1]) - 1, min_dist)

print(min_dist)