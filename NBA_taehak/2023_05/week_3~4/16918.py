# [BOJ] 16918. 봄버맨
# 소요 시간 : 00분
import sys
input = sys.stdin.readline

row_size, col_size, times = map(int, input().split())
case = times % 4

if times == 1:
    for _ in range(row_size):
        print(input())

elif case in [0, 2]:
    for _ in range(row_size):
        input()
    for _ in range(row_size):
        print('O'*col_size)

else:
    area = [list(input()) for _ in range(row_size)]


    def cycle():
        global area
        bomb = []
        for r in range(row_size):
            for c in range(col_size):
                if area[r][c] == 'O':
                    bomb.append((r, c))
        
        area = [list('O' * col_size) for _ in range(row_size)]
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for r, c in bomb:
            area[r][c] = '.'

            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < row_size and 0 <= nc < col_size:
                    area[nr][nc] = '.'


    cycle()
    if case == 1:
        cycle()

    for line in area:
        print(''.join(line))