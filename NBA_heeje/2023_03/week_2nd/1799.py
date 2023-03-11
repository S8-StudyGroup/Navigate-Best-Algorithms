# [BOJ] 1799. 비숍
# 소요 시간 : 00분 07:02


def dfs(bishop_list, cnt):
    global max_cnt
    if cnt + len(bishop_list) < max_cnt:
        return
    max_cnt = max(max_cnt, len(bishop_list))

    for num in range(bishop_list[-1] + 1, N ** 2):
            y, x = num // N, num % N
            if board[y][x] == 1:
                change_list = []
                for d in range(4):
                    i = 1
                    while True:
                        move_y, move_x = y + dy[d] * i, x + dx[d] * i
                        if 0 <= move_y < N and 0 <= move_x < N:
                            if board[move_y][move_x] == 1:
                                change_list.append((move_y, move_x))
                                board[move_y][move_x] = 0
                            i += 1
                        else:
                            break
                    
                dfs(bishop_list + [num], cnt - len(change_list))

                for move_y, move_x in change_list:
                    board[move_y][move_x] = 1

dy = [-1, -1, 1, 1]
dx = [-1, 1, -1, 1]

N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
board = []
cnt_one = 0

for _ in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            cnt_one += 1
    board.append(row)

max_cnt = 0

dfs([-1], cnt_one)
print(max_cnt - 1)