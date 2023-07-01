# [Programmers] 92344. 파괴되지 않은 건물
# 소요 시간 : ∞분

def solution(board, skill):
    n = len(board)
    m = len(board[0])
    
    building = [[0] * (m + 1) for _ in range(n + 1)] 
    
    # 1. 누적합을 진행할 building 배열 채우기
    for case in skill:
        type, r1, c1, r2, c2, cnt = case
        
        if type == 1:
            cnt = -cnt
        
        building[r1][c1] += cnt
        building[r2 + 1][c1] -= cnt

        building[r2 + 1][c2 + 1] += cnt
        building[r1][c2 + 1] -= cnt
    
    # 2 - 1. 채운 building 배열에서 누적합 진행 (가로 우선)
    for i in range(n):
        for j in range(1, m):
            building[i][j] += building[i][j - 1]
            
    # 2 - 2. 채운 building 배열에서 누적합 진행 (세로 기준)
    for j in range(m):
        for i in range(1, n):
            building[i][j] += building[i - 1][j]
            
    # 3. board와 building 더하기
    answer = 0
    
    for i in range(n):
        for j in range(m):
            power = board[i][j] + building[i][j]
            if power > 0:
                answer += 1
                
    # print(answer)
    return answer