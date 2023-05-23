# [BOJ] 17135. 캐슬 디펜스
# 소요 시간 : 00분
from itertools import combinations
from collections import deque
from copy import deepcopy



archer_cnt = 3
delta = [(0, -1), (-1, 0), (0, 1)]  # 좌 상 우 순서로
row_size, col_size, archer_range = map(int, input().split())
area_0 = [list(input().split()) for _ in range(row_size)]


def inrange(r, c):
    return 0 <= r < row_size and 0 <= c < col_size


def attack(time, archer_col, archer_range):
    que = deque([(row_size - 1 - time, archer_col)])
    attack_distance = 1
    while que and attack_distance <= archer_range:
        same_distance = len(que)
        for _ in range(same_distance):
            r, c = que.popleft()
            if area[r][c] == '1' and (r, c) not in hitlist:
                return (r, c)

            for dr, dc in delta:
                nr = r + dr
                nc = c + dc

                if inrange(nr, nc) and (nr, nc) not in que:
                    que.append((nr, nc))
                
        attack_distance += 1
    
    return False


max_hit = 0
for case in combinations(range(col_size), archer_cnt):
    area = deepcopy(area_0)
    hitlist = set()
    for time in range(row_size):
        hitnow = set()
        for archer_col in case:
            attack_rc = attack(time, archer_col, archer_range)
            if attack_rc:
                hitnow.add(attack_rc)
        hitlist |= hitnow

    max_hit = max(max_hit, len(hitlist))

print(max_hit)