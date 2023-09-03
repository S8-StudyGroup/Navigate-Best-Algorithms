# [Programmers] 12946. 하노이의 탑
# 소요 시간 : 20분

def solution(n):
    
    def move(n, p_from, p_to, p_sub):
        if n == 1:
            answer.append([p_from, p_to])
            return
        
        move(n - 1, p_from, p_sub, p_to)
        answer.append([p_from, p_to])
        move(n - 1, p_sub, p_to, p_from)
        
    answer = []
    move(n, 1, 3, 2)
    
    return answer