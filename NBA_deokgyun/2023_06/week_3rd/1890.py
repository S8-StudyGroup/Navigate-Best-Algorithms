# [BOJ] 1890. 점프
# 소요 시간 : 00분
# 9,223,372,036,854,775,808 = 대충 900경


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
board2 = [[0 for _ in range(n)] for _ in range(n)]
board2[0][0] = 1
for i in range(n):
    for j in range(n):
        num = board[i][j]
        if i == n-1 and j == n-1:
            break
        try:
            board2[i + num][j] += board2[i][j]
        except IndexError:
            pass
        try:
            board2[i][j + num] += board2[i][j]
        except IndexError:
            pass
print(board2[n-1][n-1])