# [Programmers] 160585. 혼자서 하는 틱택토
# 소요 시간 : 00분

def solution(board):
    bingo_set = set([(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)])
    board_info = {"O": [], "X": []}
    for y in range(3):
        for x in range(3):
            if board[y][x] != ".":
                board_info[board[y][x]].append(y * 3 + x)
    
    len_O, len_X = len(board_info["O"]), len(board_info["X"])
    
    # O보다 X가 더 많거나 O이 X보다 2개 이상 많을 경우
    if len_O < len_X or len_O > len_X + 1:
        return 0
    
    bingo_O, bingo_X = 0, 0
    for bingo in bingo_set:
        for val in bingo:
            if val not in board_info["O"]:
                break
        else:
            bingo_O += 1
    
        for val in bingo:
            if val not in board_info["X"]:
                break
        else:
            bingo_X += 1
    
    # 빙고가 2개 이상일 경우
    if bingo_O + bingo_X > 2:
        return 0
    
    # O 빙고인데 X랑 개수가 같거나 X 빙고인데 O가 더 많은 경우
    if (bingo_O and len_O == len_X) or (bingo_X and len_O > len_X):
        return 0
    
    return 1