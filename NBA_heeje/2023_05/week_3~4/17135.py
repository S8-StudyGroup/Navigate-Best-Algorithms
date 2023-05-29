# [BOJ] 17135. 캐슬 디펜스
# 소요 시간 : 60분

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

# 1. 궁수 공격
# 2. 적 이동

# 궁수가 적을 제거하는 함수
def terminate_enemy(archors):

    # 여러 궁수가 한 적을 동시에 공격할 수 있으니 set으로 설정
    terminate_enemy_set = set()
    for archor_x in archors:
        queue = deque()
        queue.append((N, archor_x))
        archor_range = 0
        while queue and archor_range < D:
            archor_range += 1
            attack_list = []
            for _ in range(len(queue)):
                y, x = queue.popleft()
                for d in range(4):
                    move_y, move_x = y + dy[d], x + dx[d]
                    if 0 <= move_y < N and 0 <= move_x < M:
                        if copied_matrix[move_y][move_x] == 1:
                            attack_list.append((move_y, move_x))
                        queue.append((move_y, move_x))
            
            # 해당 범위 내에서 공격 가능한 적이 있을 때
            if attack_list:
                sorted_attack_list = sorted(attack_list, key= lambda x: x[1])
                terminate_enemy_set.add(sorted_attack_list[0])
                break
    return list(terminate_enemy_set)

# 적들이 한 칸 아래로 이동하는 함수
def move_enemy():
    excepted_enemy = 0
    for point in copied_matrix.pop():
        if point == 1:
            excepted_enemy += 1
    copied_matrix.insert(0, [0] * M)
    return excepted_enemy
            
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M, D = map(int, input().split())
cnt_enemy = 0
max_cnt_terminated_enemy = 0

matrix = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            cnt_enemy += 1
    matrix.append(row)

# 궁수들의 자리 배치에 대한 조합
for archors in combinations(range(M), 3):

    cnt_terminated_enemy = 0
    cnt_cur_enemy = cnt_enemy
    copied_matrix = []
    for i in range(N):
        copied_matrix.append(matrix[i][:])

    # 적들이 하나라도 남아 있다면 진행
    while cnt_cur_enemy > 0:

        terminate_enemy_list = terminate_enemy(archors)
        for y, x in terminate_enemy_list:
            copied_matrix[y][x] = 0
            cnt_terminated_enemy += 1
            cnt_cur_enemy -= 1
        cnt_cur_enemy -= move_enemy()
    
    max_cnt_terminated_enemy = max(max_cnt_terminated_enemy, cnt_terminated_enemy)

print(max_cnt_terminated_enemy)