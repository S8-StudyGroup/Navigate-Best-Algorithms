# [BOJ] 2146. 다리 만들기
# 소요 시간 : 00분
import sys
from collections import deque
input = sys.stdin.readline

# Input
size = int(input())
area = [list(map(int, input().split())) for _ in range(size)]


# island marking
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def marking(start_r, start_c, num):
    stack = [(start_r, start_c)]
    area[start_r][start_c] = num

    while stack:
        r, c = stack.pop()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < size and 0 <= nc < size and area[nr][nc] == 1:
                area[nr][nc] = num
                stack.append((nr, nc))


num = 2
for r in range(size):
    for c in range(size):
        if area[r][c] == 1:
            marking(r, c, num)
            num += 1


# find bridge
def connect_bridge(start_r, start_c):
    global min_value
    length = 0
    my_island = area[start_r][start_c]
    visited = [[False] * size for _ in range(size)]
    que = deque([(start_r, start_c)])

    while que:
        for _ in range(len(que)):
            r, c = que.popleft()
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < size and 0 <= nc < size:
                    if area[nr][nc] > 0 and area[nr][nc] != my_island:
                        min_value = length
                        return
                    if not visited[nr][nc] and area[nr][nc] == 0:
                        visited[nr][nc] = True
                        que.append((nr, nc))
        length += 1
        if length > min_value:
            return


min_value = 999
for r in range(size):
    for c in range(size):
        if area[r][c] > 0:
            connect_bridge(r, c)

# OutPut
print(min_value)