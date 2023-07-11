# [BOJ] 1520. 내리막길
# 소요 시간 : 00분

row, col = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(row)]

valuelist = []

wayboard = [[0 for _ in range(col)] for _ in range(row)]
wayboard[0][0] = 1

for i in range(row):
    for j in range(col):
        valuelist.append((i,j,board[i][j]))

valuelist.sort(key=lambda x:x[2], reverse=True)

for i,j,value in valuelist:
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < row and 0 <= nj < col and board[ni][nj] > board[i][j]:
            wayboard[i][j] += wayboard[ni][nj]
print(wayboard[-1][-1])