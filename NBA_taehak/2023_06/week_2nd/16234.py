# [BOJ] 16234. 인구 이동
# 소요 시간 : 00분

from collections import deque

size, left, right = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(size)]

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        r, c = queue.popleft()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < size and 0 <= nc < size and visited[nr][nc] == 0:
                if left <= abs(area[nr][nc] - area[r][c]) <= right:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
                    union.append((nr, nc))
    return union               

result = 0
while True:
    visited = [[0 for _ in range(size)] for _ in range(size)]
    flag = 0
    for i in range(size):
        for j in range(size):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                
                if len(country) > 1:
                    flag = 1
                    people = sum(area[x][y] for x, y in country) // len(country)
                    
                    for x, y in country:
                        area[x][y] = people
    
    if flag == 0:
        print(result)
        break

    result += 1