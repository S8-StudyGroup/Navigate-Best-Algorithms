# [BOJ] 16234. 인구 이동
# 소요 시간 : 60분
def bfs(i, j):
    queue = []
    union = []
    queue.append((i, j))
    union.append((i, j))
    while queue:
        x, y = queue.pop(0)
        for d in range(4):
            nx = x + di[d]
            ny = y + dj[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                here = board[x][y]
                beside = board[nx][ny]
                # 조건 충족시 연합
                if L <= abs(here - beside) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union


N, L, R = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
days = 0
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]
# 전체 돌면서 오른쪽, 아래와 차이 검사
while True:
    moved = False
    visited = [[0] * (N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                info = bfs(i, j)
                # 현재 연합인 국가끼리 인구 이동
                if len(info) > 1:
                    moved = True
                    num = sum([board[a][b] for a, b in info]) // len(info)
                    for x, y in info:
                        board[x][y] = num
    if not moved:
        break
    days += 1

print(days)