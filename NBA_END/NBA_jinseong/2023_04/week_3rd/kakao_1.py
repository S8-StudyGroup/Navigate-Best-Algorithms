# [Programmers 2023 KAKAO BLIND TEST] 1. 개인정보 수집 유효기간
# 소요 시간 : 60분

def solution(today, terms, privacies):
    answer = []
    temp_today = list(map(int, today.split('.')))
    converted_terms = dict()
    converted_today = temp_today[0] * 12 * 28 + temp_today[1] * 28 + temp_today[2]
    for term in terms:
        promise, period = term.split()
        period = int(period)
        converted_terms[promise] = period

    for i, privacy in enumerate(privacies):
        date, promise = privacy.split()
        year, month, day = map(int, date.split('.'))
        expire = year * 12 * 28 + month * 28 + day + converted_terms[promise] * 28 - 1
        if expire < converted_today:
            answer.append(i + 1)
    return answer


