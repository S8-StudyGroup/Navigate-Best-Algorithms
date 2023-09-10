# [BOJ] 11052. 카드 구매하기
# 소요 시간 : 00분

# 해당 카드팩을 사용하지 않는 경우와
# 해당 카드팩을 최대치로 사용하는 경우를 비교

N = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(2, N + 1):
    dp[i] = max(dp[j] + dp[i - j] for j in range(i // 2 + 1))

print(dp[N])