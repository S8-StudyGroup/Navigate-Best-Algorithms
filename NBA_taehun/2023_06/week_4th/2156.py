# [BOJ] 2156. 포도주 시식
# 소요 시간 : 00분

import sys

input = sys.stdin.readline

N = int(input().strip())
cups = [int(input().strip()) for _ in range(N)]

dp = [0] * N

dp[0] = cups[0]

# 컵이 2개 미만인 경우 체크
if N > 1:
    dp[1] = cups[0] + cups[1]

# 컵이 3개 미만인 경우 체크
if N > 2:
    dp[2] = max(cups[2] + cups[1], cups[2] + cups[0], dp[1])

# 나올 수 있는 경우의 수 비교
for i in range(3, N):
    dp[i] = max(dp[i - 1], dp[i - 3] + cups[i - 1] + cups[i], dp[i - 2] + cups[i])

print(dp[N - 1])
