# [BOJ] 1149. RGB거리
# 소요 시간 : 00분

# Input
house_cnt = int(input())
costs = [tuple(map(int, input().split())) for _ in range(house_cnt)]

# dp
dp = [[0, 0, 0] for _ in range(house_cnt)]
dp[0] = list(costs[0])

for idx in range(1, house_cnt):
    r0, g0, b0 = dp[idx-1]
    r, g, b = costs[idx]

    dp[idx][0] = min(g0 + r, b0 + r)
    dp[idx][1] = min(r0 + g, b0 + g)
    dp[idx][2] = min(r0 + b, g0 + b)

# Output
print(min(dp[-1]))