# [BOJ] 2294. 동전 2
# 소요 시간 : 00분

n, k = map(int, input().split())

coins =[]

for i in range(n):
   coins.append(int(input().rstrip()))

dp = [10001] * (k+1)
dp[0] = 0

for coin in coins:
   for i in range(coin, k+1):
       dp[i] = min(dp[i],dp[i-coin]+1)
       
if dp[k] == 10001:
   print(-1)
else:
   print(dp[k])