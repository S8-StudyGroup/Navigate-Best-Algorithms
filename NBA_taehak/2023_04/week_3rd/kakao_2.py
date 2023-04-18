# [Programmers 2023 KAKAO BLIND TEST] 2. 택배 배달과 수거하기
# 소요 시간 : 00분
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_cnt = 0
    pickup_cnt = 0

    for idx in range(n - 1, -1, -1):
        deliver_cnt += deliveries[idx]
        pickup_cnt += pickups[idx]

        while deliver_cnt > 0 or pickup_cnt > 0:
            deliver_cnt -= cap
            pickup_cnt -= cap
            answer += 2 * (idx + 1)
    
    return answer


print(solution(	4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))