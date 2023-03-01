# [BOJ] 10870. 피보나치 수 5
# 소요 시간 : 10분

n = int(input())

dp = [0, 1]

for i in range(2, n + 1):
    new = dp[i - 2] + dp[i - 1]
    dp.append(new)

print(dp[n])