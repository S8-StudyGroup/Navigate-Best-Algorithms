# [BOJ] 7562. 나이트의 이동
# 소요 시간 : 30분

# 나이트의 이동
from collections import deque


def inrange(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    else:
        return False


def cango(r, c):
    cango_list = []

    for i in [1, -1]:
        for j in [1, -1]:
            for (d_r, d_c) in [(1, 2), (2, 1)]:
                next_r = r + d_r * i
                next_c = c + d_c * j
                cango_list.append((next_r, next_c))

    return(cango_list)


def knight_bfs(start_r, start_c, board_size):
    if board[start_r][start_c] == -1:
        print(0)
        return
    
    board[start_r][start_c] = 1
    que = deque([(start_r, start_c, 0)])

    while que:
        r, c, step = que.popleft()
        for next_r, next_c in cango(r, c):
            if inrange(next_r, next_c, board_size):
                if board[next_r][next_c] == -1:
                    print(step + 1)
                    return
                elif board[next_r][next_c] == 0:
                    board[next_r][next_c] = 1
                    que.append((next_r, next_c, step + 1))


case_cnt = int(input())

for _ in range(case_cnt):
    board_size = int(input())
    start_r, start_c = map(int, input().split())
    target_r, target_c = map(int, input().split())

    board = [[0] * board_size for _ in range(board_size)]
    board[target_r][target_c] = -1

    knight_bfs(start_r, start_c, board_size)