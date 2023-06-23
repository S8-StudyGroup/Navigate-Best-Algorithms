# [BOJ] 2156. 포도주 시식
# 소요 시간 : 20분

import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]
dp[0][1] = wines[0]

for i in range(1, n):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + wines[i]
    dp[i][2] = dp[i - 1][1] + wines[i]

print(max(dp[-1]))