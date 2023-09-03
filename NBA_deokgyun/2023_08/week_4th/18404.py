# [BOJ] 18404. 현명한 나이트
# 소요 시간 : 00분

from collections import deque

length, cnt = map(int, input().split())

func = lambda x: int(x) - 1

board = [[0 for _ in range(length)] for _ in range(length)]
visited = [[0 for _ in range(length)] for _ in range(length)]

qu = deque([list(map(func, input().split())) + [1]])

while qu:
    i, j, k  = qu.popleft()
    if not visited[i][j]:
        visited[i][j] = k
        for di, dj in [[2,1], [2,-1], [-2,1], [-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]:
            ni = i + di
            nj = j + dj
            if (0 <= ni < length and 0 <= nj < length):
                qu.append([ni,nj,k+1])

for k in range(1, cnt + 1):
    i, j = map(func, input().split())
    print(visited[i][j] - 1, end=" ")