# [BOJ] 7562. 나이트의 이동
# 소요 시간 : 30분

import sys
input = sys.stdin.readline
from collections import deque


dy = [1, 2, 1, 2, -1, -2, -1, -2]
dx = [2, 1, -2, -1, 2, 1, -2, -1]

def bfs(knight):
    board[knight[0]][knight[1]] = True
    queue = deque([knight])
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for d in range(8):
                move_y, move_x = y + dy[d], x + dx[d]
                if 0 <= move_y < l and 0 <= move_x < l and not board[move_y][move_x]:
                    board[move_y][move_x] = True
                    if (move_y, move_x) == goal:
                        return cnt
                    queue.append((move_y, move_x))
                    
    


T = int(input())

for _ in range(T):
    l = int(input())
    board = [[False] * l for _ in range(l)]
    knight = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))

    print(0 if knight == goal else bfs(knight))
