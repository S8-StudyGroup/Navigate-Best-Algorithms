# [BOJ] 16926. 배열 돌리기 1
# 소요 시간 : 20분

import sys
from collections import deque

input = sys.stdin.readline


def rotate(y: int, x: int) -> None:
    """
    y, x를 좌상단 시작점으로 잡고 테두리를 회전시키는 함수
    """
    border_list = []
    for d in range(4):
        while (
            0 <= y + dy[d] < N
            and 0 <= x + dx[d] < M
            and answer[y + dy[d]][x + dx[d]] == 0
        ):
            y, x = y + dy[d], x + dx[d]
            border_list.append(matrix[y][x])

    cnt = R % (((N - y * 2 - 1) + (M - x * 2 - 1)) * 2)
    border_deque = deque(border_list[-cnt:] + border_list[:-cnt])

    for d in range(4):
        while (
            0 <= y + dy[d] < N
            and 0 <= x + dx[d] < M
            and answer[y + dy[d]][x + dx[d]] == 0
        ):
            y, x = y + dy[d], x + dx[d]
            answer[y][x] = border_deque.popleft()


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

N, M, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * M for _ in range(N)]

for i in range(min(M, N) // 2):
    rotate(i, i)

for i in range(N):
    print(*answer[i], sep=" ")
