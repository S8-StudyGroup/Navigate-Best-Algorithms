# [BOJ] 11726. 2xn 타일링
# 소요 시간 : 50분
factorials = [1, 1]


def factorial(n):
    if n < 2:
        return factorials[n]
    if len(factorials) >= n+1:
        return factorials[n]
    factorials.append(n * factorial(n-1))
    return factorials[n]


def combination(n, m):
    return factorial(n) // (factorial(m) * factorial(n-m))


N = int(input())
ans = 0
for i in range(N // 2 + 1):
    two = i
    one = N - 2 * two
    ans += combination(two + one, two)

print(ans % 10007)
