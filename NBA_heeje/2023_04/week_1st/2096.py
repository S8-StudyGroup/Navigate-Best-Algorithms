# [BOJ] 2096. 내려가기
# 소요 시간 : 00분

import sys
input = sys.stdin.readline

N = int(input())

# pre_min_dp = [0] * 3
# pre_max_dp = [0] * 3

min_dp = list(map(int, input().split()))
max_dp = min_dp[:]

for _ in range(1, N):
    # pre_min_dp, pre_max_dp = min_dp, max_dp
    a, b, c = map(int, input().split())
    min_dp = [a + min(min_dp[0:2]), b + min(min_dp), c + min(min_dp[1:])]
    max_dp = [a + max(max_dp[0:2]), b + max(max_dp), c + max(max_dp[1:])]

print(max(max_dp), min(min_dp))