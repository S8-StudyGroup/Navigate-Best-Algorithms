# [BOJ] 1074. Z
# 소요 시간 : 50분

import sys
n, r, c = map(int, sys.stdin.readline().split())
cnt = 0


def search(width, x, y): # 사분면씩 체크
    global cnt
    if width == 1:
        return
    half = width // 2
    plus = half ** 2
    if x < half:
        if y < half: # 2
            cnt += 0
            search(half, x, y)
            return
        else: # 1
            cnt += plus
            search(half, x, y - half)
            return
    else:
        if y < half: # 3
            cnt += 2 * plus
            search(half, x - half, y)
            return
        else: # 4
            cnt += 3 * plus
            search(half, x - half, y - half)
            return


search(2 ** n, r, c)
print(cnt)