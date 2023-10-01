# [Programmers] 160585. 혼자서 하는 틱택토
# 소요 시간 : 00분

def count_pieces(board):
    cnt_o, cnt_x = 0, 0
    for line in board:
        for value in line:
            if value == "O":
                cnt_o += 1
            elif value == "X":
                cnt_x += 1
    return cnt_o, cnt_x


def check_bingo(board, value1, value2, value3):
    if value1 == value2 == value3 != ".":
        if value1 == "O":
            return True, False
        elif value1 == "X":
            return False, True
    return False, False


def solution(board):
    cnt_o, cnt_x = count_pieces(board)

    # 개수 확인
    if cnt_x > cnt_o:
        return 0
    if cnt_o - cnt_x > 1:
        return 0

    # 빙고 확인
    win_o, win_x = False, False
    for i in range(3):
        row_o, row_x = check_bingo(
            board, board[i][0], board[i][1], board[i][2])
        col_o, col_x = check_bingo(
            board, board[0][i], board[1][i], board[2][i])
        win_o |= row_o or col_o
        win_x |= row_x or col_x
    diag_o1, diag_x1 = check_bingo(
        board, board[0][0], board[1][1], board[2][2])
    diag_o2, diag_x2 = check_bingo(
        board, board[0][2], board[1][1], board[2][0])
    win_o |= diag_o1 or diag_o2
    win_x |= diag_x1 or diag_x2

    # 결과 반환
    if win_o and win_x:
        return 0
    if win_o:
        if cnt_o - cnt_x != 1:
            return 0
    if win_x:
        if cnt_o != cnt_x:
            return 0
    return 1
