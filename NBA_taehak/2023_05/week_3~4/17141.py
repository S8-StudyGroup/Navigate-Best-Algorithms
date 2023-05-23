# [BOJ] 17141. 연구소 2
# 소요 시간 : 00분

# 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸이다.
# M(1 ≤ M ≤ 10)
# 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.

from itertools import combinations
from collections import deque


def inrange(r, c, size):
    return 0 <= r < size and 0 <= c < size


INF = 1e9
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
def bfs(case, size, spreadable):
    visited = [[False] * size for _ in range(size)]
    que = deque(case)
    time = -1
    spread = 0

    while que:
        cycle_cnt = len(que)
        spread += cycle_cnt
        time += 1

        for _ in range(cycle_cnt):
            r, c = que.popleft()
            visited[r][c] = True

            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if inrange(nr, nc, size) and area[nr][nc] != 1 and (nr, nc) not in que and not visited[nr][nc]:
                    que.append((nr, nc))
    
    if spread != spreadable:
        return INF

    return time


size, virus_cnt = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(size)]

spreadable = 0
virusable = []
for r in range(size):
    for c in range(size):
        if area[r][c] == 2:
            virusable.append((r, c))
        if area[r][c] != 1:
            spreadable += 1
  
answer = INF
for case in combinations(virusable, virus_cnt):

    answer = min(bfs(case, size, spreadable), answer)

if answer == INF:
    print(-1)
else:
    print(answer)