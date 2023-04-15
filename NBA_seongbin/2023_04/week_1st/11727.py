# [BOJ] 11727. 2xn 타일링 2
# 소요 시간 : 20분

a, b = 1, 1

for _ in range(int(input())-1):
    a, b = b, (2*a+b) % 10007

print(b)
