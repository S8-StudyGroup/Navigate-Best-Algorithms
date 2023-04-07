# [Programmers] 160585. 혼자서 하는 틱택토
# 소요 시간 : 00분

def ttt(board, char):
    '''
    board에 char로 승리조건을 만족하는 것이 있으면
    '''
    result = 0
    # 가로 체크
    triple = 3 * char
    for row in board:
        if row == triple:
            result += 1
        
    di_1 = 0
    di_2 = 0
    for idx in range(3):
        cnt_memo = 0
        # 세로 체크
        for row in board:
            if row[idx] == char:
                cnt_memo += 1
        if cnt_memo == 3:
            result += 1
        
        # 대각선 체크
        if board[idx][idx] == char:
            di_1 += 1
        
        if board[idx][2-idx] == char:
            di_2 += 1
    
    if di_1 == 3 or di_2 == 3:
        result += 1
    
    return result
        
        
            

def solution(board):
    # 규칙에 어긋난 경우
    # 1. x 가 o 보다 많을 경우 (선후공)
    # 2. O 개수랑 x개수 차이가 2 이상일때 (차례 무시)
    # 3. O나 X가 빙고를 완성했는데 둘 차이 갯수가 올바르지 않을 경우 (종료해도 계속 했을 경우)
    
    # O, X 개수 파악
    ocnt = 0
    xcnt = 0
    for r in range(3):
        for c in range(3):
            if board[r][c] == 'O':
                ocnt += 1
            elif board[r][c] == 'X':
                xcnt += 1
    
    # CHECK CASE 1
    if ocnt < xcnt:
        return 0
        
    # CHECK CASE 2
    if ocnt - xcnt > 1:
        return 0
    
    # CHECK CASE 3
    if ttt(board, 'O') > 0 and xcnt != ocnt - 1:
        return 0    
    if ttt(board, 'X') > 0 and xcnt != ocnt:
        return 0
    
    return 1