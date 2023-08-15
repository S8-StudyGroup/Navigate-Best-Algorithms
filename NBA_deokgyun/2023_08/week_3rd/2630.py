# [BOJ] 2630. 색종이 만들기
# 소요 시간 : 00분
from math import log2 as log
length = int(input())
k_len = int(log(length))

board = []
for _ in range(length):
    board.append(list(map(int, input().split())))

count = [0,0]

for k in range(k_len, -1, -1):
    wide = 2**k
    for i in range(0, length, wide):
        for j in range(0, length, wide):
            prev = board[i][j]
            if prev != -1:
                for t in range(i, i + wide):
                    for y in range(j, j + wide):
                        if board[t][y] != prev:
                            prev = -2
                            break
                    if prev == -2:
                        break
                else:
                    for t in range(i, i + wide):
                        for y in range(j, j + wide):
                            board[t][y] = -1
                    count[prev] += 1
print(*count,sep="\n")