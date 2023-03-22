# [BOJ] 11726. 2xn 타일링
# 소요 시간 : 10분

n = int(input())
dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 1

for d in range(2, n + 1):
    dp[d] = (dp[d - 2] + dp[d - 1]) % 10007

print(dp[n])
