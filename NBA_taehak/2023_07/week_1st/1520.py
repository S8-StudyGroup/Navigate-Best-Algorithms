# [BOJ] 1520. 내리막길
# 소요 시간 : 00분
from heapq import heappop, heappush

row_size, col_size = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(row_size)]


# bfs
# (-높이, row, col)
que = [(-area[0][0], 0, 0)]
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
visited = [[0] * col_size for _ in range(row_size)]
visited[0][0] = 1

while que:
    m_height, r, c = heappop(que)
    for dr, dc in delta:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < row_size and 0 <= nc < col_size and area[nr][nc] < area[r][c]:
            if visited[nr][nc] == 0:
                heappush(que, (-area[nr][nc], nr, nc))
            visited[nr][nc] += visited[r][c]

print(visited[row_size-1][col_size-1])



#### 시간초과
# import sys
# sys.setrecursionlimit(10 ** 8)

# row_size, col_size = map(int, input().split())
# area = [list(map(int, input().split())) for _ in range(row_size)]

# dp = [[0] * col_size for _ in range(row_size)]
# delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# row_max = row_size - 1
# col_max = col_size - 1

# def dfs(r=0, c=0):
#     dp[r][c] += 1

#     # 종료조건
#     if r == row_max and c == col_max:
#         return
    
#     # 이동
#     for dr, dc in delta:
#         nr = r + dr
#         nc = c + dc
#         if 0 <= nr < row_size and 0 <= nc < col_size and area[nr][nc] < area[r][c]:
#             dfs(nr, nc)


# dfs()
# #for line in dp: print(line)
# print(dp[row_max][col_max])