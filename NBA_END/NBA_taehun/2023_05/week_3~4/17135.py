# [BOJ] 17135. 캐슬 디펜스
# 소요 시간 : 00분

import sys
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline

# 거리 구하기
def diff(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# 제거할 수 있는 적 찾기
def check(archer, target_r):
    targets = []
    end = target_r-D if target_r-D >= -1 else -1
    for r in range(target_r, end, -1):
        for c in range(M):
            if temp_board[r][c] == 1:
                d = diff(archer, (r, c))
                if d <= D:
                    targets.append((d,(r,c)))
    # 가장 가까운 적중에 가장 왼쪽에 있는 적 찾기
    if targets:
        target.add(sorted(targets, key=lambda x:(x[0], x[1][1]))[0][1])

N, M, D = map(int, input().strip().split())

board = [list(map(int, input().strip().split())) for _ in range(N)]

max_result = 0

for case in combinations(range(M), 3):
    result = 0
    temp_board = deepcopy(board)
    for r in range(N, 0, -1):
        target = set()
        for c in case:
            check((r,c), r-1)
        result += len(target)
        # 제거한 적 표시
        for r, c in target:
            temp_board[r][c] = 0

    max_result = max(max_result, result)

print(max_result)