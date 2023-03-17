# [BOJ] 17144. 미세먼지 안녕!
# 소요 시간 : 00분
from collections import deque

row_size, col_size, times = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(row_size)]


# 범위 안?
def inrange(r, c):
    if 0 <= r < row_size and 0 <= c < col_size and room[r][c] != -1:
        return True
    else:
        return False


# 먼지 확산
def dust_spread(r, c, spread):
    '''
    input : 좌표, spread
    '''
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if inrange(nr, nc):
            room[nr][nc] += spread
            room[r][c] -= spread


# 좌표 구하기
def get_command():
    commands = []
    for r in range(row_size):
        for c in range(col_size):
            if room[r][c] >= 5:
                commands.append((r, c, room[r][c] // 5))
    return commands


# 공기청정기 좌표, 회전 좌표 구하기
def aircon_rc():
    r1 = r2 = 0
    for r in range(row_size):
        if room[r][0] == -1:
            r1 = r
            r2 = r + 1
            break

    # 윗방향
    delta = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    rotate_idx = deque([(r1, 1)])
    delta_idx = 0
    while True:
        r_now, c_now = rotate_idx[-1]
        r_d, c_d = delta[delta_idx]

        nr = r_now + r_d
        nc = c_now + c_d
        if (nr, nc) == (r1, 0):
            rotate_idx.append((nr, nc))
            break
        elif inrange(nr, nc):
            rotate_idx.append((nr, nc))
        else:
            delta_idx += 1
            r_d, c_d = delta[delta_idx]
            nr = r_now + r_d
            nc = c_now + c_d
            rotate_idx.append((nr, nc))

    # 아랫방향 1
    delta2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rotate_idx2 = deque([(r2, 1)])
    delta_idx = 0
    while True:
        r_now, c_now = rotate_idx2[-1]
        r_d, c_d = delta2[delta_idx]

        nr = r_now + r_d
        nc = c_now + c_d
        if (nr, nc) == (r2, 0):
            rotate_idx2.append((nr, nc))
            break
        elif inrange(nr, nc):
            rotate_idx2.append((nr, nc))
        else:
            delta_idx += 1
            r_d, c_d = delta2[delta_idx]
            nr = r_now + r_d
            nc = c_now + c_d
            rotate_idx2.append((nr, nc))

    return (rotate_idx, rotate_idx2, r1, r2)


rotate_idx1, rotate_idx2, r1, r2 = aircon_rc()

for _ in range(times):
    commands = get_command()

    for r, c, spread in commands:
        dust_spread(r, c, spread)

    up_dusts = deque([])
    down_dusts = deque([])
    for r, c in rotate_idx1:
        up_dusts.append(room[r][c])
    
    for r, c in rotate_idx2:
        down_dusts.append(room[r][c])

    # print('===========================')
    # for i in room:
    #     print(i)
    # print(rotate_idx2)

    rotate_idx1.rotate(-1)
    rotate_idx2.rotate(-1)

    # print(rotate_idx2)
    # print('===========================')
    for r, c in rotate_idx1:
        room[r][c] = up_dusts.popleft()

    for r, c in rotate_idx2:
        room[r][c] = down_dusts.popleft()
    
    room[r1][0]= room[r2][0] = -1
    room[r1][1]= room[r2][1] = 0
    
    # for i in room:
    #     print(i)

print(sum(map(sum, room)) + 2)