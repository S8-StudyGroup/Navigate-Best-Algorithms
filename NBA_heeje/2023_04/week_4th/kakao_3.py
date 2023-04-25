# [Programmers 2023 KAKAO BLIND TEST] 3. 이모티콘 할인행사
# 소요 시간 : 90분

def solution(users, emoticons):
    
    def dfs(idx, discount_rate):
        nonlocal max_cnt_user, max_benefit
        if idx == len(emoticons):

            cnt_user = 0
            total_benefit = 0
            for i in range(len(users)):
                price = 0
                for j in range(len(discount_rate)):
                    if users[i][0] <= 100 * discount_rate[j]:
                        price += emoticons[j] * (1 - discount_rate[j])
                if price >= users[i][1]:
                    cnt_user += 1
                else:
                    total_benefit += price
            if max_cnt_user < cnt_user:
                max_cnt_user = cnt_user
                max_benefit = total_benefit
            
            if max_cnt_user == cnt_user and max_benefit < total_benefit:
                max_benefit = total_benefit
            return
        
        for i in range(4, 0, -1):
            discount_rate[idx] = 0.1 * i
            dfs(idx + 1, discount_rate[:])
    max_cnt_user = 0
    max_benefit = 0
    dfs(0, [0] * len(emoticons))
    return [max_cnt_user, int(max_benefit)]