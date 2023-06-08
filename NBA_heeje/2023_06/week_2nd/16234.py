# [BOJ] 16234. 인구 이동
# 소요 시간 : 30분

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# 국경선 개방 여부 함수
def open_border_line(i, j, team):
    visited[i][j] = team
    team_info[team].append(matrix[i][j])
    queue = deque()
    queue.append((i, j))

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            move_y, move_x = y + dy[d], x + dx[d]
            if (
                0 <= move_y < N
                and 0 <= move_x < N
                and visited[move_y][move_x] == -1
                and L <= abs(matrix[y][x] - matrix[move_y][move_x]) <= R
            ):
                visited[move_y][move_x] = team
                team_info[team].append(matrix[move_y][move_x])
                queue.append((move_y, move_x))


# 인구 이동 함수
def move_population():
    team_populations = [
        sum(team_info[team_idx]) // len(team_info[team_idx]) for team_idx in range(team)
    ]

    for i in range(N):
        for j in range(N):
            matrix[i][j] = team_populations[visited[i][j]]


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
day = 0

# 인구 이동 진행
while True:
    team = 0
    team_info = defaultdict(list)
    visited = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                open_border_line(i, j, team)
                team += 1
    if team == N**2:
        break

    move_population()
    day += 1

print(day)
