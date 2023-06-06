# [BOJ] 15661. 링크와 스타트
# 소요 시간 : 00분

size = int(input())
board = [list(map(int, input().split())) for _ in range(size)]
last_num = size - 1
visited = [False] * size
min_diff = float('inf')


def score():
    global min_diff

    link_team = 0
    start_team = 0

    for i in range(size):
        for j in range(i + 1, size):
            if visited[i] and visited[j]:
                link_team += board[i][j]
            elif not visited[i] and not visited[j]:
                start_team += board[i][j]
    
    diff = abs(link_team - start_team)    
    min_diff = min(min_diff, diff)


def dfs(num):

    if num == last_num:
        score()
        return
    
    visited[num] = True
    dfs(num + 1)
    visited[num] = False
    dfs(num + 1)


for i in range(size):
    for j in range(i + 1, size):
        board[i][j] += board[j][i]


dfs(0)
print(min_diff)