# [BOJ] 12865. 평범한 배낭
# 소요 시간 : 60분

N, K = map(int, input().split())
things = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for i in range(N):
    for j in range(K + 1):
        if things[i][0] > j: continue
        dp[j] = max(things[i][1] + dp[j - things[i][0]], dp[j])

print(dp[-1])