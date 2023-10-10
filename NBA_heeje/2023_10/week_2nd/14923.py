# [BOJ] 14923. 미로 탈출
# 소요 시간 : 00분

from collections import deque
import sys
input = sys.stdin.readline


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    queue = deque()
    queue.append((Hy, Hx, 0, 1))
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    visited[Hy][Hx][1] = True

    while queue:
        y, x, cnt, magic = queue.popleft()

        if y == Ey and x == Ex:
            return cnt
        
        for dy, dx in direction:
            ny, nx = y + dy, x + dx


            if in_range(ny, nx):
                if matrix[ny][nx] == 1 and magic == 1:
                    visited[ny][nx][0] = True
                    queue.append((ny, nx, cnt + 1, 0))
                elif matrix[ny][nx] == 0 and not visited[ny][nx][magic]:
                    visited[ny][nx][magic] = True
                    queue.append((ny, nx, cnt + 1, magic))

    return -1

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
Hy, Hx = map(int, input().split())
Ey, Ex = map(int, input().split())
Hy, Hx, Ey, Ex = Hy - 1, Hx - 1, Ey - 1, Ex - 1
matrix = [list(map(int, input().split())) for _ in range(N)]

print(bfs())