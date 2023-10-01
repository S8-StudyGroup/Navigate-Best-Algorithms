# [BOJ] 1149. RGB거리
# 소요 시간 : 30분
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
colors = [list(map(int, input().split())) for _ in range(n)]
r, g, b = colors[0]
dp = [[r, g, b]] + [[0, 0, 0] for _ in range(n - 1)]

for i in range(1, n):
    dp[i][0] = colors[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = colors[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = colors[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[-1]))
