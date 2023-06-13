# [BOJ] 21609. 상어 중학교
# 소요 시간 : 90분

import sys
from collections import deque

input = sys.stdin.readline


def bfs(block, block_type, visited):
    queue = deque()
    queue.append(block)
    block_group = [block]
    rainbow_blocks = []

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            move_y, move_x = y + dy[d], x + dx[d]
            if (
                0 <= move_y < N
                and 0 <= move_x < N
                and not visited[move_y][move_x]
                and (
                    matrix[move_y][move_x] == 0 or matrix[move_y][move_x] == block_type
                )
            ):
                visited[move_y][move_x] = True
                if matrix[move_y][move_x] == 0:
                    rainbow_blocks.append((move_y, move_x))
                queue.append((move_y, move_x))
                block_group.append((move_y, move_x))

    for y, x in rainbow_blocks:
        visited[y][x] = False

    return block_group if len(block_group) > 1 else []


def count_rainbow_blocks(block_group):
    return len(list(filter(lambda x: matrix[x[0]][x[1]] == 0, block_group)))


def find_standard_block(block_group):
    min_row = block_group[0][0]
    min_col = block_group[0][1]

    for row, col in block_group:

        if matrix[row][col] == 0:
            continue

        if min_row < row:
            continue

        if min_row == row:
            if min_col < col:
                continue

        min_row, min_col = row, col

    return min_row, min_col


def find_largest_block_group():
    visited = [[False] * N for _ in range(N)]
    largest_block_group = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and 0 < matrix[i][j] <= 5:
                visited[i][j] = True
                block_group = bfs((i, j), matrix[i][j], visited)
                if not block_group or len(largest_block_group) > len(block_group):
                    continue
                if len(largest_block_group) == len(block_group):
                    lbg_rainbow_blocks = count_rainbow_blocks(largest_block_group)
                    bg_rainbow_blocks = count_rainbow_blocks(block_group)
                    if lbg_rainbow_blocks > bg_rainbow_blocks:
                        continue

                    if lbg_rainbow_blocks == bg_rainbow_blocks:
                        min_row_lbg, min_col_lbg = find_standard_block(
                            largest_block_group
                        )
                        min_row_bg, min_col_bg = find_standard_block(block_group)

                        if min_row_lbg > min_row_bg:
                            continue

                        if min_row_lbg == min_row_bg:
                            if min_col_lbg > min_col_bg:
                                continue

                largest_block_group = block_group

    return largest_block_group


def rotate_90():
    return list(map(list, zip(*matrix)))[::-1]


def gravity():
    for j in range(N):
        for i in range(N - 2, -1, -1):
            if matrix[i][j] in [-1, 7]:
                continue
            while i + 1 < N and matrix[i + 1][j] == 7:
                matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
                i += 1


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
score = 0

while True:
    largest_block_group = find_largest_block_group()
    if not largest_block_group:
        break

    score += len(largest_block_group) ** 2
    for y, x in largest_block_group:
        matrix[y][x] = 7

    gravity()
    matrix = rotate_90()
    gravity()

print(score)
