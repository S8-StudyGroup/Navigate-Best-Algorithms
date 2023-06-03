import sys; input = sys.stdin.readline
from itertools import combinations

n = int(input())

S = [list(map(int, input().split())) for _ in range(n)]
row, col = [sum(i) for i in S], [sum(i) for i in zip(*S)]
arr = [i+j for i, j in zip(row, col)]
total_sum = sum(arr) // 2

ans = float('inf')
for r in range(n // 2, 0, -1):
    for combi in combinations(arr, r):
        ans = min(ans, abs(total_sum - sum(combi)))
        
        if ans == 0:
            break
    if ans == 0:
        break
            
print(ans)

# # [BOJ] 15661. 링크와 스타트
# # 소요 시간 : 20분

# from itertools import combinations
# import sys
# input = sys.stdin.readline

# N = int(input())

# matrix = [list(map(int, input().split())) for _ in range(N)]
# min_difference = 99999999

# for cnt_member in range(2, N // 2 + 1):
#     for start_team in combinations(range(N), cnt_member):
#         # link_team = set(range(N)) - set(start_team)

#         link_team = []
#         for i in range(N):
#             if i not in start_team:
#                 link_team.append(i)

#         power_start = 0
#         power_link = 0

#         for y in range(len(start_team) - 1):
#             for x in range(y + 1, len(start_team)):
#                 power_start += matrix[start_team[y]][start_team[x]] + matrix[start_team[x]][start_team[y]]

#         for y in range(len(link_team) - 1):
#             for x in range(y + 1, len(link_team)):
#                 power_link += matrix[link_team[y]][link_team[x]] + matrix[link_team[x]][link_team[y]]
        
#         # for y, x in combinations(start_team, 2):
#         #     power_start += matrix[y][x] + matrix[x][y]

#         # for y, x in combinations(link_team, 2):
#         #     power_link += matrix[y][x] + matrix[x][y]
    
#         min_difference = min(min_difference, abs(power_start - power_link))

# print(min_difference)