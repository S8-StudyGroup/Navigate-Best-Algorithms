# [SWEA] 1953. 탈주범 검거
# 소요 시간 : 50분

def bfs(start):
    queue = [start]
    visited = [[0] * M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    cnt = 1
    while queue:
        x, y = queue.pop(0)
        if visited[x][y] < L:
            for d in structure[tunnels[x][y]]:
                move_x, move_y = x + dx[d], y + dy[d]
                if (
                    0 <= move_x < N
                    and 0 <= move_y < M
                    and tunnels[move_x][move_y] != 0
                    and visited[move_x][move_y] == 0
                    and (d + 2) % 4 in structure[tunnels[move_x][move_y]]
                ):
                    visited[move_x][move_y] = visited[x][y] + 1
                    queue.append((move_x, move_y))
                    cnt += 1
    return cnt


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

structure = {
    1: [0, 1, 2, 3],
    2: [0, 2],
    3: [1, 3],
    4: [0, 3],
    5: [2, 3],
    6: [1, 2],
    7: [0, 1],
}

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnels = [list(map(int, input().split())) for _ in range(N)]

    print("#%d %d" % (tc, bfs((R, C))))