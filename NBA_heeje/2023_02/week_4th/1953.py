# [SWEA] 1953. 탈주범 검거
# 소요 시간 : 20분

from collections import deque


def bfs():
    visited = set()
    visited.add((R, C))
    queue = deque()
    queue.append((R, C, 1))

    while queue:
        y, x, time = queue.popleft()

        if time == L:
            break

        for d in tunnel_info[matrix[y][x]]:
            move_y, move_x = y + dy[d], x + dx[d]

            if (0 <= move_y < N and 0 <= move_x < M and
                (move_y, move_x) not in visited and
                (d + 2) % 4 in tunnel_info[matrix[move_y][move_x]]):
                visited.add((move_y, move_x))
                queue.append((move_y, move_x, time + 1))

    return f"#{tc} {len(visited)}"


# 상좌하우 탐색
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

# 각 터널의 방향별 연결 여부 [상, 좌, 하, 우]
tunnel_info = [
    [],
    [0, 1, 2, 3],
    [0, 2],
    [1, 3],
    [0, 3],
    [2, 3],
    [1, 2],
    [0, 1],
]

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    print(bfs())