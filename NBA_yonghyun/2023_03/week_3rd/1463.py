# [BOJ] 1463. 1로 만들기
# 소요 시간 : 00분

n = int(input())

if n == 1:
    print(0)

elif n == 2 or n == 3:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[2], dp[3] = 1, 1

    for num in range(3, n + 1):
        dp[num] = 1 + dp[num - 1]
        if num % 3 == 0:
            dp[num] = min(1 + dp[num // 3], dp[num])
        if num % 2 == 0:
            dp[num] = min(1 + dp[num // 2], dp[num])

    print(dp[n])