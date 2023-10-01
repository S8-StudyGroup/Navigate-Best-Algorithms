# [BOJ] 20061. 모노미노도미노 2
# 소요 시간 : 90분 + a
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
boards = [list(map(int, input().split())) for _ in range(n)]
matrix = [[0] * 10 for _ in range(10)]
score = 0


def move(t, r, c):
    if t == 1:
        for i in range(5, 11):
            if i == 10 or matrix[r][i] != 0:
                matrix[r][i - 1] = 1
                break
        for i in range(5, 11):
            if i == 10 or matrix[i][c] != 0:
                matrix[i - 1][c] = 1
                break
    elif t == 2:
        for i in range(5, 11):
            if i == 10 or matrix[r][i] != 0:
                matrix[r][i - 1] = 1
                matrix[r][i - 2] = 1
                break
        for i in range(5, 11):
            if i == 10 or matrix[i][c] != 0 or matrix[i][c + 1] != 0:
                matrix[i - 1][c] = 1
                matrix[i - 1][c + 1] = 1
                break
    elif t == 3:
        for i in range(5, 11):
            if i == 10 or matrix[r][i] != 0 or matrix[r + 1][i] != 0:
                matrix[r][i - 1] = 1
                matrix[r + 1][i - 1] = 1
                break
        for i in range(5, 11):
            if i == 10 or matrix[i][c] != 0:
                matrix[i - 1][c] = 1
                matrix[i - 2][c] = 1
                break


def check_bingo():
    """_summary_

    행 열을 검사하고, 빙고가 되면 점수를 올리고, 빙고가 된 행/열을 0로 바꾼다.

    Returns:
    blue_bingo (list): blue_bingo 열 index를 담은 리스트
    green_bingo (list): green_bingo 행 index를 담은 리스트
    """
    global score
    blue_bingo = []
    green_bingo = []
    for i in range(9, 5, -1):
        is_blue_bingo = 1
        is_green_bingo = 1
        for j in range(4):
            if matrix[j][i] == 0:
                is_blue_bingo = 0
                break
        for j in range(4):
            if matrix[i][j] == 0:
                is_green_bingo = 0
                break

        if is_blue_bingo:
            score += 1
            blue_bingo.append(i)
            for j in range(4):
                matrix[j][i] = 0

        if is_green_bingo:
            score += 1
            green_bingo.append(i)
            for j in range(4):
                matrix[i][j] = 0

    return blue_bingo, green_bingo


def remove_col(col):
    """_summary_:
    col 열을 삭제하고, 빈 공간을 채운다.
    """
    for col in range(col, 3, -1):
        for row in range(4):
            matrix[row][col] = matrix[row][col - 1]


def remove_row(row):
    """_summary_:
    row 행을 삭제하고, 빈 공간을 채운다.
    """
    for row in range(row, 3, -1):
        for col in range(4):
            matrix[row][col] = matrix[row - 1][col]


def check_special_area():
    """_summary_

    특별 영역을 검사하고, 블록이 있는 영역의 수 반환

    Returns:
    blue_special_area (int): blue_special_area의 수
    green_special_area (int): green_special_area의 수
    """
    blue_special_area = 0
    for col in range(2, 0, -1):
        for row in range(4):
            if matrix[row][-col - 4] != 0:
                blue_special_area = col
                break
        if blue_special_area != 0:
            break

    green_special_area = 0
    for row in range(2, 0, -1):
        for col in range(4):
            if matrix[-row - 4][col] != 0:
                green_special_area = row
                break
        if green_special_area != 0:
            break

    return blue_special_area, green_special_area


def count_tile():
    tile = 0
    for row in range(10):
        for col in range(10):
            if matrix[row][col] != 0:
                tile += 1

    return tile


for t, r, c in boards:
    move(t, r, c)

    blue_bingo, green_bingo = check_bingo()

    for i in blue_bingo[::-1]:
        remove_col(i)
    for i in green_bingo[::-1]:
        remove_row(i)

    blue_special_area, green_special_area = check_special_area()

    for _ in range(blue_special_area):
        remove_col(9)
    for _ in range(green_special_area):
        remove_row(9)


count_tile()

print(score)
print(count_tile())
