# [BOJ] 1986. 체스
# 소요 시간 : 30분

import sys
input = sys.stdin.readline

def move_knight(y, x):
    cnt = 0
    for dy, dx in k_dir:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and not board[ny][nx]:
            board[ny][nx] = "X"
            cnt += 1
    
    return cnt

def move_queen(y, x):
    cnt = 0
    for dy, dx in q_dir:
        ny, nx = y + dy, x + dx
        while 0 <= ny < n and 0 <= nx < m:
            if not board[ny][nx]:
                board[ny][nx] = "X"
                cnt += 1

            elif board[ny][nx] != "X":
                break

            ny, nx = ny + dy, nx + dx
    
    return cnt

n, m = map(int, input().split())
board = [[""] * m for _ in range(n)]

queens = list(map(int, input().split()))

for i in range(1, queens[0] * 2, 2):
    board[queens[i] - 1][queens[i + 1] - 1] = "Q"

knights = list(map(int, input().split()))
for i in range(1, knights[0] * 2, 2):
    board[knights[i] - 1][knights[i + 1] - 1] = "K"

pawns = list(map(int, input().split()))
for i in range(1, pawns[0] * 2, 2):
    board[pawns[i] - 1][pawns[i + 1] - 1] = "P"

safe_zone = n * m - queens[0] - knights[0] - pawns[0]

q_dir = [
    (-1, 0), (-1, 1),
    (0, 1), (1, 1),
    (1, 0), (1, -1),
    (0, -1), (-1, -1),
    ]

k_dir = [
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (-2, -1), (-2, 1),
    (2, -1), (2, 1),
    ]

for i in range(n):
    for j in range(m):
        if board[i][j] == "K":
            safe_zone -= move_knight(i, j)
        elif board[i][j] == "Q":
            safe_zone -= move_queen(i, j)

print(safe_zone)