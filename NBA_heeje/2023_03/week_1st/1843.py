# [Programmers] 1843. 사칙연산
# 소요 시간 : 60분(시간 초과)

# 설명 준비해가기

import math

INF = math.inf

def solution(arr):

    n = len(arr) // 2 + 1
    MAX_DP = [[-INF for _ in range(n)] for _ in range(n)]
    MIN_DP = [[INF for _ in range(n)] for _ in range(n)]

    for i in range(n):
        MAX_DP[i][i] = int(arr[i * 2])
        MIN_DP[i][i] = int(arr[i * 2])

    for step in range(1, n):
        for i in range(n - step):
            j = i + step
            for k in range(i, j):
                if arr[k * 2 + 1] == "+":
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k + 1][j])
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] + MIN_DP[k + 1][j])
                elif arr[k * 2 + 1] == "-":
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] - MIN_DP[k + 1][j])
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] - MAX_DP[k + 1][j])
    return MAX_DP[0][-1]

print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))