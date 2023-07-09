# [BOJ] 3678. 카탄의 개척자
# 소요 시간 : 90+분

import sys
input = sys.stdin.readline

# 방향: 우상, 좌상, 좌하, 우하, 상, 하
dy = [-1, -2, -1, 2, 1, 1]
dx = [1, 0, -1, 0, -1, 1]

matrix = [[0] * 5000 for _ in range(5000)]
matrix[2500][2500] = 1
matrix[2499][2501] = 2
matrix[2498][2500] = 3
memo = [0, 1, 2, 3]
answer = []
y, x = 2498, 2500
d = 0

c = int(input())
for _ in range(c):
    n = int(input())
    if n < len(memo):
        answer.append(memo[n])
    else:
        for _ in range(n - len(memo) + 2):
            if matrix[y + dy[d]][x + dx[d]] != 0:
                pass
