# [BOJ] 10870. 피보나치 수 5
# 소요 시간 : 00분

n = int(input())

memo = [0, 1]
for _ in range(n - 1):
    memo.append(memo[-2] + memo[-1])

print(memo[n])