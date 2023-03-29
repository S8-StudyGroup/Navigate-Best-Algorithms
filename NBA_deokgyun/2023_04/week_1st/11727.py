# [BOJ] 11727. 2xn 타일링 2
# 소요 시간 : 20분

n = int(input())
memo = [1]

for i in range(1, n):
    if i % 2:
        memo.append((memo[-1] * 2 + 1) % 10007)
    else:
        memo.append((memo[-1] * 2 - 1) % 10007)

print(memo[-1])