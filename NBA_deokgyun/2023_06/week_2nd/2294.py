# [BOJ] 2294. 동전 2
# 소요 시간 : 00분

max_cnt = 100

def selecting(coins, target, cnt):
    global max_cnt
    if cnt >= max_cnt:
        return
    if target < 0:
        return
    elif target == 0:
        if max_cnt > cnt:
            max_cnt = cnt
        return
    for i in range(len(coins)):
        selecting(coins, target - coins[i], cnt + 1)
    

n, k = map(int, input().split())

coins = set()

for _ in range(n):
    coins.add(int(input()))

coins_list = list(coins)
coins_list.sort(reverse=True)

selecting(coins_list, k, 0)

print(max_cnt)