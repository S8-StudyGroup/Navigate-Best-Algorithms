# [BOJ] 2096. 내려가기
# 소요 시간 : 00분

n = int(input())

max_dp = min_dp = list(map(int, input().split()))

for _ in range(1, n):
    a, b, c = map(int, input().split())

    max_dp = [
        max(max_dp[:2]) + a,
        max(max_dp) + b,
        max(max_dp[1:]) + c
    ]

    min_dp = [
        min(min_dp[:2]) + a,
        min(min_dp) + b,
        min(min_dp[1:]) + c
    ]

max_value = max(max_dp)
min_value = min(min_dp)

print(max_value, min_value)
