# [BOJ] 17144. 미세먼지 안녕!
# 소요 시간 : 60분


def valid_spread_dust(y:int, x:int) -> bool:
    """
    미세먼지의 확산이 이루어지는 곳인지를 판별하는 함수입니다.
    """
    return 0 <= y < R and 0 <= x < C and room[y][x] != -1


def spread_dust() -> list:
    """
    미세먼지가 확산되는 과정을 나타내는 함수입니다.
    """
    new_room = [[0] * C for _ in range(R)]
    
    for ac_y, ac_x in air_cleaner:
        new_room[ac_y][ac_x] = -1

    for y in range(R):
        for x in range(C):
            cnt_place_of_spread = 0
            if room[y][x] >= 5:
                for d in range(4):
                    move_y, move_x = y + dy[d], x + dx[d]
                    
                    if valid_spread_dust(move_y, move_x):
                        cnt_place_of_spread += 1
                        new_room[move_y][move_x] += room[y][x] // 5

            if new_room[y][x] != -1: 
                new_room[y][x] += room[y][x] - (room[y][x] // 5) * cnt_place_of_spread

    return new_room 
                        

def working_air_cleaner() -> None:
    """
    공기청정기가 작동하는 과정을 나타내는 함수입니다.
    """

    cw_d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ccw_d = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    for idx, (ac_y, ac_x) in enumerate(air_cleaner):
        move_y, move_x, tmp = ac_y, ac_x, 0
        for dy, dx in ccw_d if idx == 0 else cw_d:
            while True:
                move_y, move_x = move_y + dy, move_x + dx
                tmp, room[move_y][move_x] = room[move_y][move_x], tmp
                if not (0 <= move_y + dy < R and 0 <= move_x + dx < C and room[move_y + dy][move_x + dx] != -1):
                    break


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

R, C, T = map(int, input().split())
room = []

air_cleaner = []
for i in range(R):
    row = list(map(int, input().split()))
    for j in range(C):
        if row[j] == -1:
            air_cleaner.append((i, j))
    
    room.append(row)

for _ in range(T):
    room = spread_dust()
    working_air_cleaner()

print(sum([sum(room[i]) for i in range(R)]) + 2)