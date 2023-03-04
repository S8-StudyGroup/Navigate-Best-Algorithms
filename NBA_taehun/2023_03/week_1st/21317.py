# [BOJ] 21317. 징검다리 건너기
# 소요 시간 : 00분

# 누적하기
# import sys

# input = sys.stdin.readline

# # def move():
# #     # 건너갈 돌이 없는 경우
# #     if N == 1:
# #         return 0
# #     # 한번만 건너가는 경우
# #     if N == 2:
# #         return jump_e[0][0]
    
# #     energy_list = [0, jump_e[0][0], min(energy_list[1] + jump_e[1][0], energy_list[0] + jump_e[0][1])]
# #     mega_jump_gap = []

# #     # 3번째 돌부터 시작
# #     for idx in range(3,N):
# #         # 다음 돌로 이동할 때 최소 에너지를 활용하는 경우
# #         jump_energy = min(energy_list[idx-1] + jump_e[idx-1][0], energy_list[idx-2] + jump_e[idx-2][1])
# #         # 매우 큰 점프를 하는 경우
# #         mega_jump = energy_list[idx-3] + K

# #         # 최소 에너지를 활용하는 경우와 매우 큰 점프를 하는 경우의 차이를 저장
# #         gap = jump_energy - mega_jump
# #         if gap > 0:
# #             mega_jump_gap.append(gap)
# #         energy_list.append(jump_energy)

# #     # 매우 큰 점프가 가능할 때
# #     if mega_jump_gap:
# #         # 가장 크게 에너지를 절약할 수 있는 경우를 사용
# #         total_e = energy_list[-1] - max(mega_jump_gap)
# #     else:
# #         total_e = energy_list[-1]
# #     return total_e



# N = int(input().strip())
# jump_e = [tuple(map(int, input().strip().split())) for _ in range(N-1)]
# K = int(input().strip())

# # result= move()
# # print(result)

# dp = [0]
# gap_list=[0]
# for idx in range(1,N):
#     if idx >= 3:
#         jump = min(dp[idx-1] + jump_e[idx-1][0], dp[idx-2] + jump_e[idx-2][1])
#         mega = dp[idx-3] + K
#         gap = jump - mega
#         if gap > 0:
#             gap_list.append(gap)
#         dp.append(jump)
#     elif idx == 2:
#         dp.append(min(dp[idx-1] + jump_e[idx-1][0], dp[idx-2] + jump_e[idx-2][1]))
#     elif idx == 1:
#         dp.append(jump_e[idx-1][0])
    
# print(dp[-1] - max(gap_list))


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