# [BOJ] 2579. 계단 오르기
# 소요 시간 : 00분

n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp = [0] * n

if n == 1:
    print(stairs[0])
else:
    dp[0], dp[1] = stairs[0], stairs[0] + stairs[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i-1] + stairs[i])

    print(dp[-1])
