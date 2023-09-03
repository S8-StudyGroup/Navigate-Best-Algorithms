# [BOJ] 17822. 원판 돌리기
# 소요 시간 : 00분

from collections import deque
import sys
input = sys.stdin.readline
sum_boards = 0

N, M, T = map(int, input().split())
boards = [deque(map(int, input().split())) for _ in range(N)]
cnt_num = N * M

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for _ in range(T):
    x, d, k = map(int, input().split())
    mx = x
    while mx - 1 < len(boards):
        boards[mx - 1].rotate(k if d == 0 else -k)
        mx += x

    if cnt_num == 0: continue
    for dy, dx in direction:
        