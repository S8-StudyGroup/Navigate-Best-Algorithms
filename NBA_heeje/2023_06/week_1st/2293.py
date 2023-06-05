# [BOJ] 2293. 동전 1
# 소요 시간 : 20분

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(n)]
dp = [1] + [0] * k

def sol():
    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]
        print(dp)

    print(dp[k])

sol()