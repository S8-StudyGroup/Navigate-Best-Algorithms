# [BOJ] 16918. 봄버맨
# 소요 시간 : 00분

# 풀이 1
import sys
import copy

input = sys.stdin.readline

R, C, N = map(int, input().strip().split())

board = [list(map(str, input().strip())) for _ in range(R)]
boom_board = [["O"] * C for _ in range(R)]
table = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
if N % 2 == 0:
    for line in boom_board:
        print("".join(line))
else:
    for n in range(N // 2):
        O_list = []
        temp_board = copy.deepcopy(boom_board)
        for r in range(R):
            for c in range(C):
                    if board[r][c] == "O":
                        O_list.append((r,c))

        for r, c in O_list:
            for dr, dc in table:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        temp_board[nr][nc] = "."
        board = temp_board
    for line in board:
          print("".join(line))

# 풀이 2
import sys

input = sys.stdin.readline

R, C, N = map(int, input().strip().split())

board = [list(map(str, input().strip())) for _ in range(R)]
boom_board = [["O"] * C for _ in range(R)]

if N <= 1:
    for line in board:
        print("".join(line))
elif N % 2 == 0:
    for line in R:
        print("O" * C)
else:
    board1 = [["O"] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == "O":
                board1[r][c] = "."
                if r-1 >= 0:
                    board1[r-1][c] = "."
                if r + 1 < R:
                    board1[r+1][c] = "."
                if c-1 >= 0:
                    board1[r][c-1] = "."
                if c + 1 < C:
                    board1[r][c+1] = "."

    board2 = [["O"] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board1[r][c] == "O":
                board2[r][c] = "."
                if r-1 >= 0:
                    board2[r-1][c] = "."
                if r + 1 < R:
                    board2[r+1][c] = "."
                if c-1 >= 0:
                    board2[r][c-1] = "."
                if c + 1 < C:
                    board2[r][c+1] = "."

    if N % 4 == 3:
        for line in board1:
            print("".join(line))
    elif N % 4 == 1:
        for line in board2:
            print("".join(line))

