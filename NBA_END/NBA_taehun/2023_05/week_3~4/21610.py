# [BOJ] 21610. 마법사 상어와 비바라기
# 소요 시간 : 00분

import sys

input = sys.stdin.readline

N, M =map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
info = [list(map(int, input().strip().split())) for _ in range(M)]

table = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
cloud = [[N-1,0], [N-1,1], [N-2,0], [N-2,1]]

total = set()
for r in range(N):
    for c in range(N):
        total.add((r,c))

for d, s in info:
    # 구름 이동    
    temp_cloud = set()
    for cloud_r, cloud_c in cloud:
        nr, nc = (cloud_r + table[d][0] * s) % N, (cloud_c + table[d][1] * s) % N
        temp_cloud.add((nr, nc))

    # 비 내림
    for cloud_r, cloud_c in temp_cloud:
        board[cloud_r][cloud_c] += 1

    # 대각선 검사
    for cloud_r, cloud_c in temp_cloud:
        cnt = 0
        for i in range(2, 9, 2):
            nr = cloud_r+table[i][0]
            nc = cloud_c+table[i][1]

            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] > 0:
                cnt += 1
        board[cloud_r][cloud_c] += cnt

    # 나머지 칸에서 구름 생성
    cloud = []

    for r in range(N):
        for c in range(N):
            if board[r][c] >= 2 and (r, c) not in temp_cloud:
                board[r][c] -= 2
                cloud.append([r, c])
    
print(sum(map(lambda x: sum(x), board)))



