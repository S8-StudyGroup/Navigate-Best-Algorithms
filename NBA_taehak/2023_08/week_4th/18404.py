# [BOJ] 18404. 현명한 나이트
# 소요 시간 : 00분
from collections import deque

# Input
size, target_cnt = map(int, input().split())
kr, kc = map(int, input().split())
targets = [tuple(map(int, input().split())) for _ in range(target_cnt)]

# bfs
graph = [[-1]*size for _ in range(size)]
delta = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

def bfs(r, c):
    que = deque()
    que.append((r, c))
    graph[r][c] = 0

    while que:
        r, c = que.popleft()
        for dr, dc in delta:
            nr, nc = r+dr, c+dc
            if 0 <= nr < size and 0 <= nc < size and graph[nr][nc] == -1:
                que.append((nr, nc))
                graph[nr][nc] = graph[r][c]+1

bfs(kr-1, kc-1)

# Output
answer = []
for r, c in targets:
    answer.append(graph[r-1][c-1])
print(*answer)