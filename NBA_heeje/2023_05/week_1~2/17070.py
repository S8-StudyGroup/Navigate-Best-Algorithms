# [BOJ] 17070. 파이프 옮기기 1
# 소요 시간 : 20분

def dfs(y, x, dir):
    if y == N - 1 and x == N - 1:
        global cnt
        cnt += 1
        return
    
    if x + 1 < N and y + 1 < N and matrix[y][x + 1] == 0 and matrix[y + 1][x] == 0 and matrix[y + 1][x + 1] == 0:
        dfs(y + 1, x + 1, 1)

    if dir == 0:
        if x + 1 < N and matrix[y][x + 1] == 0:
            dfs(y, x + 1, 0)
    
    if dir == 1:
        if x + 1 < N and matrix[y][x + 1] == 0:
            dfs(y, x + 1, 0)
        if y + 1 < N and matrix[y + 1][x] == 0:
            dfs(y + 1, x, 2)
    
    if dir == 2:
        if y + 1 < N and matrix[y + 1][x] == 0:
            dfs(y + 1, x, 2)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 0)

print(cnt)