# [BOJ] 21317. 징검다리 건너기
# 소요 시간 : 00분

import sys

input = sys.stdin.readline

def min_move(dp, idx):
    return min(dp[idx-1] + jump_e[idx-1][0], dp[idx-2] + jump_e[idx-2][1])

def move(dp, n, flag):
    for idx in range(n,N):
        if idx >= 3:
            jump = min_move(dp, idx)
            # 메가 점프가 가능한 경우
            if not flag:
                mega = dp[idx-3] + K
                temp_dp = dp[:]
                temp_dp.append(mega)
                move(temp_dp, idx+1, True)
            dp.append(jump)
        elif idx == 2:
            dp.append(min_move(dp, idx))
        elif idx == 1:
            dp.append(jump_e[idx-1][0])
    min_result[0] = min(min_result[0], dp[-1])
    
N = int(input().strip())
jump_e = [tuple(map(int, input().strip().split())) for _ in range(N-1)]
K = int(input().strip())

arr = [0]
min_result = [9999999999]
move(arr, 0, False)
print(min_result[-1])