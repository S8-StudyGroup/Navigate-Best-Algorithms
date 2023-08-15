# [BOJ] 1149. RGB거리
# 소요 시간 : 00분

from sys import stdin
readline = stdin.readline

num = int(readline())
cost = []
for _ in range(num):
    cost.append(list(map(int, readline().split())))

for i in range(1, num):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])

print(min(cost[num - 1]))