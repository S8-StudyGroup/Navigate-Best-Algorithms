# [Programmers 2023 KAKAO BLIND TEST] 1. 개인정보 수집 유효기간
# 소요 시간 : 00분

# 약관 판단 후 유효기간을 지나 파기되어야 한다면 True 반환
def is_expired(current_year: int, current_month: int, current_day: int, year: int, month: int, day: int, value: int) -> bool:
    month += value

    if month > 12:
        year += (month - 1) // 12
        month = (month - 1) % 12 + 1

    if current_year != year:
        return current_year > year

    if current_month != month:
        return current_month > month

    return current_day >= day


def solution(today: str, terms: list, privacies: list) -> list:
    answer = []
    current_year, current_month, current_day = map(int, today.split('.'))
    expiration = {key: int(value)
                  for key, value in (term.split(' ') for term in terms)}

    for idx, privacie in enumerate(privacies):
        date, key = privacie.split(' ')
        year, month, day = map(int, date.split('.'))
        value = expiration[key]

        # 유효기간 확인
        if is_expired(current_year, current_month, current_day, year, month, day, value):
            answer.append(idx + 1)

    return answer
