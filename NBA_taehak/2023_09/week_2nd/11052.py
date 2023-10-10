# [BOJ] 11052. 카드 구매하기
# 소요 시간 : 00분

# Input
target = int(input())
prices = [0] + list(map(int, input().split()))

# dp
dp = [0] * (target + 1)

for idx in range(target + 1):
    for p in range(1, idx + 1):
        dp[idx] = max(dp[idx], prices[p] + dp[idx-p])

# Output
print(dp[target])
