# [BOJ] 2096. 내려가기
# 소요 시간 : 00분


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

min_board = board[0][:]
max_board = board[0][:]

for i in range(1, N):
    temp_board = max_board[:]
    max_board[0] = board[i][0] + max(temp_board[0], temp_board[1])
    max_board[1] = board[i][1] + max(temp_board[0], temp_board[1], temp_board[2])
    max_board[2] = board[i][2] + max(temp_board[1], temp_board[2])

    temp_board = min_board[:]
    min_board[0] = board[i][0] + min(temp_board[0], temp_board[1])
    min_board[1] = board[i][1] + min(temp_board[0], temp_board[1], temp_board[2])
    min_board[2] = board[i][2] + min(temp_board[1], temp_board[2])

print(max(*max_board), min(*min_board))