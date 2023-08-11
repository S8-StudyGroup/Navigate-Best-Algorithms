# [BOJ] 1149. RGB거리
# 소요 시간 : 10분

import sys
input = sys.stdin.readline

N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(2)]

for house in houses:
    dp[1][0] = house[0] + min(dp[0][1], dp[0][2])
    dp[1][1] = house[1] + min(dp[0][0], dp[0][2])
    dp[1][2] = house[2] + min(dp[0][0], dp[0][1])
    dp[0], dp[1] = dp[1], dp[0]

print(min(dp[0]))