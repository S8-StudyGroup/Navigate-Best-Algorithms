# [BOJ] 2146. 다리 만들기
# 소요 시간 : 00분
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

answer = -float("inf")
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
island = {}


def island_naming():
    """_summary_
    지도상 섬의 이름 짓고 island에 좌표 저장
    섬의 개수 반환
    """
    def island_union(row: int, col: int):
        """_summary_
        dfs로 섬 판별
        Args:
            row (int): 행
            col (int): 열
        """
        island[cur_island_name].append((row, col, 0))
        matrix[row][col] = cur_island_name
        visited[row][col] = True

        for dr, dc in delta:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 1 and not visited[nr][nc]:
                island_union(nr, nc)

    visited = [[False] * n for _ in range(n)]
    cur_island_name = 0

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 1 and not visited[row][col]:
                cur_island_name += 1
                island[cur_island_name] = deque([])
                island_union(row, col)

    return cur_island_name


def find_min_bridge(island_name: int):
    """_summary_
    각 섬을 돌며 다른 섬과 연결할 수 있는 다리의 최소 길이 반환
    """
    queue = island[island_name]
    visited = [[False] * n for _ in range(n)]

    while queue:
        row, col, bridge_length = queue.popleft()

        for dr, dc in delta:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] != island_name and not visited[nr][nc]:

                if matrix[nr][nc] != 0:
                    return bridge_length

                visited[nr][nc] = True
                queue.append((nr, nc, bridge_length - 1))


island_cnt = island_naming()

for island_name in range(1, island_cnt + 1):
    answer = max(answer, find_min_bridge(island_name))

print(-answer)
