# [BOJ] 17837. 새로운 게임 2
# 소요 시간 : 00분


def is_blue(piece):
    y, x, d = piece
    return not (0 <= y + dy[d] < N and 0 <= x + dx[d] < N) or board[y + dy[d]][x + dx[d]] == 2


def move(idx):
    y, x, d = piece_info[idx]

    # 가려는 곳이 파란색일 경우
    if is_blue(piece_info[idx]):
        if piece_info[idx][2] < 2:
            if piece_info[idx][2] == 0:
                piece_info[idx][2] = 1
            else:
                piece_info[idx][2] = 0
        else:
            if piece_info[idx][2] == 2:
                piece_info[idx][2] = 3
            else:
                piece_info[idx][2] = 2
        
        if not is_blue(piece_info[idx]):
            return move(idx)
    

    # 가려는 곳이 흰색인 경우
    elif board[y + dy[d]][x + dx[d]] == 0:
        piece_group = get_piece_group(y, x, d, idx)
        piece_in_board[y + dy[d]][x + dx[d]].extend(piece_group)
        if len(piece_in_board[y + dy[d]][x + dx[d]]) >= 4:
            return "Game End"
    
    # 가려는 곳이 빨간색인 경우
    else:
        piece_group = get_piece_group(y, x, d, idx)
        piece_in_board[y + dy[d]][x + dx[d]].extend(piece_group[::-1])

        if len(piece_in_board[y + dy[d]][x + dx[d]]) >= 4:
            return "Game End"
    
    return "Next Piece"

def get_piece_group(y, x, d, idx):
    for i, piece_idx in enumerate(piece_in_board[y][x]):
        if piece_idx == idx:
            piece_in_board[y][x], piece_group = piece_in_board[y][x][:i], piece_in_board[y][x][i:]
            for piece in piece_group:
                piece_info[piece][0] += dy[d]
                piece_info[piece][1] += dx[d]
            return piece_group


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
piece_in_board = [[[] * N for _ in range(N)] for _ in range(N)]
piece_info = {}
for idx in range(1, K + 1):
    y, x, d = map(int, input().split())
    piece_in_board[y - 1][x - 1].append(idx)
    piece_info[idx] = [y - 1, x - 1, d - 1]

turn = 0

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
breaker = False

while True:
    turn += 1
    if turn > 1000:
        break

    for idx in range(1, K + 1):
        if move(idx) == "Game End":
            breaker = True
            break
    
    if breaker:
        break

print(turn if breaker else -1)
