# [Programmers 2023 KAKAO BLIND TEST] 3. 이모티콘 할인행사
# 소요 시간 : 00분

data = [10, 20, 30, 40]
discount = []


def dfs(temp, depth):

    if depth == len(temp):
        discount.append(temp[:])
        return

    for d in data:
        temp[depth] += d
        dfs(temp, depth + 1)
        temp[depth] -= d


def solution(users, emoticons):
    max_users = 0
    max_price = 0

    dfs([0] * len(emoticons), 0)

    for d in range(len(discount)):
        join, price = 0, [0] * len(users)
        for e in range(len(emoticons)):
            for u in range(len(users)):
                if users[u][0] <= discount[d][e]:
                    price[u] += emoticons[e] * (100 - discount[d][e]) / 100

        for u in range(len(users)):
            if price[u] >= users[u][1]:
                join += 1
                price[u] = 0

        if join >= max_users:
            if join == max_users:
                max_price = max(max_price, sum(price))
            else:
                max_price = sum(price)
            max_users = join

    return max_users, max_price
