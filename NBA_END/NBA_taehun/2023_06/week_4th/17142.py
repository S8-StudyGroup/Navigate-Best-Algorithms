# [BOJ] 17142. 연구소 3
# 소요 시간 : 80분

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def bfs(temp_lab, case):
    dq = deque(case)
    max_cnt = 0
    move_cnt = M
    for r, c in case:
        temp_lab[r][c] = 0
    while dq:
        r, c = dq.popleft()
        cnt = temp_lab[r][c]
        if cnt > max_cnt and (r, c) not in virus_points:
            max_cnt = cnt
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < N
                and 0 <= nc < N
                and lab[nr][nc] != 1
                and temp_lab[nr][nc] == -1
            ):
                temp_lab[nr][nc] = cnt + 1
                move_cnt += 1
                dq.append((nr, nc))
    if move_cnt >= null_space:
        return max_cnt
    else:
        return 999999999999


N, M = map(int, input().strip().split())
lab = [list(map(int, input().strip().split())) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
min_time = 999999999999
null_space = 0

# 바이러스 시작 위치 찾기
virus_points = set()
for r in range(N):
    for c in range(N):
        if lab[r][c] == 0:
            null_space += 1
        if lab[r][c] == 2:
            virus_points.add((r, c))
            lab[r][c] = 0

if null_space == 0:
    print(0)
else:
    null_space += len(virus_points)
    for case in combinations(virus_points, M):
        temp_lab = [[-1] * N for _ in range(N)]
        max_cnt = bfs(temp_lab, case)
        min_time = min(min_time, max_cnt)

    if min_time == 999999999999:
        print(-1)
    else:
        print(min_time)
