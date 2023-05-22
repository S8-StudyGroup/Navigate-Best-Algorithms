# [BOJ] 17141. 연구소 2
# 소요 시간 : 00분

import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int , input().strip().split())
lab = [list(map(lambda x: -1 if x == '1' else int(x) , input().strip().split())) for _ in range(N)]

table = [(-1, 0), (1, 0), (0, -1), (0, 1)]

points = []
min_count = 9999999999
flag = False

# 바이러스를 놓을 수 있는 칸 찾기
for r in range(N):
    for c in range(N):
        if lab[r][c] == 2:
            points.append((r, c, 0))
            lab[r][c] = 0

# 가능한 경우의 수 찾기
for case in combinations(points, M):
    temp_lab = deepcopy(lab)
    dq = deque(case)
    # bfs
    while dq:
        r, c, cnt = dq.popleft()
        if temp_lab[r][c] == 0 or temp_lab[r][c] > cnt:
            temp_lab[r][c] = cnt
            for dr, dc in table:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and temp_lab[nr][nc] != -1 and (nr, nc, 0) not in case:
                    dq.append((nr, nc, cnt+1))

    max_count = max(map(lambda x: max(x), temp_lab))
    zero_count = sum(map(lambda x: x.count(0), temp_lab))
    if zero_count <= M:
        min_count = min(min_count, max_count)
        flag = True

if flag:
    print(min_count)
else:
    print(-1)
