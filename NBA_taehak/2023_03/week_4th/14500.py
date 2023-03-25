# [BOJ] 14500. 테트로미노
# 소요 시간 : 00분
rsize, csize = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(rsize)]
visited = [[False] * csize for _ in range(rsize)]


def inrange(r, c):
    return 0 <= r < rsize and 0 <= c < csize


answer = 0
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
def dfs(r, c, cnt=0, result=0):
    global answer
    cnt += 1
    result += board[r][c]

    if cnt == 4:
        answer = max(answer, result)
        return 

    for dr, dc in delta:
        nr = r + dr
        nc = c + dc
        if inrange(nr, nc) and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, cnt, result)
            visited[nr][nc] = False


def aeou(r, c):
    '''
    ㅏㅓㅗㅜ
    '''
    if 0 < r < rsize-1 and 0 < c < csize-1:
        memo = []
        for dr, dc in delta:
            memo.append(board[r + dr][c + dc])
        return board[r][c] + sum(memo) - min(memo)
    elif r in [0, rsize] or c in [0, csize]:
        memo = board[r][c]
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if inrange(nr, nc):
                memo += board[nr][nc]
        return memo
    else:
        return 0


for r in range(rsize):
    for c in range(csize):
        visited[r][c] = True
        dfs(r, c)
        visited[r][c] = False
        answer = max(answer, aeou(r, c))

print(answer)