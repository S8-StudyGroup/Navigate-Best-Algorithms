# [BOJ] 1520. 내리막길
# 소요 시간 : 60분

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# 시작 지점(x, y), 이동 지점(xt, yt)
def dfs(x, y):
    # 끝에 도달
    if x == M - 1 and y == N - 1:
        return 1
    # 방문했다면 그 위치의 경우의 수 가져오기
    if dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    for d in range(4):
        ni = x + di[d]
        nj = y + dj[d]
        if 0 <= ni < M and 0 <= nj < N:
            if board[ni][nj] < board[x][y]:
                cnt += dfs(ni, nj)
    dp[x][y] = cnt
    return dp[x][y]


print(dfs(0, 0))
