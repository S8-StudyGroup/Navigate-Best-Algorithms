# [BOJ] 16926. 배열 돌리기 1
# 소요 시간 : 00분
from collections import deque
from copy import deepcopy


def onion(row_size, col_size):
    skins = []

    # 껍질 하나씩
    for rc_start in range(min(row_size, col_size) // 2):
        skin = deque([])
        r_end = row_size - rc_start
        c_end = col_size - rc_start

        # ➡
        for c in range(rc_start, c_end):
            skin.append((rc_start, c))
        # ⬇
        for r in range(rc_start + 1, r_end - 1):
            skin.append((r, c_end - 1))
        # ⬅
        for c in range(c_end - 1, rc_start - 1, -1):
            skin.append((r_end - 1, c))
        # ⬆
        for r in range(r_end - 2, rc_start, -1):
            skin.append((r, rc_start))

        skins.append(skin)

    return skins


def rotate(skins, rotate_cnt):
    new_arr = [[0] * col_size for _ in range(row_size)]
    for skin in skins:
        skin_0 = deepcopy(skin)
        skin.rotate(-rotate_cnt)
        while skin:
            nr, nc = skin_0.popleft()
            r, c = skin.popleft()

            new_arr[nr][nc] = arr[r][c]

    for line in new_arr:
        print(*line)


row_size, col_size, rotate_cnt = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row_size)]

skins = onion(row_size, col_size)
rotate(skins, rotate_cnt)