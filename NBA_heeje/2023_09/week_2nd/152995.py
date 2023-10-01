# [Programmers] 152996. 인사고과
# 소요 시간 : 20분

def solution(scores):
    answer = 1          # 등수
    wanho = scores[0]   # 완호의 점수
    max_col_score = 0   # 동료 평가 점수 최댓값
    sorted_scores = sorted(scores, key=lambda x: (-x[0], x[1]))
    
    for score in sorted_scores:
        
        # 완호 인센티브 X
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        
        # 해당 사원의 인센티브 여부 확인
        if max_col_score <= score[1]:
            
            # 등수 계산
            if wanho[0] + wanho[1] < score[0] + score[1]:
                answer += 1
                
            # 동료 평가 점수 최댓값 갱신
            max_col_score = score[1]
                    
    return answer