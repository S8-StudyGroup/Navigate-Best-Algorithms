# [BOJ] 11052. 카드 구매하기
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

n = int(input())
li = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, i+1):
    dp[i] = max(dp[i], dp[i-j]+li[j])

print(dp[-1])
