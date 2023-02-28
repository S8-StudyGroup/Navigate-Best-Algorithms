# [BOJ] 22944. 죽음의 비
# 소요 시간 : 00분

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    dq = deque([(*start,  0, H, 0)])
    while dq:
        r, c, cnt, h, ud = dq.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                nv = map[nr][nc]
                temp_h, temp_ud = h, ud
                if type(nv) == int:
                    if temp_h + temp_ud <= nv:
                        continue
                    map[nr][nc] = temp_h + temp_ud
                    if temp_ud:
                        temp_ud -= 1
                    else:
                        temp_h -= 1
                elif nv == "U":
                    temp_ud = D - 1
                elif nv == "E":
                    return cnt + 1
                if temp_h > 0:
                    dq.append(((nr, nc), cnt + 1, temp_h, temp_ud))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, H, D = map(int, input().strip().split())

map = [list(map(lambda x: 0 if x == "." else str(x), input().strip())) for _ in range(N)]

start = (0,0)
for r in range(N):
    for c in range(N):
        if map[r][c] == "S":
            start = (r, c)

count = bfs(start)
if not count:
    count = -1
print(count)

