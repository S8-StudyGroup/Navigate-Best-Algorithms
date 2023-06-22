# [Programmers] 92344. 파괴되지 않은 건물
# 소요 시간 : 00분

def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    # 누적합 이용
    
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    for skill_type, r1, c1, r2, c2, degree in skill:
        if skill_type == 2:
            degree *= -1
        prefix_sum[r1][c1] += -degree
        prefix_sum[r1][c2 + 1] += degree
        prefix_sum[r2 + 1][c1] += degree
        prefix_sum[r2 + 1][c2 + 1] += -degree
        
    for i in range(N):
        for j in range(1, M):
            prefix_sum[i][j] += prefix_sum[i][j - 1]
    
    for j in range(M):
        for i in range(1, N):
            prefix_sum[i][j] += prefix_sum[i - 1][j]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] + prefix_sum[i][j] > 0:
                answer += 1
            
    return answer