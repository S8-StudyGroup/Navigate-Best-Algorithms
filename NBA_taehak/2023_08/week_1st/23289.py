# [BOJ] 23289. 온풍기 안녕!
# 소요 시간 : 00분
from collections import defaultdict

# Input
row_size, col_size, k = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(row_size)]
wall_cnt = int(input())
wall_info = [list(map(int, input().split())) for _ in range(wall_cnt)]

# room temperature
temp = [[0] * col_size for _ in range(row_size)]


# for debug
def print_temp(ex='temp'):
    print(f'====================== < {ex} > ========================')
    for i in temp:
        print(i)


# room scan
fans = []
check_rcs = []
for r in range(row_size):
    for c in range(col_size):
        if room[r][c] == 5:
            check_rcs.append((r, c))
        elif room[r][c] > 0:
            fans.append((r, c, room[r][c]))


def check():
    for r, c in check_rcs:
        if temp[r][c] < k:
            return False
    return True


# wall 
wall = defaultdict(list)
for r, c, t in wall_info:
    rr = r-1
    cc = c-1
    if t == 0:
        wall[(rr, cc)].append((rr-1, cc))
        wall[(rr-1, cc)].append((rr, cc))
    else:
        wall[(rr, cc)].append((rr, cc+1))
        wall[(rr, cc+1)].append((rr, cc))

def air_movable(rc, next_rc):
    if wall.get(rc) and next_rc in wall.get(rc):
        return False
    return True


# delta 시계방향으로 순회
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# fan_direction (1~4) -> delta_idx (0~3)
delta_idx = {1: 1, 2: 3, 3: 0, 4: 2}


def inrange(r, c):
    return 0 <= r < row_size and 0 <= c < col_size


def turn_up(area, heat):
    for r, c in area:
        temp[r][c] += heat


def fan_working(fr, fc, fan_direction):
    dr, dc = delta[delta_idx[fan_direction]]
    dr_l, dc_l = delta[(delta_idx[fan_direction] - 1) % 4]
    dr_r, dc_r = delta[(delta_idx[fan_direction] + 1) % 4]

    # 첫번째 영역
    area = [(fr + dr, fc + dc)]
    turn_up(area, 5)

    # 나머지 영역
    for heat in range(4, 0, -1):

        next_area = []
        for r, c in area:

            # mid
            mr = r + dr
            mc = c + dc
            if inrange(mr, mc) and air_movable((r, c), (mr, mc)) and (mr, mc) not in next_area:
                next_area.append((mr, mc))
            
            # left
            lr1 = r + dr_l
            lc1 = c + dc_l
            lr2 = lr1 + dr
            lc2 = lc1 + dc
            if inrange(lr1, lc1) and air_movable((r, c), (lr1, lc1)):
                if inrange(lr2, lc2) and air_movable((lr1, lc1), (lr2, lc2)) and (lr2, lc2) not in next_area:
                    next_area.append((lr2, lc2))

            # right
            rr1 = r + dr_r
            rc1 = c + dc_r
            rr2 = rr1 + dr
            rc2 = rc1 + dc
            if inrange(rr1, rc1) and air_movable((r, c), (rr1, rc1)):
                if inrange(rr2, rc2) and air_movable((rr1, rc1), (rr2, rc2)) and (rr2, rc2) not in next_area:
                    next_area.append((rr2, rc2))
        
        turn_up(next_area, heat)
        area = next_area


def control_temp_between(r1, c1, r2, c2):
    temp1 = temp[r1][c1]
    temp2 = temp[r2][c2]
    updown = abs(temp1 - temp2) // 4

    if updown == 0:
        return 0, 0, 0
    
    if temp1 > temp2:
        return 1, -updown, updown
    elif temp1 < temp2:
        return 1, updown, -updown
    
    return 0, 0, 0


def control_temp():
    controls = []

    for r in range(row_size - 1):
        for c in range(col_size):
            if air_movable((r, c), (r+1, c)):
                go, rc, rc2 = control_temp_between(r, c, r+1, c)
                if go:
                    controls.append((r, c, rc))
                    controls.append((r+1, c, rc2))
    
    for c in range(col_size - 1):
        for r in range(row_size):
            if air_movable((r, c), (r, c+1)):
                go, rc, rc2 = control_temp_between(r, c, r, c+1)
                if go:
                    controls.append((r, c, rc))
                    controls.append((r, c+1, rc2))

    for r, c, temp_delta in controls:
        temp[r][c] += temp_delta


def temp_drop():
    for r in [0, row_size-1]:
        for c in range(col_size):
            if temp[r][c] > 0:
                temp[r][c] -= 1
    
    for c in [0, col_size-1]:
        for r in range(1, row_size-1):
            if temp[r][c] > 0:
                temp[r][c] -= 1
    

choco = 0

while choco <= 100:
    # 1
    for fr, fc, fan_direction in fans:
        fan_working(fr, fc, fan_direction)
        # print_temp(f'after fan_working : {fr}, {fc}, {fan_direction}')
    
    # 2
    control_temp()
    # print('wall:', wall)
    # print_temp('after control_temp')

    # 3
    temp_drop()
    # print_temp('after temp_drop')

    # 4
    choco += 1

    # 5
    if check():
        break

print(choco)