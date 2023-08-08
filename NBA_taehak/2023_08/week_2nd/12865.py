# [BOJ] 12865. 평범한 배낭
# 소요 시간 : 00분

# Input
cnt, limit = map(int, input().split())
stuffs = [tuple(map(int, input().split())) for _ in range(cnt)]

# dp
dp = [[0] * (limit + 1) for _ in range(cnt + 1)]
for s in range(1, cnt + 1):
    for d in range(1, limit + 1):
        w, v = stuffs[s - 1]
        if d < w:
            dp[s][d] = dp[s - 1][d]
        else: 
            dp[s][d] = max(dp[s - 1][d], v + dp[s - 1][d - w])

# Output
print(dp[-1][-1])