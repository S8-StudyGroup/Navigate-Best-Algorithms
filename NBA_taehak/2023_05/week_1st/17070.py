# [BOJ] 17070. 파이프 옮기기 1
# 소요 시간 : 00분
# import sys

# # 0 가로, 1 세로, 2 대각선
# nextdirection = {0:[0, 2], 1:[1, 2], 2:[0, 1, 2]}
# fill = {0: [(0, 1)], 1:[(1, 0)], 2:[(0, 1), (1, 0), (1, 1)]}

# house_size = int(sys.stdin.readline())
# house = [list(map(int, sys.stdin.readline().split())) for _ in range(house_size)]

# answer = 0


# def inrange(r, c):
#     return 0 <= r < house_size and 0 <= c < house_size


# def cycle(r, c, di):
#     global answer
    
#     if (r, c) == (house_size-1, house_size-1):
#         answer += 1
#         return

#     # 다음에 갈수 있는 방향에 대해서
#     for nextdi in nextdirection[di]:
#         cango = True
#         # 벽에 걸리는지 체크
#         for pr, pc in fill[nextdi]:
#             nr = r + pr
#             nc = c + pc
#             # 범위 밖이거나 벽일경우 진행x
#             if not inrange(nr, nc) or house[nr][nc] == 1:
#                 cango = False

#         if not cango:
#             continue

#         # 진행
#         if nextdi == 0:
#             cycle(r, c+1, nextdi)
#         elif nextdi == 1:
#             cycle(r+1, c, nextdi)
#         else:
#             cycle(r+1, c+1, nextdi)


# cycle(0, 1, 0)
# print(answer)


## 2
house_size = int(input())
house = [list(map(int, input().split())) for _ in range(house_size)]

# 3가지 경우로 메모 [가로, 세로, 대각선]
dp = [[[0]*3 for _ in range(house_size+1)] for _ in range(house_size+1)]

dp[0][1][0] = 1

for r in range(house_size):
    for c in range(house_size):
        # 벽일경우
        if house[r][c] == 1:
            dp[r+1][c+1][2] = 0
            dp[r+1][c][1] = 0
            dp[r+1][c][2] = 0
            dp[r][c+1][0] = 0
            dp[r][c+1][2] = 0
            continue
        # 가로방향 = 가로방향, 대각선방향으로 왔을때
        dp[r][c+1][0] += dp[r][c][0] + dp[r][c][2]

        # 세로방향 = 세로방향, 대각선방향으로 왔을때
        dp[r+1][c][1] += dp[r][c][1] + dp[r][c][2]

        # 대각선방향 = 가로, 세로, 대각선 전부
        dp[r+1][c+1][2] += sum(dp[r][c])

print(sum(dp[house_size][house_size]))