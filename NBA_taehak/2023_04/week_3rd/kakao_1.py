# [Programmers 2023 KAKAO BLIND TEST] 1. 개인정보 수집 유효기간
# 소요 시간 : 00분

def solution(today, terms, privacies):
    answer = []
    
    # 날짜 . 없애기
    year, month, day = map(int, today.split('.'))
    
    term_list = dict()
    
    for term_info in terms:        
        term, term_month = term_info.split()
        year_limit = year
        month_limit = month - int(term_month)
        day_limit = day + 1

        if day > 28:
            day_limit = 1
            month_limit += 1

        while month_limit <= 0:
            year_limit -= 1
            month_limit += 12
        
        term_list[term] = year_limit * 10000 + month_limit * 100 + day_limit
    
    print(term_list)

    for idx, privacy in enumerate(privacies, 1):
        date, term = privacy.split()
        if int(date.replace('.', '')) < term_list[term]:
            answer.append(idx)
        
    return answer


solution("2022.05.19", ["A 6", "B 100", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))