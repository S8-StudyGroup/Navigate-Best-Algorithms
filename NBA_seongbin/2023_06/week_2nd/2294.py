# https: // www.acmicpc.net/problem/2294
# [BOJ] 2294. 동전 2
# 소요 시간 : 00분

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)

for i in range(1, k + 1):
    temp = []

    for coin in coin_list:
        if i - coin >= 0 and dp[i - coin] != -1:
            temp.append(dp[i - coin] + 1)

    if len(temp) == 0:
        dp[i] = -1

    else:
        dp[i] = min(temp)

print(dp[k])
