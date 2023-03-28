# [BOJ] 3055. 탈출
# 소요 시간 : 00분

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().strip().split())

forest = [list(map(lambda x: x, input().strip())) for _ in range(R)]
warter = deque()
dq = deque()
visited = set()

# 시작, 끝, 물의 위치 찾기
for r, arr in enumerate(forest):
    for c, value in enumerate(arr):
        if value == "D":
            goal = (r, c)
        elif value == "S":
            # 시작 위치 deque에 저장, 방문처리
            dq.append((r, c, 0))
            visited.add((r,c))
            forest[r][c] = "."
        elif value == "*":
            warter.append((r, c))
dq += warter

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

flag = True
result = "KAKTUS"
while flag and dq:
    value = dq.popleft()
    l = len(value)
    # 튜플의 길이가 2면 물 (row, column)
    if l == 2: # 물
        r, c = value
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and forest[nr][nc] == ".":
                forest[nr][nc] = "*"
                dq.append((nr, nc))
    # 튜플의 길이가 3이면 고슴도치 (row, column, count)
    elif l == 3: # 고슴도치
        r, c, cnt = value
        if forest[r][c] == "*":
            continue
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if (nr, nc) == goal:
                flag = False
                result = cnt + 1
                break
            if (nr, nc) not in visited and 0 <= nr < R and 0 <= nc < C and forest[nr][nc] == ".":
                dq.append((nr, nc, cnt+1))
                visited.add((nr, nc))

print(result)

