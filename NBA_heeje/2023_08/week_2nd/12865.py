# [BOJ] 12865. 평범한 배낭
# 소요 시간 : 60분

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for i in range(N):
    for j in range(K, 0, -1):  # 무게 제한에서부터 역순으로 탐색
        if things[i][0] <= j:
            dp[j] = max(things[i][1] + dp[j - things[i][0]], dp[j])

# for i in range(N):
#     for j in range(1, K + 1):
#         if things[i][0] > j: continue
#         dp[j] = max(things[i][1] + dp[j - things[i][0]], dp[j])

print(dp[-1])