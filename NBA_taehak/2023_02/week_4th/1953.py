# [SWEA] 1953. 탈주범 검거
# 소요 시간 : 00분

from collections import deque


# 상 우 하 좌
d_r = [-1, 0, 1, 0]
d_c = [0, 1, 0, -1]

tunnel = {
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [1, 3],
    4: [0, 1],
    5: [1, 2],
    6: [2, 3],
    7: [0, 3],
}

contact = {
    0: [1, 2, 5, 6],
    1: [1, 3, 6, 7],
    2: [1, 2, 4, 7],
    3: [1, 3, 4, 5],
}


def runrun(row, col, time):
    visited[row][col] = time
    if time == time_limit:
        return
    time += 1

    for direction in tunnel[area[row][col]]:
        next_r = row + d_r[direction]
        next_c = col + d_c[direction]

        if 0 <= next_r < row_size and 0 <= next_c < col_size and (not visited[next_r][next_c] or visited[next_r][next_c] > time) and area[next_r][next_c] in contact[direction]:
            runrun(next_r, next_c, time)


for case in range(1, int(input()) + 1):
    row_size, col_size, manhole_row, manhole_col, time_limit = map(
        int, input().split())

    area = [list(map(int, input().split())) for _ in range(row_size)]
    visited = [[False] * col_size for _ in range(row_size)]

    runrun(manhole_row, manhole_col, 1)

    result = 0
    for row in range(row_size):
        for col in range(col_size):
            if visited[row][col] != False:
                result += 1

    print(f'#{case} {result}')