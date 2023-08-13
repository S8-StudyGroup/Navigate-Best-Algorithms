# [BOJ] 20061. 모노미노도미노 2
# 소요 시간 : 60분

import sys
input = sys.stdin.readline


def create_blocks(t, y, x):
    green_matrix[0][x] = 1
    blue_matrix[0][3 - y] = 1
    
    if t == 2:
        green_matrix[0][x + 1] = 1
        blue_matrix[1][3 - y] = 1
    elif t == 3:
        green_matrix[1][x] = 1
        blue_matrix[0][2 - y] = 1


def play(matrix: list):
    tiles = []
    for i in range(2):
        for j in range(4):
            if matrix[1 - i][j] == 1:
                tiles.append([1 - i, j])

    breaker = True
    while breaker:
        for ty, tx in tiles:
            if ty + 1 > 5 or matrix[ty + 1][tx] == 2:
                breaker = False
                break
        else:
            for idx, tile in enumerate(tiles):
                ty, tx = tile
                matrix[ty][tx], matrix[ty + 1][tx] = matrix[ty + 1][tx], matrix[ty][tx]
                tiles[idx][0] += 1
    
    for ty, tx in tiles:
        matrix[ty][tx] = 2
    
    for i in range(2, 6):
        if sum(matrix[i]) == 8:
            global score
            del matrix[i]
            matrix.insert(0, [0] * 4)
            score += 1

    cnt = 0
    for i in range(0, 2):
        if sum(matrix[i]) != 0:
            cnt += 1
    
    for i in range(cnt):
        matrix.pop()
        matrix.insert(0, [0] * 4)



def count_tiles():
    green_tiles = sum([sum(green_matrix[i]) for i in range(6)])
    blue_tiles = sum([sum(blue_matrix[i]) for i in range(6)])
    return (green_tiles + blue_tiles) // 2


N = int(input())
green_matrix = [[0] * 4 for _ in range(6)]
blue_matrix = [[0] * 4 for _ in range(6)]
score = 0

for _ in range(N):
    t, y, x = map(int, input().split())

    create_blocks(t, y, x)
    play(green_matrix)
    play(blue_matrix)

print(score)
print(count_tiles())