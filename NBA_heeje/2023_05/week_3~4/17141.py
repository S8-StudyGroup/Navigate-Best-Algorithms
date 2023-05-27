# [BOJ] 17141. 연구소 2
# 소요 시간 : 50분

from itertools import combinations
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# 바이러스 확산 함수
def bfs(init_virus_list) -> int:
    copy_laboratory = []
    queue = deque()
    time = 0
    cnt_blank = 0

    # 깊은 복사
    for i in range(N):
        copy_laboratory.append(laboratory[i][:])
    
    # 이미 0 ~ 2라는 숫자를 사용중이라 3부터 시작
    for y, x in init_virus_list:
        copy_laboratory[y][x] = 3
        queue.append((y, x))
    
    while queue:
        time += 1
        for _ in range(len(queue)):
            y, x = queue.popleft()
            
            # 연구소 내부 타일 중 0이거나 2인 부분은 처음 이동하는 부분!
            # 이동 횟수 + 1한 값을 넣어준다.
            for d in range(4):
                move_y, move_x = y + dy[d] , x + dx[d]
                if 0 <= move_y < N and 0 <= move_x < N and (copy_laboratory[move_y][move_x] == 0 or copy_laboratory[move_y][move_x] == 2):
                    copy_laboratory[move_y][move_x] = copy_laboratory[y][x] + 1
                    cnt_blank += 1
                    queue.append((move_y, move_x))
    
    if cnt_blank == total_blank:
        return time
    else:
        return -1
                    



N, M = map(int, input().split())

laboratory = []
virus_point_list = []
total_blank = -M
min_time = 99999999

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            virus_point_list.append((i, j))
            total_blank += 1
        elif row[j] == 0:
            total_blank += 1
    laboratory.append(row)

for case in combinations(virus_point_list, M):
    time = bfs(case)
    if time == -1:
        min_time = max(min_time, time)
    else:
        min_time = min(min_time, time)

if min_time == 99999999:
    print(-1)
else:
    print(min_time - 1)