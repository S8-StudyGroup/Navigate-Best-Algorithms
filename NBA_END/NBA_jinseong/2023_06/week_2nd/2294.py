# [BOJ] 2294. 동전 2
# 소요 시간 : 60분

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

cnt = [0] * (k + 1)
for i in range(1, k + 1):
    for coin in coins:
        index = i - coin
        # index가 음수면 넘어가기
        if index < 0:
            continue
        # 해당 코인을 이용한 갯수를 구하기 위한 이전 갯수가 -1 인 경우 넘어가기
        if cnt[index] == -1:
            continue
        temp = cnt[index] + 1
        # 동전 갯수를 처음 넣을 때
        if cnt[i] == 0:
            cnt[i] = temp
        # 동전 갯수가 존재할 때 비교
        elif cnt[i] > temp:
            cnt[i] = temp
    if cnt[i] == 0:
        cnt[i] = -1
print(cnt.pop())
