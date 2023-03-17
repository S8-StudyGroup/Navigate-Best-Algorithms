# [BOJ] 2579. 계단 오르기
# 소요 시간 : 00분

# 첫 시도 : DFS - 실패
# 원인 : 경우의 수가 너무 많음(시간 초과) - DP로 풀어야할 듯!

# import sys
# sys.setrecursionlimit(100000)

# def dfs(idx, validator, score):
#     global max_score

#     if idx == N:
#         max_score = max(max_score, score)
#         return
    
#     if validator < 2:
#         dfs(idx + 1, validator + 1, score + stairs[idx + 1])
    
#     if idx < N - 1:
#         dfs(idx + 2, 1, score + stairs[idx + 2])


# N = int(input())
# stairs = [0] + [int(input()) for _ in range(N)]
# max_score = 0
# dfs(0, 0, 0)

# print(max_score)

# ------------------------------------------------------------

# 두 번째 시도 : DP
# 방법 : 점화식 찾기
# 1. 마지막 계단을 기준으로 마지막-1 계단을 밟았을 경우
# -> 마지막-2 계단은 밟지 못함
# -> 최댓값 = 마지막-3 계단까지의 최댓값 + 마지막-1 계단 값 + 마지막 계단 값

# 2. 마지막 계단을 기준으로 마지막-1 계단을 밟지 않았을 경우
# -> 최댓값 = 마지막-2 계단까지의 최댓값 + 마지막 계단 값

import sys
input = sys.stdin.readline

N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]

if N == 1:
    print(stairs[-1])

else:
    dp = [0] * (N + 1)
    dp[1], dp[2] = stairs[1], stairs[1] + stairs[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i-3] + stairs[i - 1] + stairs[i], dp[i-2] + stairs[i])

    print(dp[-1])