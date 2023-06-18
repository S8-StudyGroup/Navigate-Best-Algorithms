# [BOJ] 1890. 점프
# 소요 시간 : 00분
size = int(input())
board = [list(map(int, input().split())) for _ in range(size)]
dp = [[0] * size for _ in range(size)]
dp[0][0] = 1

for r in range(size):
    for c in range(size):
        
        if r == size - 1 and c == size - 1:
            print(dp[r][c])
            break
        
        if dp[r][c] == 0:
            continue

        jump = board[r][c]

        if r + jump < size:
            dp[r + jump][c] += dp[r][c]

        if c + jump < size:
            dp[r][c + jump] += dp[r][c]
        