# [BOJ] 18404. 현명한 나이트
# 소요 시간 : 00분

from collections import deque
import sys
input = sys.stdin.readline


def bfs(sy, sx, M):
    queue = deque()
    queue.append((sy, sx, 0))
    visited = set()
    visited.add((sy, sx))
    cnt = 0

    while queue:
        y, x, time = queue.popleft()
        
        if min_moves_opp_pieces.get((y, x)) == 0:
            min_moves_opp_pieces[(y, x)] = time
            cnt += 1

        if cnt == M:
            return
        
        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited:
                visited.add((ny, nx))
                queue.append((ny, nx, time + 1))


direction = [
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2),
    (2, 1),
    (-2, 1),
    (2, -1),
    (-2, -1),
]

N, M = map(int, input().split())
Y, X = map(int, input().split())
min_moves_opp_pieces = dict()
opp_pieces_list = []
for _ in range(M):
    A, B = map(int, input().split())
    opp_pieces_list.append((A - 1, B - 1))
    min_moves_opp_pieces[(A - 1, B - 1)] = 0

bfs(Y - 1, X - 1, M)

for i in range(M):
    print(min_moves_opp_pieces[opp_pieces_list[i]], end=" ")