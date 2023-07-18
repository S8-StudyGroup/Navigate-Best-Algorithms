# [BOJ] 12100. 2048 (Easy)
# 소요 시간 : 00분


from collections import deque

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
answer, queue = 0, deque()

def get(i, j):
    if board[i][j]:
        queue.append(board[i][j])
        board[i][j] = 0

def merge(i, j, di, dj):
    while queue:
        x = queue.popleft()
        if not board[i][j]:
            board[i][j] = x
        elif board[i][j] == x:  # 값일치
            board[i][j] = x * 2
            i, j = i + di, j + dj
        else:  # 불일치
            i, j = i + di, j + dj
            board[i][j] = x

def move(d):  # k = 0,1,2,3 (위, 아래, 오른, 왼)
    # board[i][j]에서
    if d == 0:
        for j in range(N):
            for i in range(N):
                get(i, j)
            merge(0, j, 1, 0)
    if d == 1:
        for j in range(N):
            for i in range(N - 1, -1, -1):
                get(i, j)
            merge(N - 1, j, -1, 0)
    if d == 2:
        for i in range(N):
            for j in range(N):
                get(i, j)
            merge(i, 0, 0, 1)
    if d == 3:
        for i in range(N):
            for j in range(N - 1, -1, -1):
                get(i, j)
            merge(i, N - 1, 0, -1)

def start(depth):
    global board, answer
    if depth == 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return
    # 원본 보드 기억
    board_save = [x[:] for x in board]

    for d in range(4):
        move(d)
        start(depth + 1)
        board = [x[:] for x in board_save]

start(0)
print(answer)
