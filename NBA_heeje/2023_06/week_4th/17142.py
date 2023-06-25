# [BOJ] 17142. 연구소 3
# 소요 시간 : 30분

def bfs(virus_case, blank, min_time):
    queue = deque(virus_case)

    while queue:
        y, x = queue.popleft()

        if copied_matrix[y][x] - 3 >= min_time:
            return min_time

        for d in range(4):
            move_y, move_x = y + dy[d], x + dx[d]
            if 0 <= move_y < N and 0 <= move_x < N and copied_matrix[move_y][move_x] in [0, 2]:
                queue.append((move_y, move_x))
                if copied_matrix[move_y][move_x] == 0:
                    blank -= 1
                    if blank == 0:
                        return copied_matrix[y][x] - 2
                    
                copied_matrix[move_y][move_x] = copied_matrix[y][x] + 1

    return -1


import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())
matrix = []
virus_list = []
blank = N ** 2
min_time = float("inf")
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):

        # 벽일 때
        if row[j] == 1:
            blank -= 1
        
        # 비활성 바이러스일 때
        if row[j] == 2:
            virus_list.append((i, j))
            blank -= 1

    matrix.append(row)

if blank == 0:
    print(0)
else:
    for virus_case in combinations(virus_list, M):

        copied_matrix = []
        for i in range(N):
            copied_matrix.append(matrix[i][:])

        for y, x in virus_case:
            copied_matrix[y][x] = 3

        time = bfs(virus_case, blank, min_time)
        min_time = min_time if time == -1 else min(min_time, time)

    print(min_time if min_time < float("inf") else -1)