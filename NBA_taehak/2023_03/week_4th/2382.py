# [SWEA] 2382. 미생물 격리
# 소요 시간 : 00분
from collections import defaultdict

# 상하좌우
# delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
back = {0:1, 1:0, 2:3, 3:2}


def move(biomes, cell_size):
    '''
    Args:
        biomes: 미생물 군집 정보 딕셔너리
        cell_size: 한변에 들어가는 셀 개수
    Returns:
        한 사이클 이후 새로운 biomes 
    '''
    next_biomes = dict()

    for key, item in biomes.items():
        r, c = key
        micro_max, di, micro = item

        nr = r + dr[di]
        nc = c + dc[di]

        # 가장자리
        if nr in [0, cell_size - 1] or nc in [0, cell_size - 1]:
            next_biomes[(nr, nc)] = (micro // 2, back[di], micro // 2)
        # 합쳐질 경우
        elif (nr, nc) in next_biomes:
            micro_max_0, di_0, micro_0 = next_biomes[(nr, nc)]
            if micro > micro_max_0:
                next_biomes[(nr, nc)] = (micro, di, micro_0 + micro)
            else:
                next_biomes[(nr, nc)] = (micro_max_0, di_0, micro_0 + micro)
        # 그 외
        else:
            next_biomes[(nr, nc)] = (micro, di, micro)

    return next_biomes
        

for case_num in range(1, int(input()) + 1):
    # NMK 
    cell_size, time, biome_cnt = map(int, input().split())

    # { (r, c) : (미생물 수(최대값), 방향, 총 합) }
    biomes = defaultdict()
    for _ in range(biome_cnt):
        r, c, micro, di = map(int, input().split())
        biomes[(r, c)] = (micro, di - 1, micro)

    # if case_num != 2:
    #     continue

    # for key, item in biomes.items():
    #         print(key, item)
    for _ in range(time):
        biomes = move(biomes, cell_size)
        # print('=========================================================================')
        # for key, item in biomes.items():
        #     print(key, item)

    result = 0
    for key, item in biomes.items():
        result += item[2]

    print(f'#{case_num} {result}')