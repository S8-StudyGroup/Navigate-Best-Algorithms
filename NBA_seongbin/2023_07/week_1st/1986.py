# [BOJ] 1986. 체스
# 소요 시간 : 00분
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def generateChessmenPosition(chessmen: list):
    chessmen.pop(0)
    chessmenPosition = [[row, col]
                        for row, col in zip(chessmen[::2], chessmen[1::2])]
    return chessmenPosition


def paint(chessmen: str, chessmenPosition: list):
    for row, col in chessmenPosition:
        matrix[row-1][col-1] = chessmen


def up(row, col):
    if row == 0:
        return

    if matrix[row-1][col] not in chessmenList:
        matrix[row-1][col] = 'X'
        up(row-1, col)


def down(row, col):
    if row == n-1:
        return

    if matrix[row+1][col] not in chessmenList:
        matrix[row+1][col] = 'X'
        down(row+1, col)


def right(row, col):
    if col == m-1:
        return

    if matrix[row][col+1] not in chessmenList:
        matrix[row][col+1] = 'X'
        right(row, col+1)


def left(row, col):
    if col == 0:
        return

    if matrix[row][col-1] not in chessmenList:
        matrix[row][col-1] = 'X'
        left(row, col-1)


def upRight(row, col):
    if row == 0 or col == m-1:
        return

    if matrix[row-1][col+1] not in chessmenList:
        matrix[row-1][col+1] = 'X'
        upRight(row-1, col+1)


def upLeft(row, col):
    if row == 0 or col == 0:
        return

    if matrix[row-1][col-1] not in chessmenList:
        matrix[row-1][col-1] = 'X'
        upLeft(row-1, col-1)


def downRight(row, col):
    if row == n-1 or col == m-1:
        return

    if matrix[row+1][col+1] not in chessmenList:
        matrix[row+1][col+1] = 'X'
        downRight(row+1, col+1)


def downLeft(row, col):
    if row == n-1 or col == 0:
        return

    if matrix[row+1][col-1] not in chessmenList:
        matrix[row+1][col-1] = 'X'
        downLeft(row+1, col-1)


def border(chessmen, row, col):
    for r, c in delta[chessmen]:
        nr, nc = row + r, col + c
        if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] not in chessmenList:
            matrix[nr][nc] = 'X'


def queenMove(row, col):
    up(row, col)
    down(row, col)
    right(row, col)
    left(row, col)
    upRight(row, col)
    upLeft(row, col)
    downRight(row, col)
    downLeft(row, col)
    border('Q', row, col)


def knightMove(row, col):
    border('K', row, col)


n, m = map(int, input().split())
matrix = [[''] * m for _ in range(n)]
chessmenList = ['Q', 'K', 'P']
delta = {
    'K': [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]],
    'Q': [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]],
}

queen = list(map(int, input().split()))
queenPosition = generateChessmenPosition(queen)
paint('Q', queenPosition)

knight = list(map(int, input().split()))
knightPosition = generateChessmenPosition(knight)
paint('K', knightPosition)

pawn = list(map(int, input().split()))
pawnPosition = generateChessmenPosition(pawn)
paint('P', pawnPosition)

for row in range(n):
    for col in range(m):
        if matrix[row][col] == 'Q':
            queenMove(row, col)
        elif matrix[row][col] == 'K':
            knightMove(row, col)

answer = 0
for row in range(n):
    for col in range(m):
        if matrix[row][col] == '':
            answer += 1

print(answer)
