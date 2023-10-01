# [BOJ] 16918. 봄버맨
# 소요 시간 : 50분
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bomb(board):
    return_board = [['O'] * C for _ in range(R)]
    bomb_position = []

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bomb_position.append((i, j))

    for i in range(R):
        for j in range(C):
            if (i, j) in bomb_position:
                return_board[i][j] = '.'
                for direction in range(4):
                    nr = i + dr[direction]
                    nc = j + dc[direction]
                    if 0 <= nr < R and 0 <= nc < C:
                        return_board[nr][nc] = '.'

    return return_board


def print_board(board):
    answer = ""
    for row in board:
        answer += "".join(row)
        answer += '\n'

    print(answer)


R, C, N = map(int, input().split())
first_board = [list(input().strip()) for _ in range(R)]
second_board = [['O'] * C for _ in range(R)]

if N == 1:
    print_board(first_board)
elif N % 2 == 0:
    print_board(second_board)
elif N % 4 == 3:
    print_board(bomb(first_board))
else:
    print_board(bomb(bomb(first_board)))
