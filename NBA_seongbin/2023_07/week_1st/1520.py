# [BOJ] 1520. 내리막길
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(row, col):

    if dp[row][col] != -1:
        return dp[row][col]

    if row == n - 1 and col == m - 1:
        dp[row][col] = 1
        return dp[row][col]

    count = 0
    for dr, dc in dir:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] < matrix[row][col]:
            count += dfs(nr, nc)

    dp[row][col] = count
    return dp[row][col]


result = dfs(0, 0)
print(result)
