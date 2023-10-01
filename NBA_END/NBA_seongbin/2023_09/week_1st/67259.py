# [Programmers] 67259. 경주로 건설
# 소요 시간 : 00분
def solution(board):

    n = len(board)
    visited = [[False] * n for _ in range(n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    min_cost = float('inf')
    visited[0][0] = True

    def dfs(r, c, cost, d):
        nonlocal min_cost
        if r == n - 1 and c == n - 1:
            min_cost = min(min_cost, cost)
            return

        for direction in range(4):
            nr, nc = r + dr[direction], c + dc[direction]

            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True

                if d == -1 or d == direction:
                    dfs(nr, nc, cost + 100, direction)
                else:
                    dfs(nr, nc, cost + 600, direction)

                visited[nr][nc] = False

    dfs(0, 0, 0, -1)

    return min_cost
