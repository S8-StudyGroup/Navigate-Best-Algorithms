# [BOJ] 21317. 징검다리 건너기
# 소요 시간 : 00분
from copy import deepcopy

stone_cnt = int(input())
small_jump = []
big_jump = []

for _ in range(stone_cnt-1):
    small, big = map(int, input().split())
    small_jump.append(small)
    big_jump.append(big)
giant_jump = int(input())

if stone_cnt == 1:
    print(0)
elif stone_cnt == 2:
    print(small_jump[0])
elif stone_cnt == 3:
    print(min(sum(small_jump), big_jump[0]))
else:
    # giant점프 안하고 그냥 dp
    energy = [0 for _ in range(stone_cnt)]
    energy[0] = 0
    energy[1] = small_jump[0]
    for idx in range(2, stone_cnt):
        energy[idx] = min(energy[idx-2] + big_jump[idx-2], energy[idx-1] + small_jump[idx-1])
    cost = [energy[stone_cnt-1]]

    # giant점프 했을 때 경우의수 모두 dp 계산하기
    for k in range(stone_cnt-3):
        energy_giant = deepcopy(energy)
        energy_giant[k+3] = energy[k] + giant_jump
        for i in range(k+4, stone_cnt):
            energy_giant[i] = min(energy_giant[i-2] + big_jump[i-2], energy_giant[i-1] + small_jump[i-1])
        cost.append(energy_giant[stone_cnt-1])

    print(min(cost))