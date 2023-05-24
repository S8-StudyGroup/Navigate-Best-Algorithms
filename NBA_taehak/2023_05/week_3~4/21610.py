# [BOJ] 21610. 마법사 상어와 비바라기
# 소요 시간 : 00분
from collections import deque
import sys
input = sys.stdin.readline

delta = [
    (0, 0),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
         ]

delta_di = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

area_size, move_cnt = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(area_size)]
# (방향, 거리)
commands = [list(map(int, input().split())) for _ in range(move_cnt)]

cloud = deque([
    (area_size - 1, 0),
    (area_size - 1, 1),
    (area_size - 2, 0),
    (area_size - 2, 1),
          ])

# 1. 모든 구름 이동
for delta_idx, distance in commands:
    for _ in range(len(cloud)):
        r, c = cloud.popleft()
        nr = (r + distance * delta[delta_idx][0]) % area_size
        nc = (c + distance * delta[delta_idx][1]) % area_size
        # 2. 물의 양 증가
        cloud.append((nr, nc))
        area[nr][nc] += 1
    # 4. 물복사
    for r, c in cloud:
        for dr, dc in delta_di:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < area_size and 0 <= nc < area_size and area[nr][nc]:
                area[r][c] += 1
    # 5. 구름 생성
    next_cloud = deque([])
    for r in range(area_size):
        for c in range(area_size):
            if area[r][c] >= 2 and (r, c) not in cloud:
                area[r][c] -= 2
                next_cloud.append((r, c))
    cloud = next_cloud

print(sum(map(sum, area)))