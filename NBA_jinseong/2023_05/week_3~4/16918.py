# [BOJ] 16918. 봄버맨
# 소요 시간 : 120분

R, C, N = map(int, input().split())
toExplode = []
board = []
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

for i in range(R):
    temp_board = list(map(lambda x: 1 if x == 'O' else x, list(input())))
    board.append(temp_board)

for n in range(2, N + 1):
    for i in range(R):
        for j in range(C):
            # 폭탄이 설치된 곳 1초 지남
            if isinstance(board[i][j], int):
                board[i][j] += 1
            # 설치
            elif board[i][j] == '.':
                board[i][j] = 0
            # 담기
            if board[i][j] == 3:
                toExplode.append([i, j])
    # 폭파
    for point in toExplode:
        a, b = point
        board[a][b] = '.'
        for d in range(4):
            ni = a + di[d]
            nj = b + dj[d]
            if 0 <= ni < R and 0 <= nj < C:
                board[ni][nj] = '.'
    toExplode = []

for i in range(R):
    for j in range(C):
        # 마무리
        if isinstance(board[i][j], int):
            print('O', end='')
        else:
            print('.', end='')
    print()
