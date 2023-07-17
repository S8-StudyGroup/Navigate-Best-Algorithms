# [BOJ] 10836. 여왕벌
# 소요 시간 : 00분

from sys import stdin
readline = stdin.readline

length, days = map(int, readline().split())
board = [[1 for _ in range(length)] for _ in range(length)]
total_grow = [0 for _ in range(2*length - 1)]
grow_len = 2*length - 1
for day in range(days):
    idx = readline()
    zero, one, two = map(int, idx.split())
    for i in range(zero, grow_len):
        total_grow[i] += 1 if i < one + zero else 2

for i in range(length):
    board[length - 1 - i][0] += total_grow[i]
    if i != grow_len - 1 - i:
        board[0][length - 1 - i] += total_grow[grow_len - 1 - i]
    else:
        break
total_grow2 = total_grow[grow_len // 2:]
for i in range(1, length):
    for j in range(1, length):
        board[i][j] += total_grow2[j]
    
for line in board:
    print(*line)