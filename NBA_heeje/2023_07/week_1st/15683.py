# [BOJ] 15683. 감시
# 소요 시간 : 20분

import sys
input = sys.stdin.readline

def dfs(c_idx, blind_spot):

    if c_idx == len(cctv_list):
        global min_blind_spot

        min_blind_spot = min(min_blind_spot, blind_spot)
        return

    y, x = cctv_list[c_idx]
    for d_list in c_dir[matrix[y][x]]:
        spot_list = []
        for d in d_list:
            ny, nx = y + dy[d], x + dx[d]
            while 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] <= 5:
                if matrix[ny][nx] == 0:
                    matrix[ny][nx] = -1
                    spot_list.append((ny, nx))
                    blind_spot -= 1
                ny, nx = ny + dy[d], nx + dx[d]
            
        dfs(c_idx + 1, blind_spot)

        for sy, sx in spot_list:
            matrix[sy][sx] = 0
            blind_spot += 1


# 상우하좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
c_dir = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
    ]

N, M = map(int, input().split())
matrix = []
cctv_list = []
blind_spot = N * M
min_blind_spot = N * M
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if 1 <= row[j] <= 6:
            if row[j] < 6:
                cctv_list.append((i, j))
            blind_spot -= 1

    matrix.append(row)

dfs(0, blind_spot)
print(min_blind_spot)