# [BOJ] 16926. 배열 돌리기 1
# 소요 시간 : 00분
import sys
from collections import deque
input = sys.stdin.readline


def generate_line(matrix: list, i: int):
    r, c = len(matrix), len(matrix[0])
    line = []

    # 테두리를 1차원 배열로 만들기
    for j in range(i, c-i):
        line.append(matrix[0+i][j])
    for j in range(1+i, r-(1+i)):
        line.append(matrix[j][c-(1+i)])
    for j in range(c-(1+i), i-1, -1):
        line.append(matrix[r-(1+i)][j])
    for j in range(r-(2+i), i, -1):
        line.append(matrix[j][0+i])

    return line


def rotation(line: list):
    index = R % len(line)
    rotated_line = line[index:] + line[:index]

    return rotated_line


def rotate_new_matrix(line: list, i: int):
    r, c = len(matrix), len(matrix[0])

    line = deque(line)

    # 테두리를 1차원 배열로 만들기
    for j in range(i, c-i):
        new_matrix[0+i][j] = line.popleft()
    for j in range(1+i, r-(1+i)):
        new_matrix[j][c-(1+i)] = line.popleft()
    for j in range(c-(1+i), i-1, -1):
        new_matrix[r-(1+i)][j] = line.popleft()
    for j in range(r-(2+i), i, -1):
        new_matrix[j][0+i] = line.popleft()


N, M, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
new_matrix = [[0] * M for _ in range(N)]

loop = min(N, M) // 2

for i in range(loop):
    line = generate_line(matrix, i)
    rotated_line = rotation(line)
    rotate_new_matrix(rotated_line, i)

print('\n'.join([' '.join(map(str, row)) for row in new_matrix]))
