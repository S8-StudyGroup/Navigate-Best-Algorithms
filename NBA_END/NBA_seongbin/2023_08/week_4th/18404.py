# [BOJ] 18404. 현명한 나이트
# 소요 시간 : 00분
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
r, c = map(int, input().split())
matrix = [[0] * n for _ in range(n)]
delta = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]


def bfs():
    """_summary_
    matrix에는 knight의 이동 최단거리가 저장된다.
    """
    global matrix
    visited = set()
    queue = deque([(r - 1, c - 1, 0)])
    visited.add((r - 1, c - 1))

    while queue:
        row, col, deep = queue.popleft()
        matrix[row][col] = deep

        for dr, dc in delta:
            nr, nc = row + dr, col + dc

            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, deep + 1))


bfs()

for _ in range(m):
    r, c = map(int, input().split())
    print(matrix[r - 1][c - 1])
