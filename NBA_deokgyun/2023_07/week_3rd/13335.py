# [BOJ] 13335. 트럭
# 소요 시간 : 00분

num, length, weight = map(int, input().split())

trucks = list(map(int, input().split()))

now_weight = 0
time_cnt = 0
on_bridge = []
while True:
    time_cnt += 1
    if on_bridge and on_bridge[0][1] == time_cnt:
        now_weight -= on_bridge.pop(0)[0]
    if trucks and weight - now_weight >= trucks[0]:
        on_bridge.append([trucks.pop(0), time_cnt + length])
        now_weight += on_bridge[-1][0]
        if not trucks:
            print(on_bridge[-1][1])
            break