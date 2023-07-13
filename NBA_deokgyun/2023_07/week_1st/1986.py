# [BOJ] 1986. 체스
# 소요 시간 : 00분

n, m = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
queen = list(map(int, input().split()[1:]))
queen_list = list(zip(queen[::2], queen[1::2]))
knight = list(map(int, input().split()[1:]))
knight_list = list(zip(knight[::2], knight[1::2]))
pawn = list(map(int, input().split()[1:]))
pawn_list = list(zip(pawn[::2], pawn[1::2]))
safezone = n * m
for i in queen_list:
    board[i[0] - 1][i[1] - 1] = 1
    safezone -= 1
for i in knight_list:
    board[i[0] - 1][i[1] - 1] = 2
    safezone -= 1
for i in pawn_list:
    board[i[0] - 1][i[1] - 1] = 3
    safezone -= 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    ni = i
                    nj = j
                    while True:
                        ni += di
                        nj += dj
                        if 0 <= ni < n and 0 <= nj < m:
                            if board[ni][nj] == 0:
                                board[ni][nj] = -1
                                safezone -= 1
                            elif board[ni][nj] >= 1:
                                break
                        else:
                            break
        elif board[i][j] == 2:
            for two in [-2,2]:
                for one in [-1,1]:
                    for di, dj in [[two,one], [one,two]]:
                        ni = i
                        nj = j
                        ni += di
                        nj += dj
                        if 0 <= ni < n and 0 <= nj < m:
                            if board[ni][nj] == 0:
                                board[ni][nj] = -1
                                safezone -= 1
print(safezone)