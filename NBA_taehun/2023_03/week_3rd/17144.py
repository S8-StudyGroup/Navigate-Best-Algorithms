# [BOJ] 17144. 미세먼지 안녕!
# 소요 시간 : 00분

import sys
from collections import defaultdict
input = sys.stdin.readline


def air_clean():
    """
    공기 청정기 작동
    """
    for idx, d in enumerate([d_up, d_down]):
        old_dust = 0
        r, c = air_cleaner[idx]
        for dr, dc in d:
            while True:
                nr, nc = r + dr, c + dc
                if nc >= C or nc < 0 or nr >= R or nr < 0:
                    break
                
                dust = room[nr][nc]
                if dust != -1:
                    room[nr][nc], old_dust = old_dust, dust
                    r, c = nr, nc
                else:
                    break
                



def dust_diffusion():
    """
    먼지 확산
    """
    move_dust = defaultdict(int)
    for r in range(R):
        for c in range(C):
            dust = room[r][c]
            if dust > 0:
                move_dust_amount = dust // 5
                if move_dust_amount > 0:
                    count = 0
                    for dr, dc in d:
                        nr ,nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                            move_dust[(nr, nc)] += move_dust_amount
                            count += 1
                    room[r][c] = dust - (move_dust_amount * count)
            elif dust == -1:
                air_cleaner.append((r, c))
    

    for key, value in move_dust.items():
        room[key[0]][key[1]] += value
    


def total_dust_amount():
    """
    먼지의 양
    """
    total = 2
    for r in range(R):
        total += sum(room[r])
    return total

R, C, T = map(int, input().strip().split())

room = [list(map(int, input().strip().split())) for _ in range(R)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
d_up = [(0, 1), (-1, 0), (0, -1), (1, 0)]
d_down = [(0, 1), (1, 0), (0, -1), (-1, 0)]

air_cleaner = []
for _ in range(T):
    dust_diffusion()
    air_clean()
print(total_dust_amount())
