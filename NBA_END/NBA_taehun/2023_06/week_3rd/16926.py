# [BOJ] 16926. 배열 돌리기 1
# 소요 시간 : 00분

import sys

input = sys.stdin.readline


# 회전
def curl(r, c):
    if r == low_row_cursor:
        r, c = left(r, c, R)
    elif r == high_row_cursor:
        r, c = right(r, c, R)
    elif c == low_col_cursor:
        r, c = down(r, c, R)
    elif c == high_col_cursor:
        r, c = up(r, c, R)
    return r, c


def down(r, c, move):
    diff = (r + move) - high_row_cursor
    if diff > 0:
        r = high_row_cursor
        r, c = right(r, c, diff)
    else:
        r += move
    return r, c


def right(r, c, move):
    diff = (c + move) - high_col_cursor
    if diff > 0:
        c = high_col_cursor
        r, c = up(r, c, diff)
    else:
        c += move
    return r, c


def up(r, c, move):
    diff = low_row_cursor - (r - move)
    if diff > 0:
        r = low_row_cursor
        r, c = left(r, c, diff)
    else:
        r -= move
    return r, c


def left(r, c, move):
    diff = low_col_cursor - (c - move)
    if diff > 0:
        c = low_col_cursor
        r, c = down(r, c, diff)
    else:
        c -= move
    return r, c


N, M, R = map(int, input().strip().split())

arr = [list(map(int, input().strip().split())) for _ in range(N)]

result = [[0] * M for _ in range(N)]

# row와 col의 최대, 최소값 커서를 옮기며 탐색
low_row_cursor, high_row_cursor = 0, N - 1
low_col_cursor, high_col_cursor = 0, M - 1

# 커서끼리 만나기 전까지 탐색
while high_row_cursor - low_row_cursor > 0 and high_col_cursor - low_col_cursor > 0:
    for r in [low_row_cursor, high_row_cursor]:
        for c in range(low_col_cursor, high_col_cursor + 1):
            nr, nc = curl(r, c)
            result[nr][nc] = arr[r][c]

    for c in [low_col_cursor, high_col_cursor]:
        for r in range(low_row_cursor, high_row_cursor + 1):
            nr, nc = curl(r, c)
            result[nr][nc] = arr[r][c]

    # 커서 이동
    low_row_cursor += 1
    high_row_cursor -= 1
    low_col_cursor += 1
    high_col_cursor -= 1

for line in result:
    print(*line)
