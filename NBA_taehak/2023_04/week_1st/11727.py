# [BOJ] 11727. 2xn 타일링 2
# 소요 시간 : 00분
n = int(input())
memo = [0] * 1001

memo[0] = 1
memo[1] = 1

for i in range(2, n+1):
    memo[i] = memo[i-1] + 2 * memo[i-2]

print(memo[n]%10007)