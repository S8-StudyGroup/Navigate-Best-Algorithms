# [SWEA] 1953. 탈주범 검거
# 소요 시간 : 00분

from collections import deque

# 상하좌우 -> 0123
manhole = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for tc in range(int(input())):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    connect = [1, 0, 3, 2]

    step = 1
    que = deque([])
    que.append([r, c, step])
    visited[r][c] = 1
    cnt = 0

    while que:
        nx, ny, step = que.popleft()
        if step > l:
            break
        cnt += 1
        for num in manhole[tunnel[nx][ny]]:
            cx, cy = nx + direction[num][0], ny + direction[num][1]
            if 0 <= cx < n and 0 <= cy < m:
                if connect[num] in manhole[tunnel[cx][cy]] and not visited[cx][cy]:
                    que.append([cx, cy, step + 1])
                    visited[cx][cy] = 1

    print(f'#{tc + 1} {cnt}')