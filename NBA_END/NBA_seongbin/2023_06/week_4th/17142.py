# [BOJ] 17142. 연구소 3
# 소요 시간 : 00분
import sys
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
disabled_virus = []
min_time = 10e9

for row in range(N):
    for col in range(N):
        if matrix[row][col] == 2:
            disabled_virus.append((row, col, 4))


def spread_virus(virus):
    queue = deque()

    for row, col, time in virus:
        queue.append((row, col, time))
        visited[row][col] = 3

    while queue:
        row, col, time = queue.popleft()

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and matrix[nr][nc] != 1:
                if matrix[nr][nc] == 0:
                    visited[nr][nc] = time
                    queue.append((nr, nc, time + 1))
                elif matrix[nr][nc] == 2:
                    visited[nr][nc] = 3
                    queue.append((nr, nc, time + 1))

    result = 0
    for row in range(N):
        for col in range(N):
            if matrix[row][col] == 0 and not visited[row][col]:
                return 10e9
            if matrix[row][col] != 1:
                result = max(result, visited[row][col])

    return result - 3


for virus in combinations(disabled_virus, M):
    visited = [[0] * N for _ in range(N)]
    result = spread_virus(virus)
    min_time = min(min_time, result)

print(min_time if min_time != 10e9 else -1)
