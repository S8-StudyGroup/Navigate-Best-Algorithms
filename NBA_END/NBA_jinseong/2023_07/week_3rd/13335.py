# [BOJ] 13335. 트럭
# 소요 시간 : 40분

truck_num, max_num, max_weight = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = [0] * max_num
ans = 1
bridge.pop(0)
bridge.append(trucks.pop(0))
while trucks:
    ans += 1
    next_truck = trucks[0]
    # 최대 하중 이하인 경우
    if sum(bridge[1:max_num]) + next_truck <= max_weight:
        trucks.pop(0)
        bridge.append(next_truck)
    else: # 최대 하중을 넘는경우
        bridge.append(0)
    bridge.pop(0)
ans += max_num
print(ans)
