# [BOJ] 17143. 낚시왕
# 소요 시간 : 00분
# 메모리 219180kb 시간 664ms

def shark_move(row, col, velocity, d_idx):
    # 위아래
    if d_idx in [1, 2]:
        velocity %= row_cycle
        for _ in range(velocity):
            if row == 0:
                d_idx = 2
            elif row == row_max:
                d_idx = 1

            row += dr[d_idx]

    # 왼오른
    else:
        velocity %= col_cycle
        for _ in range(velocity):
            if col == 0:
                d_idx = 3
            elif col == col_max:
                d_idx = 4
            col += dc[d_idx]

    return row, col, d_idx
    

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]

row_size, col_size, shark_cnt = map(int, input().split())
row_max = row_size - 1
col_max = col_size - 1
row_cycle = row_size * 2 - 2
col_cycle = col_size * 2 - 2

# shark : (row, col, velocity, direction, shark_size)
sharks = []
for _ in range(shark_cnt):
    row, col, velocity, d_idx, shark_size = map(int, input().split())
    sharks.append((row-1, col-1, velocity, d_idx, shark_size))

area = [[[] for _ in range(col_size)] for _ in range(row_size)]

# 상어 배치
while sharks:
    row, col, velocity, d_idx, shark_size = sharks.pop()
    area[row][col].append((row, col, velocity, d_idx, shark_size))

catch_sum = 0

for fishman_col in range(col_size):

    # catch
    for row in range(row_size):
        if area[row][fishman_col]:
            catch_sum += max(map(lambda x : x[4], area[row][fishman_col]))
            area[row][fishman_col] = []
            break
    
    # eat 
    for row in range(row_size):
        for col in range(col_size):
            if len(area[row][col]) > 1:
                area[row][col].sort(key=lambda x : x[4])
                sharks.append(area[row][col].pop())
                area[row][col] = []
            elif area[row][col]:
                sharks.append(area[row][col].pop())

    # move
    while sharks:
        row, col, velocity, d_idx, shark_size = sharks.pop()
        next_row, next_col, next_d_idx = shark_move(row, col, velocity, d_idx)
        area[next_row][next_col].append((next_row, next_col, velocity, next_d_idx, shark_size))

print(catch_sum)