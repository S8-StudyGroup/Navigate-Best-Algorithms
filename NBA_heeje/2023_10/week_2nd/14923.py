# [BOJ] 14923. 미로 탈출
# 소요 시간 : 00분

import sys
input = sys.stdin.readline


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def dfs(y, x, is_used):
    global answer
    if answer != 0: return
    if y == Ey and x == Ex:
        answer = visited[Ey][Ex] - 1
        return
    
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if in_range(ny, nx) and visited[ny][nx] == 0:
            if matrix[ny][nx] == 1 and not is_used:
                matrix[ny][nx] = 0
                visited[ny][nx] = visited[y][x] + 1
                dfs(ny, nx, True)
                visited[ny][nx] = 0
                matrix[ny][nx] = 1
            elif matrix[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                dfs(ny, nx, is_used)
                visited[ny][nx] = 0


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
Hy, Hx = map(int, input().split())
Hy, Hx = Hy - 1, Hx - 1
Ey, Ex = map(int, input().split())
Ey, Ex = Ey - 1, Ex - 1
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = 0

visited[Hy][Hx] = 1
dfs(Hy, Hx, False)

print(answer)