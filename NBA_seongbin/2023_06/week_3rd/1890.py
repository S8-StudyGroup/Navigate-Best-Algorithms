# [BOJ] 1890. 점프
# 소요 시간 : 00분
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for row in range(N):
    for col in range(N):
        if row == N - 1 and col == N - 1:
            break
        if dp[row][col] > 0:
            jump = matrix[row][col]
            if row + jump < N:
                dp[row + jump][col] += dp[row][col]
            if col + jump < N:
                dp[row][col + jump] += dp[row][col]

print(dp[-1][-1])
