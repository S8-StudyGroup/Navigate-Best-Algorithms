# [BOJ] 17141. 연구소 2
# 소요 시간 : 60분
from itertools import combinations
from copy import deepcopy
from collections import deque

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(virous):

    for row, col in virous:
        lab[row][col] = 3

    queue = deque(virous)

    while queue:

        r, c = queue.popleft()

        day = lab[r][c]

        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]

            if 0 <= nr < n and 0 <= nc < n:
                value = lab[nr][nc]

                if value == 2 or value == 0:
                    lab[nr][nc] = day + 1
                    queue.append([nr, nc])

    for row in range(n):
        for col in range(n):
            value = lab[row][col]

            if value == 0:
                return -1

    return day - 3


INF = 999999999
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = INF
virous = []

for row in range(n):
    for col in range(n):
        value = matrix[row][col]

        if value == 2:
            virous.append([row, col])

for arr in combinations(virous, m):
    lab = deepcopy(matrix)

    min_day = bfs(arr)

    if min_day < answer <= INF and min_day != -1:
        answer = min_day

    if answer == -1 and min_day != -1:
        answer = min_day

if answer == INF:
    answer = -1

print(answer)
