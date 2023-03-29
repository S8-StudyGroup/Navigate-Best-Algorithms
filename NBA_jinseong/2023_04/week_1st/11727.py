# [BOJ] 11727. 2xn 타일링 2
# 소요 시간 : 40분

N = int(input())

answer = [0, 1, 3]

for i in range(3, N + 1):
    answer.append(((answer[i-2] * 2) % 10007 + answer[i-1] % 10007) % 10007)

print(answer[N])