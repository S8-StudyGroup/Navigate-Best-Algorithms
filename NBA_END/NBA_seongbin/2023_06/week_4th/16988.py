# [BOJ] 16988. Baaaaaaaaaduk2 (Easy)
# 소요 시간 : 00분
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
answer = 0
total = 0
empty_spaces = []

for row in range(N):
    for col in range(M):
        if matrix[row][col] == 0:
            empty_spaces.append((row, col))
        elif matrix[row][col] == 2:
            total += 1


def tsumego(new_matrix):
    """바둑2의 사활문제

    new_matrix를 탐색하며 잡을 수 있는 바둑돌의 수를 반환한다.
    """
    union = 0
    visited = [[False] * M for _ in range(N)]

    for row in range(N):
        for col in range(M):
            if new_matrix[row][col] == 2 and not visited[row][col]:
                cur_union = 1
                can_kill = True
                queue = deque([(row, col)])
                visited[row][col] = True

                while queue:
                    r, c = queue.popleft()

                    for dr, dc in delta:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                            if new_matrix[nr][nc] == 2:
                                cur_union += 1
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                            elif new_matrix[nr][nc] == 1:
                                visited[nr][nc] = True
                            elif new_matrix[nr][nc] == 0:
                                can_kill = False

                if can_kill:
                    union += cur_union

    return union


if len(empty_spaces) <= 2:
    print(total)
else:
    for empty_space in combinations(empty_spaces, 2):
        new_matrix = [row[:] for row in matrix]
        for row, col in empty_space:
            new_matrix[row][col] = 1

        union = tsumego(new_matrix)
        answer = max(answer, union)

    print(answer)
