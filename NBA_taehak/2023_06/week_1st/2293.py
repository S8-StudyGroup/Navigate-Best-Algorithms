# [BOJ] 2293. 동전 1
# 소요 시간 : 00분
import sys

input = sys.stdin.readline

coin_cnt, target = map(int, input().split())
coins = list(int(input()) for _ in range(coin_cnt))

dp = [0] * (target+1)
dp[0] = 1

for coin in coins:
    for num in range(coin, target + 1):
        dp[num] += dp[num-coin]

print(dp[target])