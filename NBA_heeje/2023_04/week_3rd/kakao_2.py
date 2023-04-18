# [Programmers 2023 KAKAO BLIND TEST] 2. 택배 배달과 수거하기
# 소요 시간 : 00분

def solution(cap, n, deliveries, pickups):
    d_idx = p_idx = n - 1
    answer = 0
    while True:
        d_boxes = cap
        max_d_idx = -1
        while d_boxes > 0 and d_idx >= 0:
            if deliveries[d_idx] != 0:
                max_d_idx = max(max_d_idx, d_idx)
                if deliveries[d_idx] > d_boxes:
                    deliveries[d_idx] -= d_boxes
                    d_boxes = 0
                else:
                    d_boxes -= deliveries[d_idx]
                    deliveries[d_idx] = 0
                    d_idx -= 1
            else:
                d_idx -= 1

        p_boxes = cap
        max_p_idx = -1
        while p_boxes > 0 and p_idx >= 0:
            if pickups[p_idx] != 0:
                max_p_idx = max(max_p_idx, p_idx)
                if pickups[p_idx] > p_boxes:
                    pickups[p_idx] -= p_boxes
                    p_boxes = 0
                else:
                    p_boxes -= pickups[p_idx]
                    pickups[p_idx] = 0
                    p_idx -= 1
            else:
                p_idx -= 1
        
        if max_d_idx == max_p_idx == -1:
            break
        
        answer += (max(max_d_idx, max_p_idx) + 1) * 2    
                
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))