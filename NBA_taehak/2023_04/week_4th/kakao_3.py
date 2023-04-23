# [Programmers 2023 KAKAO BLIND TEST] 3. 이모티콘 할인행사
# 소요 시간 : 00분

'''
1. 적용 할인율 10, 20, 30, 40 
2. 유저별로 플러스 요금에 가입할 수 있는 할인율 경우의수를 모두 구하기? 이모티콘 최대개수 7개 -> 4^7 -> 16000
'''

from itertools import product


def checkuser(user, emoticons, discount):
    '''
    @params
        user [할인율, 기준가격]
        emoticons 이모티콘 가격[]
        discount 최종가격 = 가격 * (1 - 할인율)
    @return
        (플러스요금제 가입여부, 이모티콘 구매 금액합)
    '''
    user_discount, user_plus = user
    user_discount = 1 -  user_discount / 100
    isplus = 0
    user_sum = 0

    for idx, emoticon in enumerate(emoticons):
        if discount[idx] <= user_discount:
            user_sum += emoticon * discount[idx]
    
    if user_sum >= user_plus:
        isplus = 1
        user_sum = 0

    return (isplus, user_sum)


discounts = [0.9, 0.8, 0.7, 0.6]

def solution(users, emoticons):
    emoticon_cnt = len(emoticons)
    answer = [0, 0]

    for discount in product(discounts, repeat=emoticon_cnt):
        plus_sum = 0
        fee_sum = 0
        for user in users:
            isplus, user_sum = checkuser(user, emoticons, discount)
            plus_sum += isplus
            fee_sum += user_sum
        
        # 1번 목표
        if plus_sum > answer[0]:
            answer = [plus_sum, fee_sum]
        # 2번 목표
        elif plus_sum == answer[0] and fee_sum > answer[1]:
            answer[1] = fee_sum

        answer[1] = int(answer[1])
    return answer