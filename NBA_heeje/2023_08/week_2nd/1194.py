# [BOJ] 1194. 달이 차오른다, 가자.
# 소요 시간 : 70분

from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    sy, sx = start
    visited = set()
    visited.add((sy, sx, 0))
    queue = deque()
    queue.append((sy, sx, 0, 0))

    while queue:
        y, x, keys, time = queue.popleft()

        if maze[y][x] == "1":
            return time

        for dy, dx in DIR:
            ny, nx = y + dy, x + dx
            if in_range(ny, nx) and (ny, nx, keys) not in visited and maze[ny][nx] != "#":
                if maze[ny][nx] in KEYS:
                    if keys & (1 << (ord(maze[ny][nx]) - 97)) == 0:
                        queue.append((ny, nx, keys + (1 << ord(maze[ny][nx]) - 97), time + 1))
                        visited.add((ny, nx, keys + (1 << ord(maze[ny][nx]) - 97)))
                    else:
                        queue.append((ny, nx, keys, time + 1))
                        visited.add((ny, nx, keys))
                elif maze[ny][nx] in DOORS and keys & (1 << (ord(maze[ny][nx]) - 65)) != 0:
                    queue.append((ny, nx, keys, time + 1))
                    visited.add((ny, nx, keys))
                elif maze[ny][nx] == "." or maze[ny][nx] == "1":
                    queue.append((ny, nx, keys, time + 1))
                    visited.add((ny, nx, keys))

    return -1

def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


N, M = map(int, input().split())
maze = []
KEYS = ["a", "b", "c", "d", "e", "f"]
DOORS = ["A", "B", "C", "D", "E", "F"]
DIR = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for i in range(N):
    row = list(input())
    for j in range(M):
        if row[j] == "0":
            start = (i, j)
            row[j] = "."
    maze.append(row)

print(bfs(start))

