# [BOJ] 1986. 체스
# 소요 시간 : 30분

N, M = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
# 빈칸: 0, 말있는칸: 1, 위험한칸: 2

queens = []
queen_temp = list(map(int, input().split()))
for i in range(queen_temp[0]):
    queens.append([queen_temp[2 * i + 1] - 1, queen_temp[2 * i + 2] - 1])

knights = []
knight_temp = list(map(int, input().split()))
for i in range(knight_temp[0]):
    knights.append([knight_temp[2 * i + 1] - 1, knight_temp[2 * i + 2] - 1])

pawns = []
pawn_temp = list(map(int, input().split()))
for i in range(pawn_temp[0]):
    pawns.append([pawn_temp[2 * i + 1] - 1, pawn_temp[2 * i + 2] - 1])


# 말 위치 마킹
def mark(array):
    for loc in array:
        i, j = loc
        board[i][j] = 1


def queen_move(array):
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    # 각 방향에 대해 위험 처리
    for loc in array:
        i, j = loc
        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]
            # 범위 안이거나 지나는 자리에 다른 말이 있는 경우 해당 방향 스탑
            while 0 <= ni < N and 0 <= nj < M:
                if board[ni][nj] != 1:
                    board[ni][nj] = 2
                    ni += di[d]
                    nj += dj[d]
                else:
                    break


def knight_move(array):
    di = [-2, -1, 1, 2, 2, 1, -1, -2]
    dj = [1, 2, 2, 1, -1, -2, -2, -1]
    for loc in array:
        i, j = loc
        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M:
                if board[ni][nj] != 1:
                    board[ni][nj] = 2


# 시작
mark(queens)
mark(knights)
mark(pawns)

queen_move(queens)
knight_move(knights)

cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            cnt += 1
print(cnt)



