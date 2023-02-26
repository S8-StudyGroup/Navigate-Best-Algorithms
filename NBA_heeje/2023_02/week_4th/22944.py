# [BOJ] 22944. 죽음의 비
# 소요 시간 : 00분

from collections import deque


def validator(health, shield, check_list):
    if health + shield > sum(check_list):
        return True
    elif health + shield == sum(check_list) and health > check_list[0]:
        return True
    return False


def bfs(start, health):
    start_y, start_x = start
    visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
    visited[start_y][start_x] = [health, 0]
    # visited = set()
    # visited.add((start_y, start_x))
    queue = deque()
    queue.append((start_y, start_x, health, 0, 0))

    while queue:
        y, x, health, shield, step = queue.popleft()

        if health == 0:
            continue
        
        for d in range(4):
            move_y, move_x = y + dy[d], x + dx[d]
            if (0 <= move_y < N and 0 <= move_x < N and validator(health, shield, visited[move_y][move_x])):
                # visited.add((move_y, move_x))
                visited[move_y][move_x] = [health, shield]
                if matrix[move_y][move_x] == ".":
                    if shield == 0:
                        queue.append((move_y, move_x, health - 1, shield, step + 1))
                    else:
                        queue.append((move_y, move_x, health, shield - 1, step + 1))
                elif matrix[move_y][move_x] == "U":
                    queue.append((move_y, move_x, health, D - 1, step + 1))
                elif matrix[move_y][move_x] == "E":
                    return step + 1
                
    return -1

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# N: 정사각형 격자의 한 변의 길이
# H: 현재 체력
# D: 우산의 내구도
N, H, D = map(int, input().split())
matrix = []
start = (0, 0)
for j in range(N):
    row = list(input())
    for i in range(N):
        if row[i] == "S":
            start = (j, i)

    matrix.append(row)

print(bfs(start, H))
    