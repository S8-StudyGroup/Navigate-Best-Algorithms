# [Programmers] 152996. 인사고과
# 소요 시간 : 00분

def solution(scores):
    answer = 0
    target_a, target_b = scores[0]
    target_score = target_a + target_b

    scores.sort(key=lambda x: (-x[0], x[1]))
    memo = 0
    
    for a, b in scores:
        if target_a < a and target_b < b:
            return -1
        
        if b >= memo:
            memo = b
            if a + b > target_score:
                answer += 1
            
    return answer + 1