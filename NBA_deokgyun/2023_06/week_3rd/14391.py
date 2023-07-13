# [BOJ] 14391. 종이 조각
# 소요 시간 : 00분

n, m = map(int, input().split())
used = [[False for _ in range(m)] for _ in range(n)]
board = []
for _ in range(n):
    board.append(input().split())

for i in range(n):
    for j in range(m):
        numstr = ""
        ni, nj = i, j
        while not used[ni][nj]:
            numstr += board[ni][nj]
            ni += 1
        numlist = []