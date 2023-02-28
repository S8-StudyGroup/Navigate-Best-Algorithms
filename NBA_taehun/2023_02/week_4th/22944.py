# [BOJ] 22944. 죽음의 비
# 소요 시간 : 00분

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    dq = deque([])

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, H, D = map(int, input().strip().split())

map = [input() for _ in range(N)]

start = (0,0)
for r in range(N):
    for c in range(N):
        if map[r][c] == "S":
            start = (r, c)

bfs()