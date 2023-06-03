# [BOJ] 5547. 일루미네이션
# 소요 시간 : 00분

import sys
from collections import deque
input = sys.stdin.readline

# 1. 건물 바깥과 연결되어있으면서 건물이 없는 곳 분류
# 2. BFS를 통해 각 변이 1번 또는 건물 바깥과 연결되어 있다면 조명 + 1


def find_non_building_area():
    for h in [0, H - 1]:
        for w in range(W):
            if matrix[h][w] == 0:
                non_building_bfs(h, w)

    for h in range(H):
        for w in [0, W - 1]:
            if matrix[h][w] == 0:
                non_building_bfs(h, w)

def non_building_bfs(h, w):
    matrix[h][w] = 2
    queue = deque()
    queue.append((h, w))

    while queue:
        y, x = queue.popleft()
        odd_or_even = "odd" if y % 2 == 1 else "even"
        for d in range(6):
            move_y, move_x = y + dir_dict[odd_or_even][d][0], x + dir_dict[odd_or_even][d][1]
            if 0 <= move_y < H and 0 <= move_x < W and matrix[move_y][move_x] == 0:
                if move_y == 2 and move_x == 1:
                    print(h, w, y, x)
                matrix[move_y][move_x] = 2
                queue.append((move_y, move_x))

def find_building_area():
    for h in range(H):
        for w in range(W):
            if matrix[h][w] == 1:
                building_bfs(h, w)



def building_bfs(h, w):
    global cnt_light
    matrix[h][w] = 3
    queue = deque()
    queue.append((h, w))

    while queue:
        y, x = queue.popleft()
        odd_or_even = "odd" if y % 2 == 1 else "even"
        for d in range(6):
            move_y, move_x = y + dir_dict[odd_or_even][d][0], x + dir_dict[odd_or_even][d][1]
            if not 0 <= move_y < H or not 0 <= move_x < W or matrix[move_y][move_x] == 2:
                cnt_light += 1
            elif matrix[move_y][move_x] == 1:
                matrix[move_y][move_x] = 3
                queue.append((move_y, move_x))


dir_dict = {
    "odd": [(-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1)],
    "even": [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]
}

W, H = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]
cnt_light = 0

find_non_building_area()
find_building_area()

print(cnt_light)