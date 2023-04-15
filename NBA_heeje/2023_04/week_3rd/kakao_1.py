# [Programmers 2023 KAKAO BLIND TEST] 1. 개인정보 수집 유효기간
# 소요 시간 : 30분

def solution(today, terms, privacies):
    
    today_y, today_m, today_d = map(int, today.split("."))
    answer = []
    term_info = {}
    
    # 약관의 유효기간 정리
    for term in terms:
        term_type, period = term.split()
        term_info[term_type] = int(period)
    
    # 개인정보 수집 일자와 오늘 날짜 비교
    for idx, privacy in enumerate(privacies, start=1):
        expired_date, term_type = privacy.split()
        date_y, date_m, date_d = map(int, expired_date.split("."))
        
        date_d -= 1
        if date_d == 0:
            date_m -= 1
            date_d = 28
        
        date_m += term_info[term_type]
        if date_m > 12:
            date_y += (date_m - 1) // 12
            date_m = (date_m - 1) % 12 + 1
            
        if date_y < today_y or date_y == today_y and date_m < today_m or date_y == today_y and date_m == today_m and date_d < today_d:
            answer.append(idx)

    return answer