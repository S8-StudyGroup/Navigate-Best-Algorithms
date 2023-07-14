# [BOJ] 13335. 트럭
# 소요 시간 : 15분

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
bridge = []
time = 0

while trucks or bridge:
    time += 1
    if bridge:
        for truck in bridge:
            truck[1] -= 1
        if bridge[0][1] == 0:
            bridge.pop(0)                

    if trucks:
        if trucks[0] + sum(list(map(lambda x: x[0], bridge))) <= L:
            bridge.append([trucks.pop(0), w])

print(time)
        