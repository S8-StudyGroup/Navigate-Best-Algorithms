# [BOJ] 11727. 2xn 타일링 2
# 소요 시간 : 90분

"""
답 봄
열받는다.
"""

import sys

input = sys.stdin.readline

N = int(input().strip())

dp = [0,1,3] 
if N <= 2:
    print(dp[N])
else:
    now = 3
    old = 1
    for i in range(3, N+1):
        now, old = now + old*2, now
    print(now%10007)