# [BOJ] 10870. 피보나치 수 5
# 소요 시간 : 00분

import sys

N = int(sys.stdin.readline())

memo = [0, 1]

if N < 2:
    print(memo[N])
else:
    for i in range(2, N+1):
        memo.append(memo[i-2] + memo[i-1])
    print(memo[-1])
