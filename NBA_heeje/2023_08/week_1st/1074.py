# [BOJ] 1074. Z
# 소요 시간 : 60분


def filled_number(start_y, end_y, start_x, end_x, num):
    if end_y - start_y == 2:
        if start_y == r and start_x == c:
            print(num)
        elif start_y == r and end_x - 1 == c:
            print(num + 1)
        elif end_y - 1 == r and start_x == c:
            print(num + 2)
        else:
            print(num + 3)
        return

    mid_y = (start_y + end_y) // 2
    mid_x = (start_x + end_x) // 2
    quarter_num = (end_y - start_y) ** 2 // 4
    matrix_ranges = [
        [start_y, mid_y, start_x, mid_x],
        [start_y, mid_y, mid_x, end_x],
        [mid_y, end_y, start_x, mid_x],
        [mid_y, end_y, mid_x, end_x],
        ]
    for idx, matrix_range in enumerate(matrix_ranges):
        y1, y2, x1, x2 = matrix_range
        if y1 <= r < y2 and x1 <= c < x2:
            filled_number(y1, y2, x1, x2, num + quarter_num * idx)

N, r, c = map(int, input().split())
filled_number(0, 2 ** N, 0, 2 ** N, 0)