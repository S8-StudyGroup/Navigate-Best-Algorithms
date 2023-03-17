# [BOJ] 2579. 계단 오르기
# 소요 시간 : 00분

import sys

input = sys.stdin.readline

n = int(input().strip())

stairs = [int(input().strip()) for _ in range(n)]

if n <= 3:
    print(sum(stairs))
else:
    dp = [0] * (n)

    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

    for i in range(2,n):
        dp[i] = max(dp[i-3] + stairs[i] + stairs[i-1], dp[i-2] + stairs[i])

    print(dp[n-1])
