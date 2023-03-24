# [BOJ] 11726. 2xn 타일링
# 소요 시간 : 00분
size = int(input())
result = [0, 1, 2]

for idx in range(3, size + 1):
    result.append(result[-1] + result[-2])
print(result[size]%10007)