# [BOJ] 7562. 나이트의 이동
# 소요 시간 : 30분

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(si, sj):
    visited = [[0] * l for _ in range(l)]
    queue = []
    queue.append((si, sj))
    visited[si][sj] = 1

    while queue:
        px, py = queue.pop(0)

        if px == ax and py == ay:
            return visited[px][py]

        for d in range(8):
            nx = px + dx[d]
            ny = py + dy[d]

            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[px][py] + 1
            else:
                nx -= dx[d]
                ny -= dy[d]


t = int(input())
for tc in range(t):
    l = int(input())
    x, y = map(int, input().split())
    ax, ay = map(int, input().split())

    answer = bfs(x, y)

    print(answer - 1)