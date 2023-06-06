# [BOJ] 2293. 동전 1
# 소요 시간 : 40분
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
dp = [1] + [0] * k

for coin in coin_list:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

answer = dp[k]

print(answer)
