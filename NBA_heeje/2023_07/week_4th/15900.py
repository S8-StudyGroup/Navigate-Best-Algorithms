# [BOJ] 15900. 나무 탈출
# 소요 시간 : 00분

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append(1)
    visited = set()
    visited.add(1)
    cnt = 0
    turn = 0
    while queue:
        for _ in range(len(queue)):
            v = queue.popleft()                

            if len(adj_list[v]) == 1:
                cnt += turn

            for w in adj_list[v]:
                if w not in visited:
                    visited.add(w)
                    queue.append(w)

        turn += 1
    
    return "Yes" if cnt % 2 else "No"


N = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

print(bfs())