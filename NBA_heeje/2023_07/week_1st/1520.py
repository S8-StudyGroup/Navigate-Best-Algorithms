# [BOJ] 1520. 내리막길
# 소요 시간 : 90분
# 실행 시간 : 144 ms
# 메모리 : 42788 KB

import sys
input = sys.stdin.readline

def dfs(sy, sx):
    if sy == M - 1 and sx == N - 1:
        return 1
    
    if dp[sy][sx] != -1:
        return dp[sy][sx]
    
    cnt = 0
    for d in range(4):
        ny, nx = sy + dy[d], sx + dx[d]
        if 0 <= ny < M and 0 <= nx < N and matrix[sy][sx] > matrix[ny][nx]:
            cnt += dfs(ny, nx)
    
    dp[sy][sx] = cnt
    return dp[sy][sx]


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

print(dfs(0, 0))