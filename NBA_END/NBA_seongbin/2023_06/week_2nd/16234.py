# [BOJ] 16234. 인구 이동
# 소요 시간 : 00분
import sys
from collections import deque
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def bfs(r, c):
    queue = deque([(r, c)])
    union = [(r, c)]
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(matrix[nr][nc] - matrix[r][c]) <= R:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    union.append((nr, nc))

    return union


N, L, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

# 인구 이동이 없는 경우까지 반복
while True:
    visited = [[False] * N for _ in range(N)]
    union_list = []

    # 배열을 돌며 인구 이동이 가능한 국가 연결
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                union = bfs(r, c)
                union_list.append(union)

    # 인구 이동이 없을 경우 종료
    if len(union_list) == N**2:
        break

    # 인구 이동
    for union in union_list:
        population = sum(matrix[r][c] for r, c in union) // len(union)

        for r, c in union:
            matrix[r][c] = population

    # 하루 증가
    answer += 1

print(answer)
