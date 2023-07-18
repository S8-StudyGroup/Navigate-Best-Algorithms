# [BOJ] 3190. 뱀
# 소요 시간 : 00분

import sys
input = sys.stdin.readline
from collections import deque

# 빈칸: 0, 사과: 1, 뱀: 2
N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

L = int(input())
directions = deque()
for _ in range(L):
    X, C = input().split()
    directions.append((int(X), C))

# h: 뱀의 머리, t: 뱀의 꼬리
h_y, h_x = 0, 0
snake = deque()
snake.append((0, 0))
board[0][0] = 2
time = 0

# 0: 우, 1: 하, 2: 좌, 3: 상
d = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

while True:
    time += 1

    move_y, move_x = h_y + dy[d], h_x + dx[d]

    # 벽 또는 자기자신과 부딪히는 경우
    if not (0 <= move_y < N and 0 <= move_x < N) or board[move_y][move_x] == 2:
        break

    h_y, h_x = move_y, move_x
    snake.append((h_y, h_x))
    if board[h_y][h_x] == 0:
        board[snake[0][0]][snake[0][1]] = 0
        snake.popleft()

    board[h_y][h_x] = 2

    if directions and directions[0][0] == time:
        d = (d - 1) % 4 if directions[0][1] == "L" else (d + 1) % 4
        directions.popleft()

print(time)