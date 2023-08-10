# [SWEA] 1953. 탈주범 검거
# 소요 시간 : 00분

from collections import deque

def bfs(row, col):
    visited = [[False] * m for _ in range(n)]
    visited[row][col] = True

    v = [row, col, 1]
    queue = deque([v])
    result = set()
    while queue:
        row, col, cnt = queue.popleft()
        if cnt == l + 1:
            break
        result.add((row, col))
        for d in direction[arr[row][col]]:
            nr, nc = row + dr[d], col + dc[d]
            if (
                0 <= nr < n
                and 0 <= nc < m
                and not visited[nr][nc]
                and arr[nr][nc] in check[d]
            ):
                visited[nr][nc] = True
                queue.append([nr, nc, cnt + 1])
    return len(result)

dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]
direction = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
check = {0: (1, 2, 5, 6), 1: (1, 2, 4, 7), 2: (1, 3, 4, 5), 3: (1, 3, 6, 7)}

for t in range(1, int(input()) + 1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{t} {bfs(r, c)}')