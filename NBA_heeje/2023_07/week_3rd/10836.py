# [BOJ] 10836. 여왕벌
# 소요 시간 : 40분

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [[1] * M for _ in range(M)]
grow_info = [0] * (2 * M - 1)
for _ in range(N):
    cnt_zero, cnt_one, cnt_two = list(map(int, input().split()))
    for i in range(cnt_zero, cnt_zero + cnt_one):
        grow_info[i] += 1
    for i in range(cnt_zero + cnt_one, 2 * M - 1):
        grow_info[i] += 2

for i in range(M):
    matrix[M - i - 1][0] += grow_info[i]
for i in range(M, len(grow_info)):
    matrix[0][i - M + 1] += grow_info[i]

for i in range(1, M):
    for j in range(1, M):
        matrix[i][j] += matrix[0][j] - 1

for i in range(M):
    print(*matrix[i])