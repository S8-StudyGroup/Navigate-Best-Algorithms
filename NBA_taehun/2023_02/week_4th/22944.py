# [BOJ] 22944. 죽음의 비
# 소요 시간 : 00분

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    dq = deque([(start,  0, H, 0)])
    maps[start[0]][start[1]] = H
    while dq:
        start, cnt, h, ud = dq.popleft()
        r, c = start
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and (nr ,nc):
                nv = maps[nr][nc]

                if nv == "E":
                    print(cnt + 1)
                    return

                temp_h, temp_ud = h, ud
                
                if nv == "U":
                    temp_ud = D
                    maps[nr][nc] = temp_h

                if temp_ud:
                    temp_ud -= 1
                else:
                    temp_h -= 1

                if temp_h == 0:
                    continue
                
                if nv == "U" or nv < temp_h:
                    maps[nr][nc] = temp_h
                    dq.append(((nr, nc), cnt + 1, temp_h, temp_ud))
    print(-1)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, H, D = map(int, input().strip().split())

maps = [list(map(lambda x: 0 if x == "." else str(x), input().strip())) for _ in range(N)]

start = (0,0)
for r in range(N):
    for c in range(N):
        if maps[r][c] == "S":
            start = (r, c)

bfs(start)
