# [BOJ] 1149. RGB거리
# 소요 시간 : 10분

import sys
input = sys.stdin.readline

N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]
dp = [0, 0, 0]

for house in houses:
    dp[0], dp[1], dp[2] = house[0] + min(dp[1:]), house[1] + min(dp[0], dp[2]), house[2] + min(dp[:2])

print(min(dp))
