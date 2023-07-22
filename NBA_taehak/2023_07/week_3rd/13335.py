# [BOJ] 13335. 트럭
# 소요 시간 : 00분

# n개의 트럭, w 단위길이, L 최대하중
from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

time = 0
on_bridge = deque([0]*w)
on_bridge_sum = 0

while trucks:

    time += 1

    # 기존 다리 위에서 트럭이 한대 빠져나감
    truck_out = on_bridge.popleft()
    on_bridge_sum -= truck_out

    # 최대하중을 견딜수 있으면 다음 트럭 다리위로
    truck = trucks[0]
    if on_bridge_sum + truck <= L:
        trucks.popleft()
        on_bridge.append(truck)
        on_bridge_sum += truck
    else:
        on_bridge.append(0)

print(time + w)