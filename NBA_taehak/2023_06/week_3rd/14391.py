# [BOJ] 14391. 종이 조각
# 소요 시간 : 00분
from itertools import product

row_size, col_size = map(int, input().split())
area = [list(map(int, list(input()))) for _ in range(row_size)]

sets = [0, 1]
dr = [0, 1]
dc = [1, 0]

answer = 0

for case in product(sets, repeat = row_size * col_size):
    area_case = [[] for _ in range(row_size)]
    for idx, di in enumerate(case):
        area_case[idx // col_size].append(di)

    visited = [[False] * col_size for _ in range(row_size)]
    num_sum = 0

    for r in range(row_size):
        for c in range(col_size):
            if visited[r][c]:
                continue

            num = area[r][c]
            visited[r][c] = True
            di = area_case[r][c]
            rr, cc = r, c
            while True:
                nr = rr + dr[di]
                nc = cc + dc[di]

                if 0 <= nr < row_size and 0 <= nc < col_size and area_case[nr][nc] == di:
                    visited[nr][nc] = True
                    num = num * 10 + area[nr][nc]
                    rr = nr
                    cc = nc
                
                else:
                    num_sum += num
                    break
    
    answer = max(answer, num_sum)

print(answer)